import yaml
import os
import argparse

from src.Models.UNet import optimizer

model_paths = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/Models'))
model_infos_path = os.path.join(model_paths, 'model_list.yml')

def dict_to_namespace(config_dict):
    return argparse.Namespace(**config_dict)

def load_ModelList(dataset_name):
    if not os.path.isfile(model_infos_path):
        raise FileNotFoundError(f"{model_infos_path} does not exist.")

    with open(model_infos_path, 'r') as file:
        global config
        config = yaml.safe_load(file)
    

def load_model(model_name):
    #* Load Model Config
    MODEL_CONFIG = config[model_name]

    import model_paths + model_name.model.model as model
    import model_paths + model_name.model.optimizer as optimizer

    #* Load Model
    log("loading model...")
    model = model().todevice(device)

    #* Load Optimizer
    log("loading optimizer...")
    optimizer = optimizer().todevice(device)

    #* Load Checkpoint
    log("loading checkpoint...")
    checkpoint_path = os.path.join(model_paths, 'pretrain/checkpoint.pth')
    if os.path.isfile(checkpoint_path):
        checkpoint = torch.load(checkpoint_path)


    #* Mount on Device
    

    return model, optimizer, checkpoint