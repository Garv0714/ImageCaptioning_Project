import numpy as np
import pandas as pd

def load_captions():
    # Dummy captions for demo
    return {"sample.jpg": ["a cat sitting on a mat", "a cute kitten resting"]}

def preprocess_image(img_path):
    from tensorflow.keras.preprocessing import image
    from tensorflow.keras.applications.inception_v3 import preprocess_input

    img = image.load_img(img_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x