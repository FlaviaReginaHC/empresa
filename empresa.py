import streamlit as st

col1, col2, col3 = st.columns([1, 2, 3])

with col2:
  st.image("samsung-logo.png", width=300, link="https://www.samsung.com.br/")

st.title("NOME: Flávia Regina")

st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
  st.image("Panda-Vermelho.png", width=100)
  
with col2:
  st.header("Sobre Mim:")
  st.write("Olá")

st.image("whatsapp-logo.png", width=100, link="https://wa.me/+5583981821591")
