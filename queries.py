from re import S
import sqlite3
import os
import pandas as pd
import bs4
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path= os.path.join(BASE_DIR, "git_repo.db")
connection = sqlite3.connect(db_path)



def get_most_starred():
    query = """
    SELECT *
    FROM repos
    ORDER BY stargazers DESC
    LIMIT 50
    """
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query, conn)
    return df
most_starred= get_most_starred()
print(most_starred)

def get_languages():
    query = """
    SELECT language, SUM(stargazers) AS total_stargazers, COUNT(name) AS number_of_repos
    FROM repos
    GROUP BY language
    ORDER BY total_stargazers DESC"""
    with sqlite3.connect(db_path) as conn:
       df =pd.read_sql_query(query,conn)
       return df 
languages = get_languages()
print(languages)

def get_most_forked():
    query = """
    SELECT name, link, forks
    FROM repos
    ORDER BY forks DESC"""
    with sqlite3.connect(db_path) as conn:
     df=pd.read_sql_query(query, conn)
     return df
most_forked = get_most_forked()
print(most_forked)

def get_most_issues():
    query = """
    SELECT name, forks, open_issues AS "open issues", created_on
    FROM repos
    ORDER BY "open issues" DESC
    LIMIT 50"""
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query,conn)
        return df
most_issues = get_most_issues()
print(most_issues)

def get_most_issues_corr():
    query = """
    SELECT name, forks, open_issues AS "open issues", created_on
    FROM repos
    ORDER BY "open issues" DESC
    LIMIT 100"""
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query,conn)
        return df
most_issues_corr = get_most_issues_corr()
print(most_issues_corr)