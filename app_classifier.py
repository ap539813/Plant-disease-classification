import altair as alt
import streamlit as st
import seaborn as sns

# importing the local modules
from important_variables import input_shape, data_url, css_file_path
from prediction import prediction
from add_style import local_css

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

