import importlib.util
import os
import argparse

def dict_to_namespace(config_dict):
    return argparse.Namespace(**config_dict)

def load(work_path):
    config_path = os.path.join(work_path, "config.py")

    # import config.py
    spec = importlib.util.spec_from_file_location("config_module", config_path)
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)

    config = config_module.CONFIG
    
    return dict_to_namespace(config)
