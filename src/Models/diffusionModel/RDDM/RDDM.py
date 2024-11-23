from common.auto_logger import log
from ...Class.diffusionModel import ClassDiffusionModel as CLASS_DIFFUSION

class RDDM(CLASS_DIFFUSION):
    def __init__(self, channel=None, img_size=None, debug=False, device=None):
        super().__init__(
            channel=channel,
            img_size=img_size,
            debug=debug,
            device=device
        )

    def __call__(self, *args, **kwargs):
        log("using [RDDM] diffusion model")

        model = UnetRes(
            dim=64,
            dim_mults=(1, 2, 4, 8),
            share_encoder=0,
            condition=condition,
            input_condition=input_condition
        )
        diffusion = ResidualDiffusion(
            model,
            image_size=image_size,
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

        return RDDM(*args, **kwargs)
