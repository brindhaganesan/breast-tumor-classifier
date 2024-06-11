
from pathlib import Path

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from streamlit.runtime.uploaded_file_manager import UploadedFile

IMG_SIZE = 224


title = "Breast Cancer Detector"
st.set_page_config(page_title=title)
st.header(title)
st.markdown(
    "Predict whether breast tumours in [histopathological][hp] images are"
     " *benign* or *malignant (cancerous)*.\n\n"
    "[hp]: https://en.wikipedia.org/wiki/Histopathology"
)


def load_image(
    image: Path | UploadedFile, resize: bool = False
) -> Image.Image | tf.Tensor:
    """Convert an input image into the form expected by the model.

    Args:
        image (Path | UploadedFile): Image input.
        resize (bool): Whether or not to resize the image.

    Returns:
        PIL.image.Image | tensorflow.Tensor: A PIL Image. Or a 3D tensor, if
        resize is True.
    """
    img = Image.open(image)
    if resize:
        img = img.convert("RGB")  # Ensure image is in RGB mode
        img = tf.image.resize_with_pad(img, IMG_SIZE, IMG_SIZE)
    return img


@st.cache_resource
def load_model() -> tf.keras.Model:
    """Fetch pretrained model.

    Returns:
        tf.keras.Model: Trained convolutional neural network.
    """
    return tf.keras.models.load_model('custom_cnn_model.h5')


def get_prediction(image: Image.Image | tf.Tensor) -> None:
    """Obtain a prediction for the supplied image, and format the results for
    display.

    Args:
        image (Image | Tensor): An image (PIL Image or 3D tensor).
    """
    pred = model.predict(np.expand_dims(image, 0), verbose=0)[0][0]
    if pred < 0.5:
        st.success(f"Result: {pred:.5f}")
        st.markdown("Inference at *threshold==0.5*: :green['benign']")
    else:
        st.warning(f"Result: {pred:.5f}")
        st.markdown("Inference at *threshold==0.5*: :orange['malignant']")
    st.caption(
        "The model's output node has *sigmoid activation*, with 'malignant' "
        "being the positive class (1), and 'benign' being the negative "
        "class (0). Values close to 1 suggest high chances of malignancy, "
        "and vice versa."
    )



model = load_model()

upload_tab, sample_tab = st.tabs(["Upload an image", "Use a sample image"])

with upload_tab:
    with st.form("image-input-form", clear_on_submit=True):
        file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])
        submitted = st.form_submit_button("submit")
        if file:
            img = load_image(file, resize=True)
            st.image(img.numpy().astype("uint8"))
            get_prediction(img)


