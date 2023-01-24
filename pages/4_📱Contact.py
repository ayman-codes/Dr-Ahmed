import pathlib
import requests
import streamlit as st

st.header('Get in touch with me! ☎️ ')
st.write('##')

# LOAD CSS
css = 'https://raw.githubusercontent.com/ayman-codes/Dr-Ahmed/main/styles/main.css?token=GHSAT0AAAAAAB5ORJB4BMPALOMCLU22Y3Q2Y6P2AYA'
# --- LOAD CSS from github ---
response_css = requests.get(css)
st.markdown("<style>{}</style>".format(response_css), unsafe_allow_html=True)


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