import streamlit as st


def footer_home():

    logo_url = "https://raw.githubusercontent.com/prem0239/Images/refs/heads/main/Footer_logo_.png"

    st.markdown(f"""
    <style>

        /* Remove Streamlit bottom spacing */
        .block-container {{
            padding-bottom: 0 !important;
        }}

        /* Remove bottom margin from Streamlit elements */
        .stApp {{
            margin-bottom: 0 !important;
            padding-bottom: 0 !important;
        }}

        /* Full-width footer */
        .custom-footer {{
            width: 100vw;
            margin-left: calc(50% - 50vw);
            margin-top: 50px;
            margin-bottom: 0 !important;
            padding: 0 !important;

            overflow: hidden;
        }}

        .custom-footer img {{
            width: 100%;
            height: 150px;

            display: block;
            margin: 0 !important;
            padding: 0 !important;

            object-fit: cover;
            object-position: center;
        }}

    </style>

    <div class="custom-footer">
        <img src="{logo_url}" alt="NexaAttend AI Footer">
    </div>

    """, unsafe_allow_html=True)




def footer_dashboard():

    logo_url = "https://raw.githubusercontent.com/prem0239/Images/refs/heads/main/Footer_logo_.png"

    st.markdown(f"""
    <style>

        /* Remove Streamlit bottom spacing */
        .block-container {{
            padding-bottom: 0 !important;
        }}

        /* Remove bottom margin from Streamlit elements */
        .stApp {{
            margin-bottom: 0 !important;
            padding-bottom: 0 !important;
        }}

        /* Full-width footer */
        .custom-footer {{
            width: 100vw;
            margin-left: calc(50% - 50vw);
            margin-top: 50px;
            margin-bottom: 0 !important;
            padding: 0 !important;

            overflow: hidden;
        }}

        .custom-footer img {{
            width: 100%;
            height: 150px;

            display: block;
            margin: 0 !important;
            padding: 0 !important;

            object-fit: cover;
            object-position: center;
        }}

    </style>

    <div class="custom-footer">
        <img src="{logo_url}" alt="NexaAttend AI Footer">
    </div>

    """, unsafe_allow_html=True)





    