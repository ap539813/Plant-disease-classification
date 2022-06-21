import altair as alt
import streamlit as st
import seaborn as sns

# importing the local modules
from important_variables import input_shape, data_url
from prediction import prediction
from homepage import homepage

from PIL import Image


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

print(st.session_state)

if 'home_page' not in st.session_state:
    st.session_state['home_page'] = True

def homepage():
    # if st.session_state['home_page']:
    # home_image = st.image("Plant disease classification.gif")

    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)

    c1, c2, c3 = st.columns([1,3,1])
    # col2.radio(
    #         "Mode of Operation",
    #         ("Search", "Configure"),
    #     )

    c2.markdown('<div style="text-align: center;"> <h2> Select mode of operation </h2></div>', unsafe_allow_html=True)
    # col2.markdown('<div style="text-align: center;">Hello World!</div>', unsafe_allow_html=True)


    search_page = c2.button('Search')
    config_page = c2.button('Configure')

    st.session_state['home_page'] = False
    # print(search_page)
    

    if search_page:
        print('going for search!!')
        st.session_state['mode'] = 'Search'
        home_image.empty()
        main()
    if config_page:
        print('going for configuration!!')
        st.session_state['mode'] = 'Config'
        home_image.empty()
        main()

def main():
    st.sidebar.title("Control Panel")
    left_col, middle_col, right_col = st.columns(3)
    palette = sns.color_palette("bright")

    tick_size = 12
    axis_title_size = 16



    # data = generate_data()
    type_plant = st.sidebar.radio("Select Type of Plant: ", ('General Disease Detection', 'Apple Plant',
                                'Grape Plant'))

    if type_plant == 'General Disease Detection':
        st.markdown("# Under Development!!!")
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


if __name__ == '__main__':
    if st.session_state['home_page']:
        homepage()
    else:
        main()

