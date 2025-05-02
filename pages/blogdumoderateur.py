import requests
from bs4 import BeautifulSoup


import streamlit as st


# requete vers le site blog du modérateur
response2 = requests.get("https://www.blogdumoderateur.com/")
# interpretation du site par beautifulsoup
soup = BeautifulSoup(response2.text)
# recuperation des articles dans la variable articles
articles = soup.find_all("article")


# boucle sur les articles

for article in articles:
    try:
        col1,col2 = st.columns(2)
        with col1:
            # catégorie de l'article
            st.text(article.find("span").text)
            
            # lien de l'image
            st.image(article.find("img").attrs["data-lazy-src"])
        with col2:
            # titre de l'article
            st.title(article.find("h3").text)
                
            # date de l'article
            st.text(article.find_all('span')[1].text)
            
            # lien de l'article
            st.link_button("voir l'article", article.find("a").attrs['href'])
    except:
        pass