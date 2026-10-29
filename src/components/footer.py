import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/0F7Z1kL/snap-class-logo.png"  # Replace with your logo URL

    st.markdown(f"""
        <div style="margin-top: 2rem; display: flex; gap:6px; justify-content: center; align-items: center;">
        <p style="font-weight: bold; color: white"> Created with ❤️ by </p>
        <img src='{logo_url}' alt="SnapClass logo" style="max-height: 25px"/>
        </div>
                """, unsafe_allow_html=True)

def footer_dashboard():
    logo_url = "https://i.ibb.co/0F7Z1kL/snap-class-logo.png"  # Replace with your logo URL

    st.markdown(f"""
        <div style="margin-top: 2rem; display: flex; gap:6px; justify-content: center; align-items: center;">
        <p style="font-weight: bold; color:black"> Created with ❤️ by </p>
        <img src='{logo_url}' alt="SnapClass logo" style="max-height: 25px"/>
        </div>
                """, unsafe_allow_html=True)