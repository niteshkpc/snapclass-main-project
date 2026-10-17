import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import  style_base_layout, style_background_home
from src.components.footer import footer_home

def home_screen():
    #st.header("Home Screen")   Not needed as we have a header component

    style_base_layout()
    style_background_home()
    
    header_home()
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            "<h2 style='color: black;'>I'm Student</h2>",
            unsafe_allow_html=True
        )
        st.image("https://i.ibb.co/0F7Z1kL/snap-class-logo.png", width=120)
        if st.button("Student Portal", type="primary", icon=":material/arrow_outward:", icon_position="right"):
            st.session_state['login_type'] = 'student'
            st.rerun()
    with col2:
        st.markdown(
            "<h2 style='color: black;'>I'm Teacher</h2>",
            unsafe_allow_html=True
        )
        st.image("https://i.ibb.co/0F7Z1kL/snap-class-logo.png", width=120)
        if st.button("Teacher Portal", type="primary", icon=":material/arrow_outward:", icon_position="right"):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

            
    footer_home()  # Call the footer function to display the footer at the bottom of the page