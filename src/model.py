from tensorflow.keras.models import load_model

def get_model():
    # Load pretrained/dummy model
    model = load_model("model/pretrained_model.keras", compile=False)
    return model