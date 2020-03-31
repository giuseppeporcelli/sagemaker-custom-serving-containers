import os
import pickle as pkl

def model_fn(model_dir):
    model_file = model_dir + '/xgboost-model'
    model = pkl.load(open(model_file, 'rb'))
    return model