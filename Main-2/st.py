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
st.metric(label="Reverse",value=12345,delta='+10%',delta_color="inverse")
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
