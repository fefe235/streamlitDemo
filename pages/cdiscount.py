from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import streamlit as st


driver = webdriver.Chrome()
url = "https://www.cdiscount.com/"
driver.get(url)
sleep(2)
driver.find_element(By.ID,"footer_tc_privacy_button_2").click()
sleep(2)
with st.form("My form"):
    search = st.text_input("search")

    if (st.form_submit_button('Go')):
        driver.find_element(By.ID,"search").click()
        sleep(2)
        driver.find_element(By.ID,"search").send_keys(search+Keys.ENTER)
        sleep(2)
        articlesCdis=driver.find_elements(By.TAG_NAME, "article")

        col1,col2,col3 = st.columns(3)
        for article in articlesCdis:
            try:
                with col2:
                    st.text(article.find_element(By.TAG_NAME,"h4").text)
                    st.text(article.find_element(By.CLASS_NAME,"o-card__desc").text)
                with col1:
                    st.image(article.find_element(By.TAG_NAME,"img").get_attribute("src"))
                with col3:
                    st.title(article.find_element(By.CLASS_NAME,"c-price").text)
            except:
                    pass
    
driver.quit
