import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator", page_icon="🔐")

st.title("🔐 Password Generator")
st.write("Generate strong and secure passwords instantly.")

# User inputs
length = st.slider("Password Length", min_value=4, max_value=50, value=12)
use_upper = st.checkbox("Include Uppercase Letters", value=True)
use_lower = st.checkbox("Include Lowercase Letters", value=True)
use_digits = st.checkbox("Include Numbers", value=True)
use_symbols = st.checkbox("Include Symbols", value=True)

# Generate password
def generate_password(length, upper, lower, digits, symbols):
    characters = ''
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if st.button("Generate Password"):
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    st.code(password)
