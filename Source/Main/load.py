# -*- coding: utf-8 -*-
import pickle

def load(load_path):
    with open (load_path, 'rb') as load00: data = pickle.load(load00)
    return data