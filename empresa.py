import streamlit as st

col1, col2, col3 = st.columns([1, 2, 3])

with col2:
  st.image("samsung-logo.png", width=300, link="https://www.samsung.com.br/")

st.title("Nome: Flávia Regina")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
  st.image("Panda-Vermelho.png", width=300)
  
with col2:
  st.header("Sobre Mim:")
  st.write("Olá! Eu sou Flávia e não sou formada em nada.")

st.write("")
  
st.link_button("Acessar Site", "https://sites.google.com/academico.ifpb.edu.br/flaviaregina/in%C3%ADcio")

col1, col2, col3 = st.columns([1, 2, 3])

st.markdown("<br>", unsafe_allow_html=True)

with col2:
  st.image("whatsapp-logo.png", width=100, link="https://wa.me/+5583981821591")
