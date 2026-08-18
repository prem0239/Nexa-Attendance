import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_home
from src.components.footer import footer_home

def home_screen():

    header_home()
    style_base_layout()
    style_background_home()


    col1, col2 = st.columns(2, gap='large')

    with col1:
        st.header("I'm Student")
        st.image('src\screens\Student_logo.png')
        if st.button('Student Portal',icon=':material/arrow_outward:'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        st.image("src\\screens\\Teacher_logo.png" )
        if st.button('Teacher Portal', icon=':material/arrow_outward:'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    


    footer_home()