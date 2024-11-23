class ClassDiffusionModel:
    def __init__(self, channel, img_size, debug, device):
        self.channel = channel
        self.img_size = img_size
        self.debug = debug
        self.device = device
    