import gradio as gr
from ultralytics import YOLO

# On charge votre fichier .pt
model = YOLO("models/yolov8n-cls.pt") 

def predict(image):
    results = model(image)
    # On récupère l'image avec les prédictions dessinées dessus
    return results[0].plot()

# Création de l'interface
demo = gr.Interface(fn=predict, inputs="image", outputs="image")
demo.launch()
