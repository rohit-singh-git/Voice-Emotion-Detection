from diffusers import StableDiffusionPipeline
import torch

print("Modules loaded.")

# Load the model
pipe = StableDiffusionPipeline.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5",  # or use other models
    torch_dtype=torch.float16
)

print("Model loaded.")
pipe.to("cuda")  # Move to GPU

# Prompt based on emotion
emotion = "happy"  # Replace with actual detected emotion
prompt_map = {
    "angry": "a fiery red abstract face full of anger",
    "calm": "a peaceful scenic blue landscape",
    "disgust": "an unsettling surreal abstract face",
    "fearful": "a dark, eerie forest with fear and suspense",
    "happy": "a colorful joyous artwork full of sunshine",
    "neutral": "a plain minimalistic grayscale image",
    "sad": "a lonely figure standing in the rain",
    "surprised": "a burst of colors and abstract emotions"
}

print("Prompt defined.")

prompt = prompt_map.get(emotion, "an abstract artwork")

# Generate the image
image = pipe(prompt).images[0]

print("Image generated.")

image.save(f"{emotion}_image.png")
image.show()  # Optional: view the image
