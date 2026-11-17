# 💵 RupeeScan – Smart Currency AI 

### AI-Powered Indian ₹50 Currency Note Detection Using YOLOv8

RupeeScan is a computer vision and deep learning project designed to detect Indian ₹50 currency notes using the YOLOv8 object detection model.

The system uses a custom-trained model to identify new-series Indian ₹50 banknotes, including their front and back sides. It demonstrates object detection, image annotation, model training, evaluation, and deployment using modern AI technologies.

## 🎥 Project Demo

**Watch the project demonstration here:**

👉 [Click Here to Watch Demo](https://drive.google.com/file/d/1Z1krPOFEI4XSRujaSL6h_3On3_i5hI-V/view?usp=drivesdk)


## 🚀 Key Features

- Detection of Indian ₹50 currency notes
- Support for front and back views of new-series ₹50 notes
- Custom-trained YOLOv8 object detection model
- Bounding-box visualization with confidence scores
- Image preprocessing using OpenCV
- Custom dataset annotation using Roboflow
- Model training and evaluation
- ONNX model export for optimized inference
- Python-based testing
- Interactive web application for demonstrating predictions

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| YOLOv8 | Object detection |
| PyTorch | Deep learning framework |
| OpenCV | Image processing and computer vision |
| Roboflow | Dataset annotation and management |
| ONNX | Model export and optimized inference |
| Ultralytics | YOLO model training and prediction |
| NumPy | Numerical operations |
| Google Colab / Jupyter Notebook | Model development and experimentation |
| Git & GitHub | Version control and project hosting |

## 🧠 How It Works

1. **Dataset Collection:** Images of Indian ₹50 currency notes are collected from different views.
2. **Image Annotation:** Currency notes are annotated using Roboflow.
3. **Dataset Preparation:** Images and labels are prepared in YOLO format.
4. **Model Training:** A YOLOv8 model is trained using the custom dataset.
5. **Model Evaluation:** Detection performance is analyzed using precision, recall, F1-score, and confusion matrices.
6. **Inference:** The trained model processes input images and predicts currency-note locations.
7. **Visualization:** Detected notes are highlighted using bounding boxes and confidence scores.

## 📂 Project Structure

```text
Smart-Currency-AI-V2/
│
├── dataset/                 # Dataset images and annotations
├── deployment/
│   ├── app.py               # Deployment application
│   └── requirements.txt
├── models/                  # Additional model assets, if present
├── notebooks/
│   └── Smart_Currency_AI_V2.ipynb
├── reports/
│   ├── weights/
│   │   ├── best.pt          # Best trained YOLOv8 model
│   │   ├── best.onnx        # Exported ONNX model
│   │   └── last.pt         # Final training checkpoint
│   ├── results.csv
│   ├── results.png
│   ├── confusion_matrix.png
│   └── evaluation_summary.txt
├── src/
├── data.yaml
├── requirements.txt
├── test.py
└── README.md
```

*Note: The structure above describes the project files. Some local dataset or model folders may not yet be available in the GitHub repository.*

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_NEW_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

### 2. Install dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Verify the trained model

The primary trained model is located at:

```text
reports/weights/best.pt
```

### 4. Run the test script

```bash
python test.py
```

**Important:** The test script may require an input image, camera, or other configuration. Check the paths and settings in `test.py` before running it.

## 🤖 Model Inference

For a basic YOLOv8 prediction using the trained weights:

```python
from ultralytics import YOLO

model = YOLO("reports/weights/best.pt")

results = model.predict(
    source="path/to/test_image.jpg",
    conf=0.25,
    save=True
)

print("Prediction completed.")
```

Replace `path/to/test_image.jpg` with the location of your test image.

Predicted images are saved to the Ultralytics output directory.

## 📊 Model Evaluation

The project includes training and evaluation artifacts such as:

- Precision, recall, and F1-score curves
- Confusion matrix visualizations
- Training results and loss curves
- Validation prediction images
- Evaluation summary files

These files are available in the `reports/` directory.

The project does not claim a specific accuracy percentage here; evaluation results should be interpreted from the recorded metrics and testing performance.

## 📁 Dataset

The custom dataset consists of annotated images of Indian ₹50 currency notes, including front and back views.

Annotations are prepared in YOLO-compatible format for object detection.

The dataset is intended for training and evaluating the detection model.

## ⚠️ Limitations

- The model focuses on new-series Indian ₹50 currency notes.
- Detection performance can vary with lighting, camera angle, blur, and occlusion.
- The project detects currency notes; it does not independently verify whether a note is genuine or counterfeit.
- Other denominations are outside the current model's scope.

## 🔮 Future Enhancements

- Support for additional Indian currency denominations
- Improved performance in challenging lighting conditions
- Real-time detection optimization
- Mobile application integration
- Expanded training dataset
- Improved deployment and user experience

## 👨‍💻 Developer

**Naveen SS**

GitHub: https://github.com/Naveenss0504

## 📌 Conclusion

RupeeScan demonstrates the practical application of deep learning and computer vision for Indian currency-note detection.

The project covers the machine learning workflow from dataset preparation and annotation to YOLOv8 training, evaluation, inference, and deployment.

It highlights hands-on experience with Python, OpenCV, PyTorch, Roboflow, and object detection technologies.
