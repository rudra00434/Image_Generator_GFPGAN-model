import torch
import cv2
import numpy as np
from PIL import Image
from diffusers import StableDiffusionXLPipeline
from insightface.app import FaceAnalysis
from gfpgan import GFPGANer

# -------------------------------
# STEP 1: Load SDXL model
# -------------------------------
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16
).to("cuda")

prompt = """
cinematic action movie poster, two men standing confidently,
post-apocalyptic industrial environment, fire, smoke, rain,
dramatic lighting, ultra realistic, 8k, movie poster style
"""

negative_prompt = "blurry, low quality, distorted face, extra limbs"

# Generate base poster
base_image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    guidance_scale=8.5,
    num_inference_steps=40
).images[0]

base_image.save("base_poster.png")

# -------------------------------
# STEP 2: Load Face Swap Model
# -------------------------------
app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0)

# Load images
poster = cv2.imread("base_poster.png")
face1 = cv2.imread("face1.jpg")  # your image
face2 = cv2.imread("face2.jpg")  # friend's image

poster_faces = app.get(poster)
face1_data = app.get(face1)[0]
face2_data = app.get(face2)[0]

# -------------------------------
# STEP 3: Face Swapping
# -------------------------------
from insightface.model_zoo import get_model

swapper = get_model("inswapper_128.onnx", download=True)

result = poster.copy()

if len(poster_faces) >= 2:
    result = swapper.get(result, poster_faces[0], face1_data, paste_back=True)
    result = swapper.get(result, poster_faces[1], face2_data, paste_back=True)

cv2.imwrite("swapped.png", result)

# -------------------------------
# STEP 4: Face Enhancement (GFPGAN)
# -------------------------------
gfpgan = GFPGANer(
    model_path="GFPGANv1.4.pth",
    upscale=2,
    arch="clean",
    channel_multiplier=2
)

_, _, enhanced = gfpgan.enhance(result, has_aligned=False)

cv2.imwrite("final_output.png", enhanced)

print(" Done! Check final_output.png")
