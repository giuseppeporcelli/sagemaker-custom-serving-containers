import os
import boto3
import pickle as pkl

from sagemaker_containers.beta.framework import (
    content_types, encoders, env, modules, transformer, worker)

def model_fn(model_dir):
    model_file = model_dir + '/xgboost-model'
    model = pkl.load(open(model_file, 'rb'))
    return model
