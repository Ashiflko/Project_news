import streamlit as st
import requests
from newsscrapper import scrapNDTV, scrapIndiatoday, scrapTimes

st.title(' News App')


websites = ('ndtv','indiatoday','TimesNews')
category= st.radio('choose website', websites)

btn=st.button('Enter')

if btn:
    if category == websites[0]:
        news1 = scrapNDTV()
        col1,col2=st.columns(2)
        for newsrow in news1:
            col1.write(newsrow['heading'])
            col1.markdown(f"![alt text]({newsrow['image']})")
            
            col1.write(newsrow['summary'])
            #col2.write(newsrow['image'])

    elif category == websites[1]:
        news1 = scrapIndiatoday()
        col1,col2=st.columns(2)
        for newsrow in news1:
            col1.markdown(f"![alt text]({newsrow['image']})")
            col2.write(newsrow['heading'])
            col2.write(newsrow['summary'])
            #col2.write(newsrow['image'])


    elif category == websites[2]:
         news1 = scrapTimes()
         col1,col2=st.columns(2)
         for newsrow in news1:
            col1.markdown(f"![alt text]({newsrow['image']})")
            col2.write(newsrow['heading'])
            col2.write(newsrow['summary'])

       

