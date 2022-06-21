import altair as alt
import streamlit as st
import seaborn as sns

# importing the local modules
from important_variables import input_shape
from prediction import prediction

from PIL import Image


if __name__ == '__main__':
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



    # data = generate_data()
    type_plant = st.sidebar.radio("Select Type of Plant: ", ('General Disease Detection', 'Apple Plant',
                                'Grape Plant'))


    if type_plant == 'Apple Plant':
        st.title(f"{type_plant} illness Classification Interface")
        class_dict = {0:'Apple___Apple_scab', 2:'Apple___Cedar_apple_rust',
                1:'Apple___Black_rot', 3:'Apple___healthy'}
        prediction('apple_cnn1.h5', class_dict, input_shape)

    elif type_plant == 'Grape Plant':
        st.title(f"{type_plant} illness Classification Interface")
        class_dict = {0:'Grape___Black_rot', 2:'Grape___healthy',
                1:'Grape___Esca_', 3:'Grape___Leaf_blight_'}
        prediction('grape_cnn1.h5', class_dict, input_shape)
