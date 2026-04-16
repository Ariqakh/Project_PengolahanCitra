#PROGRAM PENGOLAHAN CITRA - CONVOLUTION (MASK PROCESSING)
#Anggota Kelompok : Ariqa Khairunnisa (2301020040) & Yunita Br Situmorang (2301020039)

import streamlit as st
import cv2, numpy as np
from PIL import Image
from io import BytesIO

st.set_page_config(page_title='Mask Processing', layout='centered')

st.markdown('''<style>
.main {background:#f6f8fb;}
.block-container{max-width:900px;padding-top:2rem;padding-bottom:2rem;}
.card{background:white;padding:22px;border-radius:18px;box-shadow:0 8px 24px rgba(0,0,0,.08);}
.small{color:#666;font-size:14px;}
</style>''', unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title('Program Convolution (Mask Processing)')

file = st.file_uploader('Upload Gambar', type=['jpg','jpeg','png'])

filters = [
    'Gambar Asli',
    'Box Filter',
    'Weighted Average Filter',
    'Gaussian Filter',
    'Median Filter',
    'Laplacian Filter',
    'High Boost Filter'
]

menu = st.radio('Pilih Filter', options=filters, index=0, horizontal=False)

if file:
    img = np.array(Image.open(file).convert('RGB'))
    hasil = img.copy()

    if menu == 'Box Filter':
        kernel = np.array([
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9]
        ], dtype=np.float32)
        hasil = cv2.filter2D(img,-1,kernel)
    elif menu == 'Weighted Average Filter':
        kernel = np.array([
            [1/16, 2/16, 1/16],
            [2/16, 4/16, 2/16],
            [1/16, 2/16, 1/16]
        ], dtype=np.float32)
        hasil = cv2.filter2D(img,-1,kernel)
    elif menu == 'Gaussian Filter':
        hasil = cv2.GaussianBlur(img,(3,3),0)
    elif menu == 'Median Filter':
        hasil = cv2.medianBlur(img,3)
    elif menu == 'Laplacian Filter':
        kernel = np.array([
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]
        ], dtype=np.float32)
        hasil = cv2.filter2D(img,-1,kernel)
    elif menu == 'High Boost Filter':
        A=1.5; w=(9*A)-1
        kernel = np.array([
            [-1, -1, -1],
            [-1,  w, -1],
            [-1, -1, -1]
        ], dtype=np.float32)
        hasil = cv2.filter2D(img,-1,kernel)

    c1,c2 = st.columns(2)
    with c1:
        st.subheader('Gambar Asli')
        st.image(img, use_container_width=True)
    with c2:
        st.subheader(menu)
        st.image(hasil, use_container_width=True)

    buf = BytesIO()
    Image.fromarray(hasil).save(buf, format='PNG')
    st.download_button('Download Hasil', data=buf.getvalue(), file_name='hasil_filter.png', mime='image/png')
else:
    st.info('Silakan upload gambar terlebih dahulu.')

st.markdown('</div>', unsafe_allow_html=True)
