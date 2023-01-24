from io import BytesIO
import requests
import streamlit as st
from PIL import Image

st.header('Certificates')
st.write('\n\n')
st.write('#')
cardiac_life_support = "https://i.ibb.co/9cVJCSQ/cardiac-life-support.png"
shield_of_honour = "https://i.ibb.co/dm0cYsv/shield-of-honour.png"
years_award = 'https://i.ibb.co/VMC8tpL/15years-award.png'
master_degree = 'https://i.ibb.co/xJ5X9hW/master-degree.png'
naaim_award = 'https://i.ibb.co/3m9HLvw/na3im-culture-certificate.jpg'
bahchelor_degree = 'https://i.ibb.co/HpJxTLL/Bahchelor-degree.png'

response_cardiac = requests.get(cardiac_life_support)
cardiac_img = Image.open(BytesIO(response_cardiac.content))

response_shield = requests.get(shield_of_honour)
shield_image = Image.open(BytesIO(response_shield.content))

response_15year = requests.get(years_award)
years_award_image = Image.open(BytesIO(response_15year.content))

response_master = requests.get(master_degree)
master_degreee_img = Image.open(BytesIO(response_master.content))

response_naaim = requests.get(naaim_award)
naaim_img = Image.open(BytesIO(response_naaim.content))

response_bahchelor_degree = requests.get(bahchelor_degree)
bahchelor_img = Image.open(BytesIO(response_bahchelor_degree.content))



st.image(bahchelor_img)
st.write('''Bahchelor degree in general medicine from the university of Algeria. Date of issue: 12/01/1991. 
         \n[📄 Download PDF](https://github.com/ayman-codes/Dr-Ahmed/raw/main/assets/Diplomas/%D8%B4%D9%87%D8%A7%D8%AF%D8%A9%20%D8%A7%D9%84%D8%B7%D8%A8%20%D8%A7%D9%84%D8%B9%D8%A7%D9%85%20%D8%AE%D9%84%D9%81.pdf)''')

st.write('---')

st.image(master_degreee_img)
st.write('''My master's degree from Syria. Date of issue: 22/11/2000. 
         \n[📄 Download PDF](https://github.com/ayman-codes/Dr-Ahmed/raw/main/assets/Diplomas/master%20certificate.pdf)''')

st.write('---')

st.image(cardiac_img)
st.write('''Cardiac life support provider certficate. Date of issue: 02/03/2020. [📄 Download PDF](https://github.com/ayman-codes/Dr-Ahmed/raw/main/assets/Diplomas/AHMAD%20AYMAN%20M.%20TAHER%20OBIDOU(1).pdf)''')

st.write('---')

st.image(shield_image)
st.write('''Commemorative shield in appreciation and pride for his extreme care of patients and auditors, and his keenness in accurate examination and presciribing
         the appropriate treatment for each case.  
         \n\n[📄 Download PDF](https://github.com/ayman-codes/Dr-Ahmed/raw/main/assets/Diplomas/Shield_of_honor.pdf)''')

st.write('---')

st.image(years_award_image)
st.write('''Award for proffieciency and good dealings with the residents if the neighborhood affiliated with the committee during the 15 years he spent in 
         healthy neighborhoods affiliated with the comittee 
         \n[📄 Download PDF](https://github.com/ayman-codes/Dr-Ahmed/raw/main/assets/Diplomas/15years%20award.pdf)''')

st.write('---')

st.image(naaim_img)
st.write('''From Naa'im cultral organization in Al-hassa: we're pleased to award the family Doctor in Mualimeen clinic Dr.Ahmed Ayman Obidou a commemorative shield
         in appreciation and pride for his lectures on: 'Diabetes and it's complications' 08/02/2016.  
         \n[📄 Download JPEG](https://github.com/ayman-codes/Dr-Ahmed/raw/main/assets/Diplomas/na3im_culture_certificate.jpeg)''')