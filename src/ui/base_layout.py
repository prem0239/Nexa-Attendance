import streamlit as st

def style_background_home():
    st.markdown("""
            <style>

                .stApp{
                    background: #DAF1DE !important;
                }           
                .stApp div[data-testid="stColumn"]{
                    background-color: #6da5c0 !important;
                    padding:1.5rem !important;
                    border-radius: 5rem !important;
                } 

            </style>    

            """
    ,unsafe_allow_html=True)




def style_background_dashboard():
    st.markdown("""
            <style>

                .stApp{
                    background: #8eb69b !important;
                }            

            </style>    

            """
    ,unsafe_allow_html=True)




def style_base_layout():
    st.markdown("""
            <style>

                    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&family=Sekuya&family=Titan+One&display=swap');
                    @import url('https://fonts.googleapis.com/css2?family=Chewy&display=swap');




                #MainMenu, footer, header{
                    visibility: hidden;}    

                .block-container{
                    padding-top: 1.5rem !important;
                    }
                h1{
                    font-family: 'Caveat', sans-serif !important;
                    font-size: 3rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                    color: #b51a2b !important;
                }

                h2{
                    font-family: 'Caveat', sans-serif !important;
                    font-weight: bold !important;
                    font-size: 3.5rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem !important;
                    color: #051f20!important;
                    }

                h3, h4, p{
                
                    font-family:'Chewy', sans-serif !important;
                    }


                    
                button{
                    border-radius: 1.5rem !important;
                    background-color: #a78d78 !important;
                    color: #49769f !important;
                    padding: 10px 20px !important;
                    border: none; !important;
                    transition: transform 0.25s ease-in-out !important;
                    }

                button[kind = "secondary"]{
                                    border-radius: 1.5rem !important;
                                    background-color: #ffa586 !important;
                                    color: #49769f !important;
                                    padding: 10px 20px !important;
                                    border: none; !important;
                                    transition: transform 0.25s ease-in-out !important;
                                    }
                                    
                button[kind = "tertiary"]{
                                    border-radius: 1.5rem !important;
                                    background-color: #a78d78 !important;
                                    color: #49769f !important;
                                    padding: 10px 20px !important;
                                    border: none; !important;
                                    transition: transform 0.25s ease-in-out !important;
                                    }
                button:hover{
                        transform:scale(1.05)
                }

            </style>    

            """
    ,unsafe_allow_html=True)