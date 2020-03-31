from __future__ import absolute_import

from subprocess import CalledProcessError
from retrying import retry
from multi_model_serving import handler_service
from sagemaker_inference import model_server

HANDLER_SERVICE = handler_service.__name__

def _retry_if_error(exception):
    return isinstance(exception, CalledProcessError)

@retry(stop_max_delay=1000 * 30,
       retry_on_exception=_retry_if_error)
def _start_model_server():
    # there's a race condition that causes the model server command to
    # sometimes fail with 'bad address'. more investigation needed
    # retry starting mms until it's ready
    model_server.start_model_server(handler_service=HANDLER_SERVICE)

if __name__ == '__main__':
    _start_model_server()
