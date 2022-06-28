from create_model import create_model, AlexNet
from important_variables import img_height, img_width
import streamlit as st
from PIL import Image
import numpy as np

def prediction_individual_plant(model_path, class_dict, input_shape):
    model = create_model(input_shape)
    model.load_weights(model_path)
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        # image = cv2.imread(uploaded_file)
        image = Image.open(uploaded_file)
        col1, col2 = st.columns(2)
        col1.image(image, caption='Input Image.', use_column_width=True)
        st.write("")
        image = image.resize((img_width, img_height))
        image = np.array(image).reshape((1, img_width, img_height, 3))/255

        
        pred = model.predict(image).argmax()

        
        # st.write(class_dict)
        if class_dict[pred] == "Apple___Apple_scab":
            col2.error("This is not a healthy Apple Plant. It has a de named APPLE SCAB")
            col2.write("To know more about about the disease and it's cure check out this [link](https://arborjet.com/2019/03/28/apple-scab-symptoms-and-how-to-treat)")

        elif class_dict[pred] == "Apple___Black_rot":
            col2.error("This is not a healthy Apple Plant. It has a de named BLACK ROT")
            col2.write("To know more about about the disease and it's cure check out this [link](https://extension.umn.edu/plant-diseases/black-rot-apple)")
        
        elif class_dict[pred] == "Apple___Cedar_apple_rust":
            col2.error("This is not a healthy Apple Plant. It has a disease named CEDAR APPLE RUST")
            col2.write("To know more about about the disease and it's cure check out this [link](https://gardenerspath.com/how-to/disease-and-pests/cedar-apple-rust-control/)")
        
        elif class_dict[pred] == "Apple___healthy":
            col2.success("Congrats This is a healthy Apple Plant")
        
        elif class_dict[pred] == "Grape___Black_rot":
            col2.error("This is not a healthy Grape Plant. It has a de named BLACK ROT")
            col2.write("To know more about about the disease and it's cure check out this [link](https://www.gardeningknowhow.com/edible/fruits/grapes/black-rot-grape-treatment.htm)")
        
        elif class_dict[pred] == "Grape___healthy":
            col2.success("Congrats This is a healthy Grape Plant")
        
        elif class_dict[pred] == "Grape___Esca_":
            col2.error("This is not a healthy Grape Plant. It has a de named ESCA")
            col2.write("To know more about about the disease and it's cure check out this [link](http://ipm.ucanr.edu/PMG/r302100511.html)")
        
        elif class_dict[pred] == "Grape___Leaf_blight_":
            col2.error("This is not a healthy Grape Plant. It has a de named LEAF BLIGHT")
            col2.write("To know more about about the disease and it's cure check out this [link](https://www.goodfruit.com/11-tips-to-beat-grape-fungal-diseases)")


def prediction_general(model_path, class_dict, input_shape):
    model = AlexNet(input_shape)
    model.load_weights(model_path)
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        # image = cv2.imread(uploaded_file)
        image = Image.open(uploaded_file)
        col1, col2 = st.columns(2)
        col1.image(image, caption='Input Image.', use_column_width=True)
        st.write("")
        image = image.resize((img_width, img_height))
        image = np.array(image).reshape((1, img_width, img_height, 3))/255

        
        pred = model.predict(image).argmax()

        
        # st.write(class_dict)
        if class_dict[pred] == "Apple___Apple_scab":
            col2.error("This is not a healthy Apple Plant. It has a de named APPLE SCAB")
            col2.write("To know more about about the disease and it's cure check out this [link](https://arborjet.com/2019/03/28/apple-scab-symptoms-and-how-to-treat)")

        elif class_dict[pred] == "Apple___Black_rot":
            col2.error("This is not a healthy Apple Plant. It has a de named BLACK ROT")
            col2.write("To know more about about the disease and it's cure check out this [link](https://extension.umn.edu/plant-diseases/black-rot-apple)")
        
        elif class_dict[pred] == "Apple___Cedar_apple_rust":
            col2.error("This is not a healthy Apple Plant. It has a disease named CEDAR APPLE RUST")
            col2.write("To know more about about the disease and it's cure check out this [link](https://gardenerspath.com/how-to/disease-and-pests/cedar-apple-rust-control/)")
        
        elif class_dict[pred] == "Apple___healthy":
            col2.success("Congrats This is a healthy Apple Plant")
        
        elif class_dict[pred] == "Grape___Black_rot":
            col2.error("This is not a healthy Grape Plant. It has a de named BLACK ROT")
            col2.write("To know more about about the disease and it's cure check out this [link](https://www.gardeningknowhow.com/edible/fruits/grapes/black-rot-grape-treatment.htm)")
        
        elif class_dict[pred] == "Grape___healthy":
            col2.success("Congrats This is a healthy Grape Plant")
        
        elif class_dict[pred] == "Grape___Esca_":
            col2.error("This is not a healthy Grape Plant. It has a de named ESCA")
            col2.write("To know more about about the disease and it's cure check out this [link](http://ipm.ucanr.edu/PMG/r302100511.html)")
        
        elif class_dict[pred] == "Grape___Leaf_blight_":
            col2.error("This is not a healthy Grape Plant. It has a de named LEAF BLIGHT")
            col2.write("To know more about about the disease and it's cure check out this [link](https://www.goodfruit.com/11-tips-to-beat-grape-fungal-diseases)")
