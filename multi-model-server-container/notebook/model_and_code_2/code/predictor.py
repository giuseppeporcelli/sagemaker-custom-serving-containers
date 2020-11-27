import os
import pickle as pkl

from multi_model_serving import encoder as xgb_encoders

def input_fn(input_data, content_type):    
    return xgb_encoders.decode(input_data, content_type)

def model_fn(model_dir):
    model_file = model_dir + '/model.bin'
    model = pkl.load(open(model_file, 'rb'))
    return model