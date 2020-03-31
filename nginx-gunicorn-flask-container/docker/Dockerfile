FROM ubuntu:16.04

# Set a docker label to enable container to use SAGEMAKER_BIND_TO_PORT environment variable if present
LABEL com.amazonaws.sagemaker.capabilities.accept-bind-to-port=true

# Install python and other runtime dependencies
RUN apt-get update && \
    apt-get -y install \
        build-essential \
        libatlas-dev \
        git \
        wget \
        curl \
        nginx \
        jq

RUN echo 'installing miniconda' && \
    curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -bfp /miniconda3 && \
    rm Miniconda3-latest-Linux-x86_64.sh

ENV PATH=/miniconda3/bin:${PATH}

RUN conda install python=3.6 && \
    conda update -y conda && \
    conda install -c conda-forge pyarrow=0.14.1 && \
    conda install -c mlio -c conda-forge mlio-py=0.1

# Python won’t try to write .pyc or .pyo files on the import of source modules
# Force stdin, stdout and stderr to be totally unbuffered. Good for logging
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install latest version of XGBoost
RUN pip install --no-cache -I xgboost==0.90

WORKDIR /

# Install the serving module.
COPY code/nginx_gunicorn_flask_serving-1.0.0.tar.gz /nginx_gunicorn_flask_serving-1.0.0.tar.gz
RUN pip install nginx_gunicorn_flask_serving-1.0.0.tar.gz && rm /nginx_gunicorn_flask_serving-1.0.0.tar.gz

ENV SAGEMAKER_SERVING_MODULE nginx_gunicorn_flask_serving.serving:main
