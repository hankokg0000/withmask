from fastapi import FastAPI, Request
from PIL import Image
import numpy as np
import cv2
import io
import base64
from tensorflow.keras.models import load_model

def image2base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="png")
    base64_string = base64.b64encode(buffered.getvalue())
    return base64_string


def base642image(base64_string):
    imgdata = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(imgdata))
    return image

def preprocess(rgb):
    x = cv2.resize(rgb, (32, 32)) / 255.
    return x.reshape((1, 32, 32, 3))

label_dict = {
    0: "without mask",
    1: "with mask"
}
model = load_model("best_model.h5")
app = FastAPI()

@app.get("/")
def index():
    return {
        "message": "API is running normally."
    }

@app.post("/api/")
async def api(request: Request):
    
    body = await request.json()
    b64 = body["image"]
    image = np.array(base642image(b64))
    x = preprocess(image)
    y_pred = model.predict(x)
    pred = label_dict[y_pred.argmax()]
    
    return {
        "class": pred
    }
