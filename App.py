import streamlit as st
import requests
from newsscrapper import scrapNdtv, scrapIndiatoday,scrapTimesofindia
  
st.markdown('<h1 style="text-align: center">News App</h1>', unsafe_allow_html=True)

sidebar = st.sidebar

sidebar.header("Choose a Website")
websites = ('Ndtv','Indiatoday','Timesofindia')
category= sidebar.radio('', websites)

sidebar.button('Enter')

if category == websites[0]:
    news1 = scrapNdtv()
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
    news1 = scrapTimesofindia()
    for newsrow1 in news1:
        col1,col2=st.columns([4, 10])
        #col2.write(newsrow1['heading'])
        col2.markdown(f'<h2> <a target ="_blank" href="https://timesofindia.indiatimes.com/news/ {newsrow1["link"]}">{newsrow1["heading"]}</a></h2> ', unsafe_allow_html=True)
        #col1.write(newsrow1['image'])
        #col1.markdown(f"![alt text]({newsrow1['image']})")
        col1.markdown(f'<h1><img src={newsrow1["image"]} style="width: 80%" /></h1>', unsafe_allow_html=True)
        col2.write(newsrow1['summary'])
        st.markdown("# ")




