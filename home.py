import streamlit as st

# titre
st.title('Python')

#text 

st.write('bonjour tout le monde !')

# User Input

user_input = st.text_input("tapez votre texte :")

st.write(user_input)
#colone
col1,col2 = st.columns(2)
#image video
with col1:
    st.image("https://imgs.search.brave.com/3i5QHAUElMCwVYjycHGjHMxYDQw1eTMW70davmzo93Q/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNS8w/OS8wNS8wNS8yNC9s/YW5kc2NhcGUtOTIz/NzY5XzY0MC5qcGc")
with col2:
    st.video("https://youtu.be/RWWbMz89QrU?si=GEyNrowgsjImmvGj")

pays =st.selectbox("selectionner un pays",["France","belgique","esapgne"])
st.write(pays)

st.sidebar.image("https://imgs.search.brave.com/3i5QHAUElMCwVYjycHGjHMxYDQw1eTMW70davmzo93Q/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNS8w/OS8wNS8wNS8yNC9s/YW5kc2NhcGUtOTIz/NzY5XzY0MC5qcGc")

