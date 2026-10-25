#Dependencies
import sqlite3
import os
import pandas as pd
#est. Connection
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path= os.path.join(BASE_DIR, "git_repo.db")
connection = sqlite3.connect(db_path)

def get_avg_stars():
    query = """
    SELECT language, AVG(stargazers) AS avg_stargazers, AVG(forks) AS Avg_forks
    FROM repos
    WHERE language NOT NULL
    GROUP BY language
    ORDER BY avg_stargazers DESC"""

    with sqlite3.connect(db_path) as conn:
        df =pd.read_sql_query(query,conn)
        return df 
avg_stars = get_avg_stars()
#print(avg_stars)

def age_vs_stars():
    query = """
    SELECT name, stargazers, forks
    FROM repos
    WHERE Created_on >= "2020-01-01"
    ORDER BY stargazers DESC"""

    with sqlite3.connect(db_path) as conn:
        df =pd.read_sql_query(query,conn)
        return df 
repo_age_stars = age_vs_stars()
print(repo_age_stars)

def repo_type_pop():
    query = """
    SELECT project_type, AVG(stargazers) AS avg_stargazers
    FROM repos
    GROUP BY project_type
    ORDER BY stargazers DESC"""

    with sqlite3.connect(db_path) as conn:
        df =pd.read_sql_query(query,conn)
        return df 
repo_type = repo_type_pop()
print(repo_type)

def repo_description():
    query = """
    SELECT name, stargazers, Created_on, project_type
    FROM repos
    WHERE description LIKE '%ai%'
        OR description LIKE '%artificial intelligence%'
        OR description LIKE '%llm%'
        OR description LIKE '%language model%'
        OR description LIKE '%neural network%'
    ORDER BY Created_on DESC"""

    with sqlite3.connect(db_path) as conn:
        df =pd.read_sql_query(query,conn)
        return df 
desc_corr = repo_description()
print(desc_corr)