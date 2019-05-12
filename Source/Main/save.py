# -*- coding: utf-8 -*-
import pickle

def save(save_path,data):
    with open (save_path, 'wb') as save00: pickle.dump(data, save00, pickle.HIGHEST_PROTOCOL)
    return