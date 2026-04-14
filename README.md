# 🎬 AI Cinematic Poster Generator (Face-Preserved)

Generate **cinematic movie-style posters** and inject **real human faces** into them using AI.

This project combines:

* 🧠 **Stable Diffusion (SDXL)** → scene generation
* 👤 **InsightFace** → face swapping (identity preservation)
* ✨ **GFPGAN** → face enhancement & realism

---

## 🚀 Features

* Generate high-quality **cinematic posters**
* Preserve **real facial identity**
* Automatic **face detection & swapping**
* AI-based **face enhancement**
* Works on **CPU (slow)** and **GPU (fast)**

---

## 🏗️ Project Structure

```
project/
│
├── main.py                # Main pipeline script
├── requirements.txt      # Dependencies
├── face1.jpg             # Your image
├── face2.jpg             # Friend's image
├── GFPGANv1.4.pth        # Face enhancement model
├── output/               # Generated images
```

---

## ⚙️ Installation

### 1️⃣ Clone / Setup Environment

```bash
git clone <your-repo-url>
cd project
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install PyTorch (IMPORTANT)

#### 👉 CPU (for i3 / no GPU)

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

#### 👉 GPU (CUDA)

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

---

### 4️⃣ Download Required Models

#### 🔹 GFPGAN Model

Download:
👉 https://github.com/TencentARC/GFPGAN/releases

Place file:

```
GFPGANv1.4.pth
```

inside project root.

---

## ▶️ Usage

### 1️⃣ Add Input Images

* `face1.jpg` → Your face
* `face2.jpg` → Friend’s face

---

### 2️⃣ Run the Pipeline

```bash
python main.py
```

---

### 3️⃣ Output

Generated files:

```
base_poster.png     → AI generated poster
swapped.png         → faces swapped
final_output.png    → enhanced final result
```

---

## 🧠 How It Works

### Step 1: Poster Generation

Stable Diffusion XL generates a cinematic scene based on prompt.

### Step 2: Face Detection

InsightFace detects faces and extracts embeddings.

### Step 3: Face Swapping

Real faces are injected into the generated poster.

### Step 4: Enhancement

GFPGAN restores fine details (skin, beard, texture).

---

## ⚡ Performance Guide

| Setup           | Performance           |
| --------------- | --------------------- |
| i3 CPU          | Slow (5–20 min/image) |
| i5/i7 CPU       | Moderate              |
| GPU (GTX 1650+) | Fast 🔥               |

---

## ⚠️ Important Notes

* SDXL is **heavy** → CPU users should expect slow generation
* Face swap accuracy depends on:

  * face angle
  * lighting
  * image quality
* First run downloads models automatically (InsightFace)

---

## 🔧 Troubleshooting

### ❌ Torch not installing

```bash
pip install --upgrade pip setuptools wheel
```

---

### ❌ Faces swapped incorrectly

* Ensure:

  * clear frontal images
  * similar angles

---

### ❌ CUDA error

Change:

```python
.to("cuda")
```

➡️

```python
.to("cpu")
```

---

## 🚀 Future Improvements

* Add **ControlNet (pose control)**
* Build **FastAPI backend**
* Create **web UI (Streamlit)**
* Add **video trailer generation**

---

## 📌 Tech Stack

* Python
* PyTorch
* Diffusers (Stable Diffusion)
* InsightFace
* GFPGAN

---

## 🤝 Contribution

Feel free to fork, improve, and build on top of this project.

---

## ⭐ Final Note

This is not just an AI project — it’s a **real-world computer vision pipeline** combining:

* generative models
* facial recognition
* image restoration

---

🔥 *Build. Experiment. Break limits.*
