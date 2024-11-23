from common.auto_logger import log

from dataclasses import dataclass
from PIL import Image

from utils import load_device
from utils import load_data

# import src.DEhance_Model as DEhance_Model


from src.Models import diffusionModel
from src.Models import referenceModel
from src.Models import WAllocateModel

from src.Trainers.Stage1_Trainer import trainer as Stage1_Trainer

# import src.EvalModel as EvalModel


# Basic Configs

DEBUG_MODE = True
WEIGHT_FOLDER = './weights'
RESULT_FOLDER = './results'

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

train_inputs = load_data.load(dataset_path['train_cloud'])
train_labels = load_data.load(dataset_path['train_label'])

test_inputs = load_data.load(dataset_path['test_cloud'])
test_labels = load_data.load(dataset_path['test_label'])

# Training Configs

diffusionModel = diffusionModel.RDDM()    # default, RDDM
# diffusionModel = diffusionModel.default()   # default, RDDM
# referenceModel = referenceModel.default()   # default
# WAllocateModel = WAllocateModel.default()   # default

# Stage I Configs

@dataclass
class STAGE_I_DIFFUSION_CONFIG:
    batch_size = 1
    epoch = 10000
    lr = 1e-4
    sample_step = 100
    save_per_step = 100

# Stage II Configs

@dataclass
class STAGE_II_DIFFUSION_CONFIG:
    batch_size = 1
    epoch = 10000
    lr = 1e-4
    sample_step = 100
    save_per_step = 100

@dataclass
class STAGE_II_REFERENCE_CONFIG:
    batch_size = 10
    epoch = 10000
    lr = 1e-4
    save_per_step = 100

@dataclass
class STAGE_II_WEIGHTALLOC_CONFIG:
    batch_size = 10
    epoch = 10000
    lr = 1e-4
    save_per_step = 100

# ---------------------------------- Training ----------------------------------

# Models

# Stage I Training 
# - train with resolution 1/4 purely on diffusion model

Stage_I_diffusion = diffusionModel(
    channel     = DATASET_CONFG.channel,
    img_size    = [d // 2 for d in DATASET_CONFG.image_size], # half resolution

    debug = DEBUG_MODE,
    device = device
)

# # Stage II
# # - train with full resolution while implementing WA and referecen Model

# Stage_II_diffusion = diffusionModel(
#     channel     = DATASET_CONFG.channel,
#     img_size    = DATASET_CONFG.image_size, # full size resolution

#     debug = DEBUG_MODE,
#     device = device
# )

# Stage_II_refModel = referenceModel(
#     channel     = DATASET_CONFG.channel,
#     img_size    = DATASET_CONFG.image_size,

#     debug = DEBUG_MODE,
#     device = device
# )

# Stage_II_WAllocateModel = WAllocateModel(
#     channel     = DATASET_CONFG.channel,
#     img_size    = DATASET_CONFG.image_size,

#     debug = DEBUG_MODE,
#     device = device
# )

# Stage_II_DE_Model = DEhance_Model(
#     diffusionModel = Stage_II_diffusion,
#     referenceModel = Stage_II_refModel,
#     WAllocateModel = Stage_II_WAllocateModel,

#     debug = DEBUG_MODE,
#     device = device
# )

# # Trainers

# Stage_I_trainer = Stage1_Trainer(
    # model = Stage_I_diffusion,
    
    # inputs = F.interpolate(inputs, scale_factor=0.5, mode='bilinear', align_corners=False),
    # labels = F.interpolate(labels, scale_factor=0.5, mode='bilinear', align_corners=False),

    # debug = DEBUG_MODE,
    # device = device
# )

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

# Stage_I_trainer.load(mileStone = -1)
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
