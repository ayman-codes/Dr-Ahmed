from io import BytesIO
import requests
import streamlit as st
from PIL import Image

st.header('Certificates')
st.write('\n\n')
st.write('#')
cardiac_life_support = "https://i.ibb.co/9cVJCSQ/cardiac-life-support.png"
award = 'https://i.ibb.co/HxsR6wp/doctor-of-the-year.jpg'

response_pfp = requests.get(cardiac_life_support)
response_pfp_img = Image.open(BytesIO(response_pfp.content))

response_award = requests.get(award)
award_image = Image.open(BytesIO(response_award.content))


st.image(response_pfp_img)
st.write('''Cardiac life support provider certficate. Date of issue: 02/03/2020. [📄 Download PDF](https://github.com/ayman-codes/Dr-Ahmed/raw/main/assets/Diplomas/AHMAD%20AYMAN%20M.%20TAHER%20OBIDOU(1).pdf)''')

st.write('---')

st.image(response_pfp_img)
st.write('''This website is designed for Deep Learning course given by Dr.Mürsel Taşgin where I aim 
         to showcase all the related projects in the website Deep learning received a lot of success in many research
         areas from image processing to voice recognition. Nowadays, the knowledge in deep learning has become the number 
         one skill to deal with artificial intelligence related tasks. Our aim with this course is to make our students 
         earn the ability to deal with modern problems in machine learning.''')

st.write('---')

st.image(award_image)
st.write('''This website is designed for Deep Learning course given by Dr.Mürsel Taşgin where I aim 
         to showcase all the related projects in the website Deep learning received a lot of success in many research
         areas from image processing to voice recognition. Nowadays, the knowledge in deep learning has become the number 
         one skill to deal with artificial intelligence related tasks. Our aim with this course is to make our students 
         earn the ability to deal with modern problems in machine learning.''')

st.write('---')

st.image(pfp)
st.write('''This website is designed for Deep Learning course given by Dr.Mürsel Taşgin where I aim 
         to showcase all the related projects in the website Deep learning received a lot of success in many research
         areas from image processing to voice recognition. Nowadays, the knowledge in deep learning has become the number 
         one skill to deal with artificial intelligence related tasks. Our aim with this course is to make our students 
         earn the ability to deal with modern problems in machine learning.''')

st.write('---')

st.image(award_image)
st.write('''This website is designed for Deep Learning course given by Dr.Mürsel Taşgin where I aim 
         to showcase all the related projects in the website Deep learning received a lot of success in many research
         areas from image processing to voice recognition. Nowadays, the knowledge in deep learning has become the number 
         one skill to deal with artificial intelligence related tasks. Our aim with this course is to make our students 
         earn the ability to deal with modern problems in machine learning.''')

st.write('---')

st.image(pfp)
st.write('''This website is designed for Deep Learning course given by Dr.Mürsel Taşgin where I aim 
         to showcase all the related projects in the website Deep learning received a lot of success in many research
         areas from image processing to voice recognition. Nowadays, the knowledge in deep learning has become the number 
         one skill to deal with artificial intelligence related tasks. Our aim with this course is to make our students 
         earn the ability to deal with modern problems in machine learning.''')