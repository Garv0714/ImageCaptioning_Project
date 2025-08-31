from data_prep import preprocess_image
from model import get_model

def generate_caption(img_path):
    model = get_model()
    img = preprocess_image(img_path)

    # Dummy output (since model is not actually trained fully)
    return "This is a demo caption for the uploaded image."

if __name__ == "__main__":
    print(generate_caption("data/sample.jpg"))