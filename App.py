import streamlit as st
import requests
from newsscrapper import scrapNDTV, scrapIndiatoday
  
st.markdown('<h1 style="text-align: center">News App</h1>', unsafe_allow_html=True)
sidebar = st.sidebar

sidebar.header("Choose a Website")
websites = ('ndtv.com','indiatoday.com')
category= sidebar.radio('', websites)

sidebar.button('Enter')

if category == websites[0]:
    news1 = scrapNDTV()
    for newsrow in news1:
        col1,col2=st.columns([4, 10])
        col2.markdown(f' <h2> <a target="_blank" href="{newsrow["link"]}">{newsrow["heading"]}</a></h2> ', unsafe_allow_html=True)
        col1.markdown(f'<img src={newsrow["image"]} style="width: 90%" />', unsafe_allow_html=True)
        col2.write(newsrow['summary'])
        st.markdown("# ")
       

elif category == websites[1]:
    news1 = scrapIndiatoday()
    for newsrow in news1:
        col1,col2=st.columns([4, 10])
        col2.markdown(f' <h2> <a target="_blank" href="https://www.indiatoday.in/{newsrow["link"]}">{newsrow["heading"]}</a></h2> ', unsafe_allow_html=True)
        col1.markdown(f"![alt text]({newsrow['image']})")
        #col1.markdown(f'<img src={newsrow["image"]} style="width: 50%" />', unsafe_allow_html=True)
        col2.write(newsrow['summary'])
        st.markdown("# ")

elif category == websites[2]:
    news1 = scrapNews18()
    for newsrow in news1:
        col1,col2=st.columns([4, 10])
        col2.write(newsrow['heading'])
        #col1.markdown(f"![alt text]({newsrow['image']})")
        col2.write(newsrow['summary'])
        #st.markdown("# ")


       
