import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load your pre-trained model (update the path to your model)
model = load_model('custom_cnn_model.h5')

# Define the class names
class_names = ['Benign', 'Malignant']

# Function to preprocess the uploaded image
def preprocess_image(img):
    img = img.resize((224, 224))  # Resize the image to match the input size of the model
    img = image.img_to_array(img)  # Convert the image to an array
    img = np.expand_dims(img, axis=0)  # Expand dimensions to match the model input
    img = img / 255.0  # Normalize the image
    return img

# Streamlit app
st.title("Breast Tumor Classification")
st.write("Upload an image of the breast tumor to classify it as benign or malignant.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    processed_img = preprocess_image(img)

    # Make a prediction
    prediction = model.predict(processed_img)
    predicted_class = class_names[np.argmax(prediction)]

    # Display the prediction
    st.write(f"Prediction: {predicted_class}")
