CREATE DATABASE IF NOT EXISTS git_repo;

DROP TABLE IF EXISTS repos;
CREATE TABLE repos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    link TEXT NOT NULL,
    language TEXT,
    stargazers INT,
    forks INT,
    open_issues INT,
    created_on DATETIME
);