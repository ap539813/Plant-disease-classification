import streamlit as st

def homepage():
    # if st.session_state['home_page']:
    home_image = st.image("Plant disease classification.gif")

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

