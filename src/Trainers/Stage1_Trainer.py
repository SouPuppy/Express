from common.auto_logger import log

from pathlib import Path
import torch
from torch.optim import Adam
from accelerate import Accelerator
from ema_pytorch import EMA

def exists(x):
    return x is not None


class trainer:
    def __init__(
        self,
        model,
        inputs_flist, labels_flist,
        epoch, batch_size,
        learning_rate,
        sample_step,
        save_per_step,

        debug,
        
        amp,
        ema_decay,

        weight_folder = "./weights/diffusion",
        adam_betas=(0.9, 0.99),
    ):
        log(f"""StageI trainer
            - img_size {model.img_size}
            - DEBUG_MODE [{'ON' if debug else 'OFF'}]
""")
        
        split_batches = True,
        fp16 = False
        ema_update_every = 10

        self.accelerator = Accelerator(
            split_batches=split_batches,
            mixed_precision='fp16' if fp16 else 'no'
        )
        self.model = model.get_diffusionModel()
        self.opt = Adam(self.model.parameters(), lr=learning_rate, betas=adam_betas)

        if self.accelerator.is_main_process:
            self.ema = EMA(self.model, beta=ema_decay,
                           update_every=ema_update_every)
            
            self.results_folder = Path(weight_folder)

        self.weight_folder = weight_folder

        # training info
        self.step = 0

        # using Accelerator
        self.model, self.opt = self.accelerator.prepare(self.model, self.opt)
        device = self.accelerator.device
        self.device = device

    def load(self, mileStone):
        """
            mileStone = -1: load latest
        """
        path = None

        mileStone_prefix = self.weight_folder + '/model-'

        if mileStone == -1:
            paths = list(self.results_folder.glob(f'{mileStone_prefix}*.pt'))    
            if not len(paths) == 0:
                paths.sort(key=lambda x: int(x.stem.split('-')[1]))
                path = paths[-1]
        else:
            path = Path(self.results_folder / f'{mileStone_prefix}{mileStone}.pt')

        if path and path.exists():
            data = torch.load(
                str(path), map_location=self.device)

            model = self.accelerator.unwrap_model(self.model)
            model.load_state_dict(data['model'])

            self.step = data['step']
            self.opt.load_state_dict(data['opt'])
            self.ema.load_state_dict(data['ema'])

            if exists(self.accelerator.scaler) and exists(data['scaler']):
                self.accelerator.scaler.load_state_dict(data['scaler'])

            print(f"load {mileStone_prefix}"+str(path))
        else:
            if path:
                log(f"{mileStone_prefix}{mileStone}.pt not found", "warning")
            else:
                log(f"{mileStone_prefix}*.pt not found", "warning")

        self.ema.to(self.device)
    
    def save(self, mileStone):
        if not self.accelerator.is_local_main_process:
            return

        data = {
            'step': self.step,
            'model': self.accelerator.get_state_dict(self.model),
            'opt': self.opt.state_dict(),
            'ema': self.ema.state_dict(),
            'scaler': self.accelerator.scaler.state_dict() if exists(self.accelerator.scaler) else None
        }
        log(f"saving mileStone {mileStone}.pt")
        torch.save(data, str(self.results_folder / f'{mileStone}.pt'))