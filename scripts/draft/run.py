from os import read
from common.auto_logger import log

from dataclasses import dataclass
from PIL import Image
import torchvision.transforms.functional as F

from utils import load_device
from utils import load_data

# import src.DEhance_Model as DEhance_Model

from src.Models import diffusionModel
from src.Models import referenceModel
from src.Models import WAllocateModel

from src.Trainers.Stage1_Trainer import trainer as Stage1_Trainer

# import src.EvalModel as EvalModel



import torch


# DEBUG

def read_image(path):
    try:
        img = Image.open(path).convert("RGB")
        img_tensor = F.to_tensor(img)
        return img_tensor
    except Exception as e:
        print(f"Error reading image {path}: {e}")
        return None

def show_image(img_tensor):
    try:
        if isinstance(img_tensor, torch.Tensor):
            img_pil = F.to_pil_image(img_tensor)
            img_pil.show()
        else:
            print("Input is not a valid tensor.")
    except Exception as e:
        print(f"Error displaying image: {e}")



# Basic Configs

DEBUG_MODE = True

avaliableGPU = [0, 1]
MULTIGPU = True

device = load_device.loadGPU(avaliableGPU)

# Dataset Configs

@dataclass
class DATASET_CONFG:
    image_size = [512, 512]
    channel = 3

# path or flist
dataset_path = {
    'train_cloud': '/home/scxys3/Desktop/data/CUHK-CR1/train/cloud',
    'train_label': '/home/scxys3/Desktop/data/CUHK-CR1/train/label',
    
    'test_cloud': '/home/scxys3/Desktop/data/CUHK-CR1/test/cloud',
    'test_label': '/home/scxys3/Desktop/data/CUHK-CR1/test/label',
}

log("loading datasets...")

train_inputs_flist = load_data.load_flist(dataset_path['train_cloud'])
train_labels_flist = load_data.load_flist(dataset_path['train_label'])

test_inputs_flist = load_data.load_flist(dataset_path['test_cloud'])
test_labels_flist = load_data.load_flist(dataset_path['test_label'])

# Training Configs

diffusionModel = diffusionModel.RDDM    # default, RDDM
# referenceModel = referenceModel.default   # default
# WAllocateModel = WAllocateModel.default   # default

# Stage I Configs

@dataclass
class STAGE_I_DIFFUSION_TRAINER_CONFIG:
    batch_size = 1
    epoch = 10000
    learning_rate = 8e-5
    sample_step = 100
    save_per_step = 100

    amp = False,
    ema_decay = 0.995

# Stage II Configs


# ---------------------------------- Training ----------------------------------

# Models

# Stage I Training 
# - train with resolution 1/4 purely on diffusion model

Stage_I_diffusion = diffusionModel(
    channel     = DATASET_CONFG.channel,
    img_size    = [d // 2 for d in DATASET_CONFG.image_size], # half resolution
)

# # Stage II
# # - train with full resolution while implementing WA and referecen Model

# Stage_II_diffusion = diffusionModel(
#     channel     = DATASET_CONFG.channel,
#     img_size    = DATASET_CONFG.image_size, # full size resolution
# )

# Stage_II_refModel = referenceModel(
#     channel     = DATASET_CONFG.channel,
#     img_size    = DATASET_CONFG.image_size,
# )

# Stage_II_WAllocateModel = WAllocateModel(
#     channel     = DATASET_CONFG.channel,
#     img_size    = DATASET_CONFG.image_size,
# )

# Stage_II_DE_Model = DEhance_Model(
#     diffusionModel = Stage_II_diffusion,
#     referenceModel = Stage_II_refModel,
#     WAllocateModel = Stage_II_WAllocateModel,
# )

# # Trainers

# show_image(read_image(train_inputs_flist[0]))

Stage_I_trainer = Stage1_Trainer(
    model = Stage_I_diffusion,
    
    inputs_flist = train_inputs_flist,
    labels_flist = train_labels_flist,

    epoch           = STAGE_I_DIFFUSION_TRAINER_CONFIG.epoch,
    batch_size      = STAGE_I_DIFFUSION_TRAINER_CONFIG.batch_size,
    learning_rate   = STAGE_I_DIFFUSION_TRAINER_CONFIG.learning_rate,
    sample_step     = STAGE_I_DIFFUSION_TRAINER_CONFIG.sample_step,
    save_per_step   = STAGE_I_DIFFUSION_TRAINER_CONFIG.save_per_step,

    amp             = STAGE_I_DIFFUSION_TRAINER_CONFIG.amp,
    ema_decay       = STAGE_I_DIFFUSION_TRAINER_CONFIG.ema_decay,

    debug = DEBUG_MODE,
)

# Stage_II_trainer = Stage2_Trainer(
#     model = Stage_II_DE_Model,

#     input = inputs,
#     label = labels,
#     mask  = masks,

#     debug = DEBUG_MODE,
#     device = device
# )

# # Start Training

# # Stage I

Stage_I_trainer.save(mileStone=12)
# Stage_I_trainer.load(mileStone=0)
# Stage_I_trainer.train()

# # Stage II

# Stage_II_trainer.load_diffusion(mileStone = -1, from_coarseTrain = True)
# Stage_II_trainer.load_reference(mileStone = -1)
# Stage_II_trainer.load_WAllocate(mileStone = -1)

# Stage_II_trainer.train_reference()
# Stage_II_trainer.train_WAllocate()
# Stage_II_trainer.train_all()

# # Testing

# @dataclass
# class EVALUATION:
#     test_round = 100
#     result_folder = RESULT_FOLDER

# EvalModel = EvalModel()

# testee = EvalModel(
#     model = Stage_II_DE_Model,
#     test_round      = EVALUATION.test_round,
#     result_folder   = EVALUATION.result_folder
# )

# testee.test()
