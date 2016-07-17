from django.conf import settings
from grad_cam.torch_models import VqaTorchModel

import grad_cam.constants as constants

import PyTorch
import PyTorchHelpers


def grad_cam_vqa(input_question, input_answer, image_path, output_dir):

    return VqaTorchModel.predict(image_path, constants.VQA_CONFIG['input_sz'], constants.VQA_CONFIG['input_sz'], input_question, input_answer, output_dir)