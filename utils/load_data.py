from common.auto_logger import log

import os
import numpy as np
from pathlib import Path

exts = ['jpg', 'png', 'jpeg']

def load_flist(flist_path):
    # if flist_path like "*.flist"
    if flist_path.endswith(".flist"):
        log("loading dataset from flist: {}".format(flist_path))
        flist = load_file_list(flist_path)
        return flist
    else:
        log("loading dataset from directory: {}".format(flist_path))
        flist = load_directory(flist_path)
        return flist
    
def load_file_list(flist_path):
    flist = []
    # check if the flist_path is valid
    if not os.path.isfile(flist_path):
        log("flist path: {} does not exist!".format(flist_path), level="error")
        return []
    
    # get all files
    with open(flist_path, 'r') as f:
        for line in f:
            flist.append(line.strip())
    if len(flist) == 0:
        log("flist path: {} is empty!".format(flist_path), level="warning")
    else :
        log("[{}] items from flist: {} loaded".format(len(flist), flist_path))
    return flist

    
def load_directory(flist_path):
    flist = []
    # check if the path is valid
    if not os.path.isdir(flist_path):
        log("path: {} does not exist!".format(flist_path), level="error")
        return []
    
    # get all files
    for root, dirs, files in os.walk(flist_path):
        for file in files:
            if file.endswith(tuple(exts)):
                flist.append(os.path.join(root, file))
    if len(flist) == 0:
        log("path: {} is empty!".format(flist_path), level="warning")
    else :
        log("[{}] items from path: {} loaded".format(len(flist), flist_path))
    return flist