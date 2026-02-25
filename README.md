# 🎙️ Voice Emotion Detection & AI Image Generation App

## Overview

This application is a **real-time Voice Emotion Detection and AI Image Generation system** built using:

* Streamlit (UI)
* Wav2Vec2 Emotion Recognition Model (Audio → Emotion)
* Stable Diffusion (Emotion → Image)
* PyTorch with CUDA (GPU acceleration)

The app records audio from the microphone, detects the speaker's emotion using AI, generates a supportive response, and creates an AI-generated image based on the detected emotion.

---

## Features

### 🎤 Voice Emotion Detection

* Records audio from microphone
* Uses pretrained Wav2Vec2 emotion recognition model
* Detects emotions such as:

  * Angry
  * Calm
  * Disgust
  * Fearful
  * Happy
  * Neutral
  * Sad
  * Surprised
  * Silence

---

### 🧠 AI Response Generation

* Generates supportive text responses based on emotion
* Example:

  * Happy → "Your positive energy is contagious!"
  * Sad → "It's okay to feel sad sometimes."

---

### 🎨 AI Image Generation

* Uses Stable Diffusion model
* Generates emotion-based artwork
* Example:

  * Happy → colorful joyful artwork
  * Sad → lonely figure in rain
  * Angry → fiery abstract image

---

### ⚡ GPU Acceleration

* Uses CUDA for fast processing
* Emotion detection and image generation run efficiently on GPU

---

### 🖥️ Interactive UI

Built using Streamlit with:

* Audio recording button
* Emotion display
* Confidence scores
* Generated image preview
* Audio playback

---

## System Architecture

```
Microphone Input
      ↓
Audio Recording
      ↓
Emotion Detection (Wav2Vec2)
      ↓
Emotion Result
      ↓
Response Generator
      ↓
Stable Diffusion Image Generation
      ↓
Display in Streamlit UI
```

---

## Project Structure

```
project/
│
├── streamlit_app.py      # Main application file
├── README.md             # Documentation
│
├── recordings/           # Saved audio files
├── results/              # Generated images
│
└── models/
    ├── emotion_model/    # Wav2Vec2 emotion model
    └── image_model/      # Stable Diffusion model
```

---

## Requirements

Python Version:

```
Python 3.12.4
```

Installed packages:

```
accelerate==1.8.1
altair==5.5.0
attrs==25.3.0
blinker==1.9.0
cachetools==6.1.0
certifi==2025.6.15
cffi==1.17.1
charset-normalizer==3.4.2
click==8.2.1
colorama==0.4.6
contourpy==1.3.2
cycler==0.12.1
diffusers==0.33.1
filelock==3.18.0
fonttools==4.58.4
fsspec==2025.5.1
gitdb==4.0.12
GitPython==3.1.44
huggingface-hub==0.33.0
idna==3.10
importlib_metadata==8.7.0
Jinja2==3.1.6
jsonschema==4.24.0
kiwisolver==1.4.8
MarkupSafe==3.0.2
matplotlib==3.10.3
mpmath==1.3.0
networkx==3.5
numpy==2.3.1
pandas==2.3.0
pillow==11.2.1
protobuf==6.31.1
psutil==7.0.0
pyarrow==20.0.0
pydeck==0.9.1
PyYAML==6.0.2
regex==2024.11.6
requests==2.32.4
safetensors==0.5.3
scipy==1.15.3
sounddevice==0.5.2
soundfile==0.13.1
streamlit==1.46.0
sympy==1.13.1
tokenizers==0.21.1
torch==2.6.0+cu124
torchaudio==2.6.0+cu124
torchvision==0.21.0+cu124
tqdm==4.67.1
transformers==4.52.4
watchdog==6.0.0
```

---

## Hardware Requirements

Minimum:

* CPU: Ryzen 5 / Intel i5
* RAM: 8GB
* GPU: Optional but recommended

Recommended:

* GPU: NVIDIA RTX 2060 or better
* VRAM: 6GB+
* RAM: 16GB

---

## Model Requirements

Emotion Model:

```
Wav2Vec2 Emotion Recognition Model
```

Image Model:

```
Stable Diffusion v1.5
```

---

## Installation

Step 1 — Clone or copy project

```
git clone <your repo>
cd project
```

---

Step 2 — Create virtual environment

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

---

Step 3 — Install requirements

```
pip install -r requirements.txt
```

---

## Run the Application

Start Streamlit server:

```
streamlit run streamlit_app.py
```

Then open browser:

```
http://localhost:8501
```

---

## How to Use

1. Click "Start Recording"
2. Speak into microphone
3. Wait for processing
4. View detected emotion
5. View generated AI image
6. View response message

---

## Example Output

Input:

```
"I am feeling great today!"
```

Output:

```
Emotion: Happy
Confidence: 92%
Response: Your enthusiasm is wonderful!
Generated Image: colorful joyful artwork
```

---

## GPU Acceleration

App automatically uses GPU if available:

```
CUDA detected → GPU used
Otherwise → CPU fallback
```

---

## Troubleshooting

### CUDA not detected

Check:

```
python -c "import torch; print(torch.cuda.is_available())"
```

Expected:

```
True
```

---

### Microphone not working

Check microphone permissions in Windows.

---

### Out of Memory

Close other GPU applications.

---

## Main File Description

```
streamlit_app.py
```

Contains:

* EmotionDetector class
* ResponseGenerator class
* Image generation logic
* Audio recording logic
* Streamlit UI

This file is fully self-contained.

---

## Future Improvements

Possible upgrades:

* Real-time continuous detection
* Emotion graph visualization
* Video emotion detection
* Multi-language support
* Cloud deployment

---

## Author

Rohit Singh

---

## License

Personal / Research Use

## Special Thanks
Thanks to Deepan Gautam for his [wav2vec2-emotion-recogniton model](https://huggingface.co/Dpngtm/wav2vec2-emotion-recognition)  
Thanks to Steven R. Livingstone for his [RAVDESS speech dataset](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)
