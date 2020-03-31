import pickle as pkl
from sagemaker_inference import content_types, decoder, default_inference_handler, encoder, errors
from multi_model_serving import encoder as xgb_encoders

class DefaultXGBoostInferenceHandler(default_inference_handler.DefaultInferenceHandler):

    def default_input_fn(self, input_data, content_type):
        """Take request data and de-serializes the data into an object for prediction.
        When an InvokeEndpoint operation is made against an Endpoint running SageMaker model server,
        the model server receives two pieces of information:
            - The request Content-Type, for example "application/json"
            - The request data, which is at most 5 MB (5 * 1024 * 1024 bytes) in size.
        The input_fn is responsible to take the request data and pre-process it before prediction.
        Args:
            input_data (obj): the request data.
            content_type (str): the request Content-Type.
        Returns:
            (obj): data ready for prediction. For XGBoost, this defaults to DMatrix.
        """
        return xgb_encoders.decode(input_data, content_type)

    def default_predict_fn(self, data, model):
        """A default predict_fn for XGBooost Framework. Calls a model on data deserialized in input_fn.
        Args:
            input_data: input data (Numpy array) for prediction deserialized by input_fn
            model: XGBoost model loaded in memory by model_fn
        Returns: a prediction
        """
        output = model.predict(data, validate_features=False)
        return output

    def default_output_fn(self, prediction, accept):
        """A default output_fn for XGBoost. Serializes predictions from predict_fn to JSON, CSV or NPY format.

        Args:
            prediction: a prediction result from predict_fn
            accept: type which the output data needs to be serialized

        Returns: output data serialized
        """
        return encoder.encode(prediction, accept)