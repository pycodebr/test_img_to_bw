import io
import streamlit as st
from PIL import Image


def img_to_black_and_white(image):
    img = Image.open(image)
    return img.convert('L')

st.title('Conversor de imagens')

file = st.file_uploader(
    'Suba sua imagem aqui!',
    type=['jpg', 'png']
)

if file:
    if file.type == 'image/jpeg':
        img_bw = img_to_black_and_white(file)

        col_left, col_right = st.columns(2)

        with col_left:
            st.subheader('Imagem original')
            st.image(file)

        with col_right:
            st.subheader('Imagem preto e branco')
            st.image(img_bw)
            img_bytes = io.BytesIO()
            img_bw.save(img_bytes, format='JPEG')
            st.download_button(
                label='Baixar imagem preto e branco',
                file_name='img_bw.jpg',
                data=img_bytes,
            )
    else:
        st.error('Formato de arquivo não suportado!')
else:
    st.warning('Ainda não tenho arquivo!')
