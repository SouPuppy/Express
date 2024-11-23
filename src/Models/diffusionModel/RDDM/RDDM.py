from common.auto_logger import log

log("loading RDDM...")

from .residual_denoising_diffusion_pytorch import (ResidualDiffusion,
                                                      Unet, UnetRes,
                                                      set_seed)

class RDDM:
    def __init__(self, channel, img_size, debug, device):
        print(f"channel {channel}")
        print(f"img_size {img_size}")
        print(f"debug {debug}")
        print(f"device {device}")
        
        condition = True
        input_condition = False
        input_condition_mask = False
        sum_scale = 1

        self.model = UnetRes(
            dim=64,
            dim_mults=(1, 2, 4, 8),
            share_encoder=0,
            condition=condition,
            input_condition=input_condition
        )
        self.diffusion = ResidualDiffusion(
            self.model,
            image_size=img_size,
            timesteps=1000,           # number of steps
            # number of sampling timesteps (using ddim for faster inference [see citation for ddim paper])
            sampling_timesteps=5,
            objective='pred_res_noise',
            loss_type='l1',            # L1 or L2
            condition=condition,
            sum_scale = sum_scale,
            input_condition=input_condition,
            input_condition_mask=input_condition_mask
        )
            