from sagemaker_inference.default_handler_service import DefaultHandlerService
from sagemaker_inference.transformer import Transformer
from multi_model_serving.default_inference_handler import DefaultXGBoostInferenceHandler

import os
import sys

ENABLE_MULTI_MODEL = os.getenv("SAGEMAKER_MULTI_MODEL", "false") == "true"

class HandlerService(DefaultHandlerService):
    def __init__(self):
        self._initialized = False
        
        transformer = Transformer(default_inference_handler=DefaultXGBoostInferenceHandler())
        super(HandlerService, self).__init__(transformer=transformer)

    def initialize(self, context):
        # This code is a workaround to fix a bug in the inference toolkit not setting the
        # user module path correctly when multi-model is enabled.
        # To be removed when the toolkit fix is available.
        if (not self._initialized) and ENABLE_MULTI_MODEL:
            code_dir = context.system_properties.get("model_dir") + '/code'
            sys.path.append(code_dir)
            self._initialized = True
        
        # Printing system properties for debugging purposes.
        print('Context system properties: ')
        print(context.system_properties)

        super().initialize(context)
