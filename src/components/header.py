import streamlit as st


def header_home():

    logo_url = "https://raw.githubusercontent.com/prem0239/delta-demo/refs/heads/main/logo2.png"
    

    st.markdown(f""" 
        <div style = "display: flex; flex-direction:column; align-items:center; justify-content:center: margin-bottm:30px margin-top: 30px">
            <img src= '{logo_url}' style = 'height: 250px;' />
            <h1 style ="text-align:center; color:#b51a2b ">Nexa Attend <br> An &nbsp; AI - Attendence System</h1>
        </div>

        """, unsafe_allow_html = True)



def header_dashboard():

    logo_url = "https://raw.githubusercontent.com/prem0239/delta-demo/refs/heads/main/logo2.png"
    

    st.markdown(f""" 
        <div style="display: flex; flex-direction: row; align-items:center; justify-content:center; gap:10px; width:100%;">
            <img src= '{logo_url}' style = 'height: 250px;' />
            <h2 style ='text-align:center; color:#b51a2b '>/* */</h2>
        </div>

        """, unsafe_allow_html = True)