from io import BytesIO
from pathlib import Path
import requests
import streamlit as st
from PIL import Image

# Path settings
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles'/'main.css'
pfp = "https://drive.google.com/file/d/13RchdS1B-dt5HYHdGgUb5eep4HG7fXUO/view?usp=sharing"
resume_file = 'https://github.com/ayman-codes/Dr-Ahmed/raw/main/assets/CV/cv3b.pdf'

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Dr. Ahmed Ayman Obidou"
PAGE_ICON = "👋"
NAME = "Dr. Ahmed Ayman Obidou"
DESCRIPTION = """
Family doctor specialist, 17 years experience in family medicine and Medical director.
"""
EMAIL = "ahmadabido2010@hotmail.com"
SOCIAL_MEDIA = {
    "LinkedIn ": "https://www.linkedin.com/in/ahmadayman-abido-91a647211",
    "Instagram": "https://instagram.com/ahmadaymanabido?igshid=OGQ2MjdiOTE=",
}
CERTIFICATES = {
    "🏆 Bachelor degree - General Medicine from university of Algeria": "https://drive.google.com/file/d/1jthRRq2Q35I-ZB2i_z6D0iW0Ro98YKtd/view?usp=sharing",
    "🏆 Specialist in Family medicine - Syria helth ministry": "https://drive.google.com/file/d/1cK3umw56itI3EBs7XWr1CoipwdR-qWzV/view?usp=sharing",
    "🏆 Basic cardiac life support - Saudi Heart Assosiation": "https://drive.google.com/file/d/1oVPqq8NHWDG3VjC5WEuGXdIceNZrnLFy/view?usp=sharing",
    "🏆 Awards - Saudi Minisry of health": "https://drive.google.com/file/d/1ttnwfALyv5sp_-_ZVCFcoVGEvY30lHru/view?usp=sharing",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.sidebar.success("Navigation menu")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


response = requests.get(pfp)
pfp2 = Image.open(BytesIO(response.content))

    
response2 = requests.get(resume_file)
#pfp2 = Image.open(BytesIO(response.content))
PDFbyte = response2.read()


# hero section
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(pfp2, width=280)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# About me
st.write('#')
st.subheader('About me')
st.write(
    '''
    I'm a highly experienced and dedicated family doctor from Egypt. I have a bachelor's degree in 
    Medicine from Algeria and a specialist degree in Family Medicine from Syria.
    I can speak French, Arabic, and English, and have over 17 years of experience working in the medical 
    field - both as a Medical Director and Family Doctor. I'm well-versed in providing patient centered care
    and has implemented quality improvement initiatives to improve patient access to care.
    I've experience in leading projects to improve patient access to care and providing health 
    education and counseling to patients and families. I'm committed to providing the highest quality 
    of care to my patients. I'm passionate about my work, as it allows to help more people and give people
    the medical care that they need. I'm constantly striving to be a better version of myself.
    '''
)

# Experience
st.write('#')
st.subheader('Experience in Family Medicine')
st.write(
    '''
    - Delivered quality, patient-centered primary care 
    - Supervised medical staff, conducted performance reviews 
    - Developed and implemented quality improvement initiatives 
    - Researched and presented best practices to staff 
    - Coordinated patient care with specialists, hospitals, and community resources 
    - Led projects to improve patient access to care 
    - Provided health education and counseling to patients and families 
    - Conducted physical exams, diagnosis and treatments.

    '''
)

# Experience
st.write('#')
st.subheader('Experience as a Medical director')
st.write(
    '''
    - ✔️ Oversee operations, staff, and patient care 
    - ✔️ Develop and implement best practices for operations and patient care 
    - ✔️ Serve as primary contact, communication, and decision-maker for staff, patients, and community
    '''
)

# --- Projects & Accomplishments ---
st.write('\n\n\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in CERTIFICATES.items():
    st.write(f"[{project}]({link})")