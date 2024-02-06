# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:53:31 2024
@author: HazelhurstLT
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#url="https://canvas.instructure.com/courses/7413444/files/222041863/download?download_frd=1"
#df=pd.read_csv(url)
#Dataset is in GitHub repositroy.
df=pd.read_csv("movie_dataset.csv")

df.rename(columns={"Runtime (Minutes)":"Runtime(minutes)"},inplace=True)
df.rename(columns={"Revenue (Millions)":"Revenue(millions)"},inplace=True)

df_dup=df.duplicated()

print(f"This is the orginal dataset summary with no duplicates\n{df.info()}")
print("\n\n")

nan_indices = df.isna()
mean_rev=df["Revenue(millions)"].mean()
mean_meta=df["Metascore"].mean()
#mean=df[["Revenue(millions)","Metascore"]].mean()
df["Revenue(millions)"].fillna(value=mean_rev, inplace=True)
df["Metascore"].fillna(value=mean_meta, inplace=True)
print(f"This is the dataset summary with Null values replaced with the mean\n{df.info()}")
print("\n\n")

print("Q1 What is the highest rated movie in the dataset?")
high_rate_all=df["Rating"].max()
high_movie=df.loc[df["Rating"]==(high_rate_all),"Title"]
#Convert title to string
print(f"The highest rated movie is {list(high_movie)} with a score of {high_rate_all}.")
print("\n")

print("Q2 What is the average revenue of all movies in the dataset?")
# Note, since the answer will be effected by how you dealt with missing values a range has been provided.
avg_revenue=int(df["Revenue(millions)"].mean())
print(f"The average revenue for all movies is {avg_revenue} million.")
print("\n")

print("Q3 What is the average revenue of movies from 2015 to 2017 in the dataset?")
# Note, since the answer will be effected by how you dealt with missing values a range has been provided. 
#Filter 2015-2017
years=(2015,2016,2017)
y15_17_df=df[df["Year"].isin(years)]
avgrevenue15_17=int(y15_17_df["Revenue(millions)"].mean())
print(f"The average revenue for movies from 2015 to 2017 was {avgrevenue15_17} million.")
print("\n")
     
print("Q4 How many movies were released in the year 2016?")
y2016_df=df[(df["Year"]==2016)]
movies16=y2016_df["Year"].count()
print(f"The number of movies release in 2016 was {movies16}.")
print("\n")

print("Q5 How many movies were directed by Christopher Nolan?")
chris_nol_df=df[(df["Director"]=="Christopher Nolan")]
count_chris_nol_df=chris_nol_df["Director"].count()
print(f"The total number of movies directed by Christopher Nolan was {count_chris_nol_df}.")
print("\n")

print("Q6 How many movies in the dataset have a rating of at least 8.0?")
rate8_df=df[(df["Rating"]>=8.0)]
rate8count=rate8_df["Rating"].count()
print(f"The number of movies that have a rating of at least 8.0 is {rate8count}.")
print("\n")

print("Q7 What is the median rating of movies directed by Christopher Nolan?")
chris_nol_df=df[(df["Director"]=="Christopher Nolan")]
rate_chris_nol_df=chris_nol_df["Rating"].median()
print(f"The median rating for Christopher Nolan movies is {rate_chris_nol_df}.")
print("\n")

print("Q8 Find the year with the highest average rating?")
year_group_rate_mean=df.groupby(["Year"])["Rating"].mean().round(decimals=3)
year_max=year_group_rate_mean.max()


list(year_group_rate_mean.items())
for index, value in year_group_rate_mean.items():
    print(f"Index:{index},Value:{value}")

year_mean_df=pd.DataFrame(year_group_rate_mean)
rate_max_df=year_mean_df.loc[year_mean_df["Rating"]==year_max]
year_high="xxxx"
#I struggled to index into the year with the best mean.
print(f"The year with the highest rating is {year_high} with an average of {year_max}")
print("\n")

print("Q9 What is the percentage increase in number of movies made between 2006 and 2016?")
year_group_num_count=df.groupby(["Year"])["Rank"].count()
y2006=int(year_group_num_count.iloc[0])
y2016=int(year_group_num_count.iloc[-1])
per_incr=int(((y2016-y2006)/y2006)*100)
print(f"The precentage increase in movies from 2006 to 2016 was {per_incr}%.")
print("\n")

print("Q10 Find the most common actor in all the movies?")
# Note, the "Actors" column has multiple actors names. You must find a way to search for the most common actor in all the movies.
actors_df=df.assign(Actors=df.Actors.str.split(",")).explode("Actors")
actors_df_strip=actors_df["Actors"].str.strip()
actors_df_v2=pd.DataFrame(actors_df_strip)
actors_df_v3=actors_df_v2.reset_index(drop=True)
actors_num=actors_df_v3["Actors"].value_counts()
actors_num_df=pd.DataFrame(actors_num)
actors_num_max=pd.DataFrame(actors_num).max()
actors_num_max_int=int(actors_num_max)
actor_top=str(actors_num_df.iloc[0:1])
#I struggled to index into the top actor
print(f"The most common actor in all movies is {actor_top} with {actors_num_max_int} movies")
print("\n")

print("Q11 How many unique genres are there in the dataset?")
# Note, the "Genre" column has multiple genres per movie. You must find a way to identify them individually.
genre_df=df.assign(Genre=df.Genre.str.split(",")).explode("Genre")
genre_df_strip=genre_df["Genre"].str.strip()
genre_df_v2=pd.DataFrame(genre_df_strip)
genre_df_v3=genre_df_v2.reset_index(drop=True)
genre_group=genre_df_v3.groupby("Genre")
genres=genre_group.groups
print(f"There are {len(genres)} unique genres.")
print("\n")

print("Q12 Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights.")
# And what advice can you give directors to produce better movies?
print("Correlations with dataset")

corr_matrix = df[["Year","Runtime(minutes)","Rating","Votes","Revenue(millions)","Metascore"]].corr()
print(corr_matrix)
heatmap=sns.heatmap(data=corr_matrix, robust=True, annot=True)
clustermap=sns.clustermap(data=corr_matrix)
plt.show()

print("Q13 Once you have completed the Quiz questions, create a GitHub repository and upload a single python file called (css4p01.py) to it.")
git_url="github.com/lyntonh/CSS4-Project1"
print("This is the link to the file")
print(git_url)