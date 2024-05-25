import streamlit as st  # pip install streamlit

st.header(":mailbox: we are here to cotact with You!")
st.write("Have a Question ? We're Here to Help!")
contact_form = """
<form action="https://formsubmit.co/longheist123@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit" class="button">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def main_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

main_css("main_css.css")
