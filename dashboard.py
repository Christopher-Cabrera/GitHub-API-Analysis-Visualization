import os
import sqlite3
import pandas as pd
import streamlit as st
import requests
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db", "git_repo.db")

from queries import get_most_starred
st.title("Favorite Git Repos")
df1= get_most_starred()
df1_sorted = df1.sort_values(by="stargazers", ascending= True)
st.bar_chart(data = df1_sorted, x="name", y="stargazers", sort= False)

from queries import get_languages
st.title("Favorite Git Repo Languages")
df2 = get_languages()
df2_sorted = df2.sort_values(by="total_stargazers", ascending=True)
st.bar_chart(data=df2_sorted,x="language", y="total_stargazers", sort=False)

from queries import get_most_issues
st.title("Most Problematic Git Repos")
df3 = get_most_issues()
fig = px.bar(df3, x="name", y= "open issues", hover_data=["forks"], title="Most Problematic Git Repos")
st.plotly_chart(fig, use_container_width=True)

df4 = get_most_issues()
fig = px.scatter(df4, x="forks", y="open issues", size="forks", color="open issues", hover_name="name", title= "Correlation between Forks and Open Issues on GitHub")
st.plotly_chart(fig, use_container_width=True)

df5 = get_most_issues()
df5["created_on"]= pd.to_datetime(df5["created_on"])
fig = px.scatter(df5, x="created_on", y="open issues", color="forks", size="open issues", hover_name="name", title= "Correlation between Repo age and forks on Open Issues on GitHub")
st.plotly_chart(fig, use_container_width=True)

df6 = get_most_starred()
df6["created_on"]= pd.to_datetime(df6["created_on"])
fig = px.scatter(df6, x="created_on", y="stargazers", hover_data="name", title="Correlation between Repo age and Stargazers")
st.plotly_chart(fig, width="stretch")