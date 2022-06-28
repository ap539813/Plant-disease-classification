import altair as alt
import streamlit as st
import seaborn as sns

# importing the local modules
from important_variables import input_shape, data_url, css_file_path
from prediction import prediction_individual_plant, prediction_general
from add_style import local_css
import tensorflow as tf

from PIL import Image


## Basic setup and app layout
st.set_page_config(layout="wide")

alt.renderers.set_embed_options(scaleFactor=2)

# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

local_css(css_file_path)

print(st.session_state)

if 'home_page' not in st.session_state:
    st.session_state['home_page'] = True

def homepage():
    # if st.session_state['home_page']:
    # home_image = st.image("Plant disease classification.gif")

    markdown_image = st.markdown(
    f'<img style="max-width: 100%; height: auto;" src="data:image/gif;base64,{data_url}" alt="homepage gif">',
    unsafe_allow_html=True,
)

    c1, c2, c3 = st.columns([2,1,2])

    # c2.markdown('<div style="text-align: center;"> <h2> Developer Arnav Singhal </h2></div>', unsafe_allow_html=True)

    c2.markdown('')
    c2.markdown('')
    continue_forward = c2.button('Continue >>>')

    st.session_state['home_page'] = False
    # print(search_page)
    

    if continue_forward:
        print('going to the application!!')
        markdown_image.empty()
        main()

def main():
    # data = generate_data()
    st.sidebar.markdown(
    f'<img style="max-width: 100%; height: auto;" src="data:image/gif;base64,{data_url}" alt="homepage gif">',
    unsafe_allow_html=True,)

    st.sidebar.title("Control Panel")

    type_plant = st.sidebar.radio("Select Type of Plant: ", ('General Disease Detection', 'Apple Plant',
                                'Grape Plant'))

    if type_plant == 'General Disease Detection':
        st.title(f"{type_plant} illness Classification Interface")
        class_dict = {0: 'Apple___Apple_scab',
                1: 'Apple___Black_rot', 2: 'Apple___Cedar_apple_rust', 3: 'Apple___healthy', 4: 'Blueberry___healthy',
                5: 'Cherry_(including_sour)___Powdery_mildew', 6: 'Cherry_(including_sour)___healthy', 7: 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                8: 'Corn_(maize)___Common_rust_', 9: 'Corn_(maize)___Northern_Leaf_Blight', 10: 'Corn_(maize)___healthy', 11: 'Grape___Black_rot',
                12: 'Grape___Esca_(Black_Measles)', 13: 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 14: 'Grape___healthy', 15: 'Orange___Haunglongbing_(Citrus_greening)',
                16: 'Peach___Bacterial_spot', 17: 'Peach___healthy', 18: 'Pepper,_bell___Bacterial_spot', 19: 'Pepper,_bell___healthy',
                20: 'Potato___Early_blight', 21: 'Potato___Late_blight', 22: 'Potato___healthy', 23: 'Raspberry___healthy',
                24: 'Soybean___healthy', 25: 'Squash___Powdery_mildew', 26: 'Strawberry___Leaf_scorch', 27: 'Strawberry___healthy',
                28: 'Tomato___Bacterial_spot', 29: 'Tomato___Early_blight', 30: 'Tomato___Late_blight', 31: 'Tomato___Leaf_Mold',
                32: 'Tomato___Septoria_leaf_spot', 33: 'Tomato___Spider_mites Two-spotted_spider_mite', 34: 'Tomato___Target_Spot',
                35: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 36: 'Tomato___Tomato_mosaic_virus', 37: 'Tomato___healthy'}
        # model = tf.keras.models.load_model('my_general_model.hdf5')
        prediction_general('my_general_model.hdf5', class_dict, input_shape)

    if type_plant == 'Apple Plant':
        st.title(f"{type_plant} illness Classification Interface")
        class_dict = {0:'Apple___Apple_scab', 2:'Apple___Cedar_apple_rust',
                1:'Apple___Black_rot', 3:'Apple___healthy'}
        prediction_individual_plant('apple_cnn1.h5', class_dict, input_shape)

    elif type_plant == 'Grape Plant':
        st.title(f"{type_plant} illness Classification Interface")
        class_dict = {0:'Grape___Black_rot', 2:'Grape___healthy',
                1:'Grape___Esca_', 3:'Grape___Leaf_blight_'}
        prediction_individual_plant('grape_cnn1.h5', class_dict, input_shape)

    


if __name__ == '__main__':
    if st.session_state['home_page']:
        homepage()
    else:
        main()

