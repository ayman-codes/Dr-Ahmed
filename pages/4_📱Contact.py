import pathlib
import streamlit as st
from pathlib import Path

st.header('Get in touch with me! ☎️ ')
st.write('##')

# LOAD CSS
current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = 'C:/Users/ayman/OneDrive/Coding-New/Coding/WORKSPACE/PYTHON/Dr-Ahmed/Dr-Ahmed/styles/main.css'
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# contact
contact_form = '''
<form action="https://formsubmit.co/ahmadabido2010@hotmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Insert your name" required>
    <input type="email" name="email" placeholder="Insert your email" required>
    <textarea name="message" placeholder="Insert your message" required></textarea>
    <button type="submit">Send</button>  
</form>
'''

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty(
    )