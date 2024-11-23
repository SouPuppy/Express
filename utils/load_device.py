import os
from common.auto_logger import log

import torch

def loadGPU(avaliableGPU):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    if (not torch.cuda.is_available()):
        log('CUDA is not available. Script will not be executed.')
        exit(0)
    
    total_gpus = torch.cuda.device_count()
    log(f"Total GPUs detected: {total_gpus}")

    valid_gpus = [gpu for gpu in avaliableGPU if gpu < total_gpus]
    if not valid_gpus:
        log(f"No valid GPUs found in the provided list: {avaliableGPU}. Falling back to CPU.")
        return torch.device("cpu")

    os.environ['CUDA_VISIBLE_DEVICES'] = ','.join(str(e) for e in avaliableGPU)
    log(f"Using GPUs: {valid_gpus}")
    
    return device