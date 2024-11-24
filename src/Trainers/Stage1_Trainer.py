from common.auto_logger import log

from pathlib import Path
import torch
from torch.optim import Adam

def exists(x):
    return x is not None


class trainer:
    def __init__(
        self,
        model,                      # diffusion Model
        inputs_flist, labels_flist,
        epoch, batch_size,
        learning_rate,
        sample_step,
        save_per_step,


        debug, device,
        
        amp,
        ema_decay,

        weight_folder = "./weights",
        adam_betas=(0.9, 0.99),
    ):
        log(f""" -- StageI trainer --
            img_size {model.img_size}
            DEBUG_MODE [{'ON' if debug else 'OFF'}]
""")
        
        self.model = model.get_diffusionModel()
        self.opt = Adam(self.model.parameters(), lr=learning_rate, betas=adam_betas)
        

        self.results_folder = Path(weight_folder)

    def load(self, mileStone):
        path = Path(self.results_folder / f'model-{mileStone}.pt')

        if path.exists():
            data = torch.load(
                str(path), map_location=self.device)

            model = self.accelerator.unwrap_model(self.model)
            model.load_state_dict(data['model'])

            self.step = data['step']
            self.opt.load_state_dict(data['opt'])
            self.ema.load_state_dict(data['ema'])

            if exists(self.accelerator.scaler) and exists(data['scaler']):
                self.accelerator.scaler.load_state_dict(data['scaler'])

            print("load model - "+str(path))

        self.ema.to(self.device)
