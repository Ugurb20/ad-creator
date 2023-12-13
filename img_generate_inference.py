import io
import torch
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import joblib
import os

def load_pipe():
    file_path = os.path.join(".","pipe.joblib")
    pipe = joblib.load(file_path)
    return pipe

def generate_img(pipe,image,prompt, color):  
    init_image = Image.open(io.BytesIO(image)).convert("RGB")
    prompt = prompt + color + " brand " + color + " theme."
    print(prompt)
    images = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images
    images[0].save("photo/coffee-mug.png")

    