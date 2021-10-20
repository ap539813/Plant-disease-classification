import altair as alt
import numpy as np
import streamlit as st
import seaborn as sns
# from sklearn.model_selection import train_test_split

# from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras.regularizers import l2

from PIL import Image


# Now we will define function to get train the model and return the model summary and performance
def create_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(4))
    model.add(Activation('softmax'))

    model.compile(optimizer='rmsprop', loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

img_width, img_height = 128, 128

# @st.cache
def prediction(model_path, class_dict):
    model = create_model()
    model.load_weights(model_path)
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        # image = cv2.imread(uploaded_file)
        image = Image.open(uploaded_file)
        st.image(image, caption='Input Image.', use_column_width=True)
        st.write("")
        image = image.resize((img_width, img_height))
        image = np.array(image).reshape((1, img_width, img_height, 3))/255

        
        pred = model.predict(image).argmax()
        # st.write(class_dict)
        st.write(f'Predicted Class is {class_dict[pred]}')



## Basic setup and app layout
st.set_page_config(layout="wide")

alt.renderers.set_embed_options(scaleFactor=2)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


st.sidebar.title("Control Panel")
left_col, middle_col, right_col = st.columns(3)
palette = sns.color_palette("bright")

tick_size = 12
axis_title_size = 16


# dimensions of our images.
img_width, img_height = 128, 128
if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)





# data = generate_data()
type_plant = st.sidebar.radio("Select Type of Plant: ", ('Apple Plant',
                              'Grape Plant'))


if type_plant == 'Apple Plant':
    st.title(f"{type_plant} illness Classification Interface")
    class_dict = {0:'Apple___Apple_scab', 2:'Apple___Cedar_apple_rust',
              1:'Apple___Black_rot', 3:'Apple___healthy'}
    prediction('apple_cnn1.h5', class_dict)
elif type_plant == 'Grape Plant':
    st.title(f"{type_plant} illness Classification Interface")
    class_dict = {0:'Grape___Black_rot', 2:'Grape___healthy',
              1:'Grape___Esca_', 3:'Grape___Leaf_blight_'}
    prediction('grape_cnn1.h5', class_dict)