 ![Python 3.7](https://img.shields.io/badge/Python-3.7-brightgreen.svg) ![library](https://img.shields.io/badge/Library-numpy-orange.svg) ![library](https://img.shields.io/badge/Library-matplotlib-blueviolet.svg) ![library](https://img.shields.io/badge/Library-seaborn-9cf.svg)

## What is EDA?

- Exploratory data analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often with visual methods. 

- It is good practice to understand the data first and try to gather as many insights from it. 

# TMDB Movie Dataset Project

The primary goal of the project is to go through the dataset and the general data analysis process using numpy, pandas and matplotlib. This contain four parts:

# Table of Contents
- [Introduction](#introduction)
- [Resources Used](#resources-used)
- [Data Wrangling](#data-wrangling)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Conclusions](#conclusions)

## Introduction
I choose the TMDb movie data set (1960-2015)downloaded from kaggle for data analysis. This data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue.I would like to find other interesting patterns in the dataset.

*Contain:*
- Total Rows = 10866
- Total Columns = 21
- After Seeing the dataset we can say that some columns is contain null values.

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
1. Which year has the highest release of movies?
2. Which Movie Has The Highest Or Lowest Profit? Top 10 movies which earn highest profit?
3. Movie with Highest And Lowest Budget?
4. Which movie made the highest revenue and lowest as well?
5. Movie with shorest and longest runtime?
6. Which movie get the highest or lowest votes (Ratings).
7. Which Year Has The Highest Profit Rate?
8. Which length movies most liked by the audiences according to their popularity?
9. Average Runtime Of Movies From Year To Year?
10. How Does The Revenue And Popularity differs Budget And Runtime? And How Does Popularity Depends On Profit?
11. Which Month Released Highest Number Of Movies In All Of The Years? And Which Month Made The Highest Average Revenue?
12. Which Genre Has The Highest Release Of Movies?
13. Most Frequent star cast?
14. Top 20 Production Companies With Higher Number Of Release?
15. Top 20 Director Who Directs Maximum Movies?
16. What kinds of properties are associated with movies that have high revenues?


## Exploratory Data Analysis
 Some of the insight gained from analysis of the data..
 
 <p float="left" align='center'>
 
 <img src = "https://github.com/diwakarDrs/EDA/blob/main/Movie_TMDB/Readme_resources/release.PNG" width = 300 alt="Movie_release">
 
 <img src = "https://github.com/diwakarDrs/EDA/blob/main/Movie_TMDB/Readme_resources/profit.PNG" width = 500 alt="Profit">
  
 </p>
 
  <p float="left">
 
 <img src = "https://github.com/diwakarDrs/EDA/blob/main/Movie_TMDB/Readme_resources/actor.PNG" width = 400 alt="Actor">
 
 <img src = "https://github.com/diwakarDrs/EDA/blob/main/Movie_TMDB/Readme_resources/buget.PNG" width = 500 alt="Budget">
  
 </p>
 
  <p float="left">
 
 <img src = "https://github.com/diwakarDrs/EDA/blob/main/Movie_TMDB/Readme_resources/genre.PNG" width = 450 alt="Genre">
 
 <img src = "https://github.com/diwakarDrs/EDA/blob/main/Movie_TMDB/Readme_resources/prod_comp.PNG" width = 450 alt="Production Companies">
  
 </p>

 <p align="center"><img src = "https://github.com/diwakarDrs/EDA/blob/main/Movie_TMDB/Readme_resources/corr.PNG" width = 450 alt="correlation"><p>
 
 **Plot 1: Budget vs Revenue**

The revenues do increase slightly at higher levels but the number of movies with high budgets seem scarce. There is a good possibility that movies with higher investments result in better revenues.
- Correlation = 0.69

I can't find a relationship here. The revenues don't seem to change with higher vote average.

**Plot 2: Popularity vs Revenue**

The revenue seems to be increasing with popularity. We can say that if the popularity of movie is high then the revenue of the movie may be high.
- Correlation = 0.63

**Plot 3: Vote Average vs Revenue**

The correlation between revenue and vote average is **0.21**. So vote average is not highly related to the revenue.

**Plot 4: Runtime vs Revenue**

The correlation between revenue and runtime is **0.24**. So runtime is not highly related to the revenue.


## Conclusions
- Maximum Number Of Movies Release In year 2014.
- 'Avatar', 'Star Wars' and 'Titanic' are the most profitable movies.
- Short or Long duration movies are more popular than long duration movies.
- Average runtime of the movies are decreasing year by year.
- May,June,November and December are most popular month for releasing movies, if you want to earn more profit.
- Revenue is directly connected to the budget.
- Warner Bros, Universal Pictures and Paramount Pictures production companies earn more life time profit than other production companies.
- Movies with higher budgets have shown a corresponding increase in the revenues.
