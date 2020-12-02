 ![Python 3.7](https://img.shields.io/badge/Python-3.7-brightgreen.svg) ![library](https://img.shields.io/badge/Library-numpy-orange.svg) ![library](https://img.shields.io/badge/Library-matplotlib-blueviolet.svg) ![library](https://img.shields.io/badge/Library-seaborn-9cf.svg)

## What is EDA?

- Exploratory data analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often with visual methods. 

- It is good practice to understand the data first and try to gather as many insights from it. 

# NBA Dataset Project

The primary goal of the project is to go through the dataset and the general data analysis process using numpy, pandas and matplotlib. 

Data is extracted from https://www.basketball-reference.com/leagues/NBA_2019_per_game.html

## Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, matplotlib, seaborn.

## Data Wrangling
After Observing the dataset and the questions related to this dataset for the analysis we will be keeping only relevent data and deleting the unused data.

- We need to remove duplicate rows from the dataset
- Changing format of release date into datetime format
- Remove the unused colums that are not needed in the analysis process.
- Remove the movies which are having zero value of budget and revenue.

### By doing EDA we can answer below questions

### Questions

Q1.1) Which player scored the most Points (PTS) Per Game?

Q1.2) what team is the player from?

Q1.3) Which position is the player playing as?

Q2) Which player scored more than 20 Points (PTS) Per Game?

Q3) Which player had the highest 3-Point Field Goals Per Game (3P) ?

Q4) Which player had the highest Assists Per Game (AST) ?

Q5) Which player scored the highest (PTS) in the Los Angeles Lakers?

Q6) which position scores the most points?


## Exploratory Data Analysis
 Some of the insight gained from analysis of the data..
 
 <p float="left" align='center'>
 
 <img src = "https://github.com/diwakarDrs/EDA/blob/main/NBA_Sports/Readme/pos.PNG" width = 500 alt="position">
 
 <img src = "https://github.com/diwakarDrs/EDA/blob/main/NBA_Sports/Readme/hm.PNG" width = 300 alt="heatmap">
  
 </p>
 
