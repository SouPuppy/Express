from common.auto_logger import log
from ..Class.diffusionModel import ClassDiffusionModel as CLASS_DIFFUSION

class default(CLASS_DIFFUSION):
    def __init__(self, channel=None, img_size=None, debug=False, device=None):
        super().__init__(
            channel=channel,
            img_size=img_size,
            debug=debug,
            device=device
        )

    def __call__(self, *args, **kwargs):
        log("using [default] diffusion model")

        return default(*args, **kwargs)
