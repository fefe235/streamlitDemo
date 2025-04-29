import streamlit as st

# titre
st.title("Titre")
st.code("st.title('str')")
st.title('str')
#text 
st.title("Texte")
st.code("st.write('str')")
st.write('str')
# User Input
st.title("Colone")
st.code("col1,col2 = st.columns(2)")
col3,col4 = st.columns(2)

with col3:
    st.code('''with col1:
        st.write('element1')''')
    st.write('element1')

with col4:
    st.code('''with col2:
        st.write('element2')''')
    st.write('element2')

#colone
#image video
st.title("Images")
st.code("st.image('lienVersImage',width=300)")
st.image("https://imgs.search.brave.com/3i5QHAUElMCwVYjycHGjHMxYDQw1eTMW70davmzo93Q/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNS8w/OS8wNS8wNS8yNC9s/YW5kc2NhcGUtOTIz/NzY5XzY0MC5qcGc",width=300)
st.title("Videos")
st.code("st.video('lienVersLaVideo')")
st.video("https://youtu.be/RWWbMz89QrU?si=GEyNrowgsjImmvGj")


st.title("sidebar")
st.code("st.sidebar.write('element')")
if st.checkbox("ajouter un element à la sidbar "):
    st.sidebar.write("element")

# Champ de saisie
st.title('Champ de saisie')
st.code('user_input = st.text_input("Quel est votre nom ?")')
user_input = st.text_input("Quel est votre nom ?")
st.code('st.write("user_input")')
st.write("user_input")

st.title("selectbox")
st.code('pays =st.selectbox("selectionner un pays",["France","belgique","esapgne"])')
pays =st.selectbox("selectionner un pays",["France","belgique","esapgne"])
st.code('st.write(pays)')
st.write(pays)

st.title('Bouton')
st.code('if st.button("Cliquer ici"): \n st.write("Bonjour " + user_input)')
if st.button("Cliquer ici"):
    st.write("Bonjour " + user_input)

st.title('Formulaire')
st.code('''with st.form("My form"):
    user_name = st.text_input("Quel est votre nom ?")

    age = st.slider("Quel est votre age", 18, 100, 35)

    if st.form_submit_button('Envoyer'):
        st.write("Bonjour " + user_name + 'tu as ' + str(age))''')

with st.form("My form"):
    user_name = st.text_input("Quel est votre nom ?")

    age = st.slider("Quel est votre age", 18, 100, 35)

    if st.form_submit_button('Envoyer'):
        st.write("Bonjour " + user_name + 'tu as ' + str(age))