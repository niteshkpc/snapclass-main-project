import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)

    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }


            /* Default text color */
            .stApp {
                color: black;
            }

            /* Keep text white inside black-background boxes */
            .stApp div[style*="background-color: black"] p,
            .stApp div[style*="background-color: black"] span,
            .stApp div[style*="background: black"] p,
            .stApp div[style*="background: black"] span {
                color: white !important;
            }

            /* Input text */
            .stApp input,
            .stApp textarea {
                color: white !important;
            }

            
            /* Make input labels black */
            .stApp div[data-testid="stTextInput"] label,
            .stApp div[data-testid="stTextInput"] label p {
                color: black !important;
            }


            /* Input placeholder */
            .stApp input::placeholder,
            .stApp textarea::placeholder {
                color: #555555 !important;
            }

            /* Keep button text white */
            .stApp button {
                color: white !important;
            }

            /* Selectbox label color */
            .stApp div[data-testid="stSelectbox"] label,
            .stApp div[data-testid="stSelectbox"] label p {
                color: black !important;
            } 

            /* Camera input label - black */
            .stApp div[data-testid="stCameraInput"] label,
            .stApp div[data-testid="stCameraInput"] label p {
                color: black !important;
            }  

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)

