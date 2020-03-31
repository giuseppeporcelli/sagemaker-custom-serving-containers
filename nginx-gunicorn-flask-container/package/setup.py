from __future__ import absolute_import

from glob import glob
import os
from os.path import basename
from os.path import splitext

from setuptools import find_packages, setup

setup(
    name='nginx_gunicorn_flask_serving',
    version='1.0.0',
    description='Nginx gunicorn flask serving package.',
    keywords="Nginx gunicorn flask serving SageMaker",

    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],

    author='Giuseppe A. Porcelli',
    author_email='giu.porcelli@gmail.com',
    license='Apache License 2.0',

    install_requires=['sagemaker-containers']    
)
