from PIL import Image
import torch
from diffusers import StableDiffusionImg2ImgPipeline
import joblib

model_id_or_path = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path, torch_dtype=torch.float32)

pipe_path = "./pipe.joblib"
joblib.dump(pipe, pipe_path)