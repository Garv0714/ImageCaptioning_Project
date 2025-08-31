# 🖼️ Image Captioning Project

This project implements an **Image Captioning System** using Deep Learning.  
It takes an image as input and generates a human-like descriptive caption.  

---

## 📂 Project Structure

ImageCaptioning_Project/
│
├── data/ # Sample image(s)
│ └── sample.jpg
│
├── model/ # Trained / Pretrained model files
│ └── pretrained_model.keras
│
├── notebooks/ # Jupyter Notebook experiments
│ └── ImageCaptioning.ipynb
│
├── src/ # Source code
│ ├── data_prep.py # Data preprocessing
│ ├── model.py # Model architecture
│ ├── inference.py # Caption generation
│ └── utils.py # Helper functions
│
├── preprocess.py # Preprocessing entry script
├── app.py # Main Flask app (for deployment)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore
└── venv/ # Virtual environment (ignored in Git)

### Dataset
Download the dataset from [Google Drive](https://drive.google.com/drive/folders/1HseuFs1NUrn3Ayz7XSA5ZKzdNgeFTz8f?usp=sharing)
---

## 🚀 Features

- Extracts image features using CNN (InceptionV3/ResNet).
- Uses an RNN/LSTM-based decoder to generate captions.
- Supports training on custom datasets.
- Ready for deployment with **Flask API**.

---

## ⚙️ Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Garv0714/ImageCaptioning_Project.git
   cd ImageCaptioning_Project
Create and activate virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate     # For Windows
source venv/bin/activate  # For Mac/Linux
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
🧪 Usage
Add your images inside data/ folder.

Run the model for predictions:

bash
Copy code
python src/inference.py
Or open the notebook:

bash
Copy code
jupyter notebook notebooks/ImageCaptioning.ipynb
📊 Example Output
Input:


Output:
"A man standing in front of a historical fort near a river."

🛠️ Tech Stack
Python

TensorFlow / Keras

NumPy, Pandas

Flask

OpenCV, Matplotlib

👤 Author
Garv Sharma
📌 **[My LinkedIn](https://www.linkedin.com/in/garv0714)**
📌 **[GitHub Profile](https://github.com/Garv0714)**
