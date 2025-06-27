import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  
import altair as alt

st.set_page_config(
    page_title =  "streamlit function demo",
    page_icon = "😁",
    layout = "centered" 

)

st.title("helllo world")

st.header("1. text element")
st.subheader("markdown,code,latek")
st.markdown("**bold text**,*italic text*,'code'text")
st.code("print('hello everyone')",language="python")
st.latex(r"a^2+b^2=c^2")



st.header("2. metrics and message")
st.metric(label="Reverse",value=12345,delta='+10%',delta_color="normal")
st.error("this is an error massage")
st.warning("this is a warning massage")
st.info("this is info masssage")
st.success("this is success masssage")
st.exception(ValueError("this is exception masssage"))

st.header("3. data display")
df=pd.DataFrame(np.random.randn(10,2),columns=["a","b"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict())




st.header("4. charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()



##file handling
##generator and decorter
##multithresding and multiprocessing
##method overloding and overriding 

st.header("6.widgets")
with st.form("input form"):
    name = st.text_input("Enter your name ")
    age = st.number_input("Enter your age")
    mood = st.radio("select your mood ",("Happy ","sad","neutral"))
    Language = st.multiselect("select your language ",("English","french","German"))
    submit = st.form_submit_button("submit")

if submit :
    st.success(f"Name : {name},Age : {int(age)},mood : {mood},Language  : {Language}")




col1 , col2 ,col3= st.columns([4,1,1])
with col1:
    st.text_input("Enter your name ")
    st.number_input("Enter your age")

with col2 :
    st.radio("select your mood ",("Happy ","sad","neutral"))
    st.multiselect("select your language ",("English","french","German"))
with col3:
    st.title("Output")





col1 , col2 , = st.columns(2)
with col1:
    number = st.slider("select a number ",0,100)
with col2 :
    colour = st.color_picker("select a color")

st.text_area("Enter your massage")
st.date_input("select a date")
st.time_input("select a time")
st.file_uploader("upload a file")

st.header("6.media")
st.image("https://picsum.photos/400",caption="random image")
st.video("https://youtube.com/shorts/D9bnByyydeQ?si=tyyc1RG0ucdcLOLg")
st.audio("https://youtube.com/shorts/D9bnByyydeQ?si=tyyc1RG0ucdcLOLg")

st.sidebar.header("sidebar header")
st.sidebar.write("this is a sidebar text")
st.sidebar.button("click me")

option = st.sidebar.selectbox("select an option ",("option 1","option 2"))

with st.container():
    st.write("this is a conatiner")

with st.expander("expender header"):
    st.write("this is a expender")

st.toast("toast meassage",icon="😁")

st.page_link("https://youtube.com/shorts/D9bnByyydeQ?si=tyyc1RG0ucdcLOLg",label = "youtube website",icon="😁")