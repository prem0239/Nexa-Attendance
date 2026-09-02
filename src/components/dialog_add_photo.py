import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time
from PIL import Image


@st.dialog("Capture or upload photos")
def add_photos_dialog():

    st.write('Add classroom photos to scan for attendance')

    if 'photo_tab' not in  st.session_state:
        st.session_state.photo_tab = 'camera'
    if 'photo_widget_gen' not in st.session_state:
        st.session_state.photo_widget_gen = 0

    t1,t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'tertiary'
        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'


    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('Upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Snapshot', key=f"dialog_cam_{st.session_state.photo_widget_gen}")


        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.session_state.photo_widget_gen += 1
            st.toast('Photo Captured ')
            st.rerun()

    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader('Choose image files', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key=f"dialog_upload_{st.session_state.photo_widget_gen}")

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.session_state.photo_widget_gen += 1
            st.toast('Photo Uploaded successfully')
            st.rerun()

    if st.session_state.attendance_images:
        st.divider()
        st.caption(f"{len(st.session_state.attendance_images)} photo(s) added")
        cols = st.columns(4)
        for i, img in enumerate(st.session_state.attendance_images):
            with cols[i % 4]:
                st.image(img, width='stretch')

    st.divider()
    if st.button('Done', type='primary', width='stretch'):
        st.rerun()