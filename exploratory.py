# Universidad del Valle de Guatemala
# Mineria de Datos
# HDT1-Exploratory Analysis
#------------------------------------
# Sofia Rueda    19099
# Martin Espana  19258
# Oliver de Leon 19270

import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from reader import reader as Reader


class main(object):

    def __init__(self, csvDoc):
        # Universal Doc
        self.csvDoc = csvDoc
        # Classes
        R = Reader(csvDoc)
        self.df = R.movies

    # Films-per-year and top year film production amount
    def films_per_year(self):
        df = self.df
        # Turning releaseDate column into an actual datetime type column, then extracting just the year
        df['releaseDate'] = pd.to_datetime(df['releaseDate'], errors='coerce').dt.year
        # Grouping releaseDate by size, merging it into new "count" column.
        df = df.groupby(df['releaseDate']).size().to_frame('count')
        # DataFrame is sortered and chopped up
        df = df.sort_values('count', ascending=False).head(25)
        # Then the top value name it's extracted
        maxYearProd = df.iloc[0].name
        
        print("-------------------------")
        print("Top year production:",maxYearProd)
        print("-------------------------")
        print(df.head())

        ax = df.plot.bar(y='count', use_index=True)
        plt.title('Movies per Year (1920-2022)')
        plt.xlabel('Years')
        plt.ylabel('Amount of Movies')
        plt.show()

    # Top genre for the 20 latest released films and data main genre
    def main_genre(self):
        df_all = self.df
        # Turning releaseDate column into an actual datetime type column
        df_all['releaseDate'] = pd.to_datetime(df_all['releaseDate'], errors='coerce')
        # Sorting into the lastest released films and limiting into the last 20
        df_all = df_all.sort_values('releaseDate', ascending=False)
        df = df_all.copy().head(20)
        # genres composition has been splitted
        df['genres'] = df['genres'].str.split("|")
        df_all['genres'] = df_all['genres'].str.split("|")
        # genres are extended and grouped by size. Then sorted again
        df = df.explode("genres").reset_index(drop=True)
        df_all = df_all.explode("genres").reset_index(drop=True)
        df = df.groupby("genres").size().sort_values(ascending=False)
        df_all = df_all.groupby("genres").size().sort_values(ascending=False)

        print(df)
        print("--------------------------------")
        print("Top genre Latest 20 films:",df.idxmax())
        print("--------------------------------")
        print(df_all)
        print("Top genre all-time films:",df_all.idxmax())
        print("--------------------------------")
        
        ax = df.plot.pie(use_index=True)
        """
        plt.title('Movies per Year (1920-2021)')
        plt.xlabel('Years')
        plt.ylabel('Amount of Movies')
        """
        plt.show()
        ax_2 = df_all.plot.pie(use_index=True)
        plt.show()

    # Most profitable films by genre
    def most_profitable_films_by_genre(self):
        df = self.df
        # Main genre is selected
        df['genres'] = df['genres'].str.split("|").str[0]
        # Profit per genre's been sorted
        df = df[['genres', 'revenue']].sort_values('revenue', ascending=False)
        # Total revenue per genre
        df = df.groupby(df['genres']).sum().sort_values('revenue', ascending=False)
        print(df)
        
        print("--------------------------------")
        print("Top main genre Revenue:",df.idxmax())
        print("--------------------------------")
    
    # Directors from the Top20 best voted films
    def directors_BestTop20(self):
        df = self.df
        # Main genre is selected
        df = df.sort_values('voteCount', ascending=False).head(20)
        df['director'] = df['director'].str.split("|")
        df = df.explode("director").reset_index(drop=True)
        # Profit per genre's been sorted
        # Total revenue per genre
        print(df['director'].drop_duplicates())
        

    # worst movie according to the votes of all users
    def worst_movie(self):
        df = self.df
        df = df[['title', 'voteCount']].sort_values('voteCount', ascending=True).head(1)

        print(df)
    
    # months with the highest grossing releases 
    def months_highest_grossing_releases(self):
        df = self.df
        df['releaseDate'] = pd.to_datetime(df['releaseDate'], errors='coerce').dt.month 
        df = df.groupby(['releaseDate'])['revenue'].count()

        print(df)

        ax = df.plot.bar(y='count', use_index=True)
        plt.title('Highest grossing releases per month')
        plt.xlabel('Months')
        plt.ylabel('Amount of Movies')
        plt.show()

    # main genre with the longest films

    def main_genre_longest_films(self):
        df = self.df
        df['genres'] = df['genres'].str.split("|").str[0]

        df = df[['genres', 'runtime']].sort_values('runtime', ascending=False)
        df = df.groupby(df['genres']).sum().sort_values('runtime', ascending=False)

        print(df)

        ax = df.plot.bar(use_index=True)
        plt.title('Total runtime per genre')
        plt.xlabel('Genre')
        plt.ylabel('Total runtime')
        plt.show()

    # popularity and income of films influenced by the number of men and women in the cast 
    # popularity, revenue, castWomenAmount, castMenAmount

    # Top 10 Movies with more budget
    def ten_movies_with_more_budget(self):
        df = self.df
        print("--------------------------------")
        print('Top 10 Movies\' budgets')
        print("--------------------------------")
        print(df[['title','budget']].sort_values('budget', ascending=False).head(10))
    
    # Top 10 Movies with more budget
    def ten_movies_with_more_revenue(self):
        df = self.df
        print("--------------------------------")
        print('Top 10 Movies\' revenue')
        print("--------------------------------")
        print(df[['title','revenue']].sort_values('revenue', ascending=False).head(10))
    
    # Most voted movie
    def most_voted_movie(self):
        df = self.df
        print("--------------------------------")
        print('Most voted Movie')
        print("--------------------------------")
        print(df[['title', 'voteCount']].sort_values('voteCount', ascending=False).head(1))

    # Actors per movie
    def actors_quantity(self):
        # Actors per movie
        df = self.df
        secondDf = self.df
        df['actors'] = df['actors'].str.split("|")
        df = df.explode('actors').reset_index(drop=True)
        df['actors'].drop_duplicates()
        df = df[['actors']].groupby(df['title']).count().sort_values('actors', ascending=False)

        # Movies with more actors
        print('-----------------------')
        print('Top 10 movies with more actors')
        print('-----------------------')
        print(df.head(10))

        # Movies with less actors
        print('-----------------------')
        print('Top 10 movies with less actors')
        print('-----------------------')
        print(df.tail(10))

        # Movies with less revenue
        print("--------------------------------")
        print('Top 10 movies with less revenue')
        print("--------------------------------")
        print(secondDf[['title','revenue']].sort_values(['revenue', ], ascending=False).tail(10))

    # month vs revenue
    def month_vs_revenue(self):
        df = self.df
        print(pd.to_datetime(df.releaseDate))

    



exp = main('movies.csv')
# exp.films_per_year()
# exp.main_genre()
# exp.most_profitable_films_by_genre()
# exp.directors_BestTop20()
# exp.main_genre_longest_films()
# exp.ten_movies_with_more_budget()
# exp.ten_movies_with_more_revenue()
# exp.most_voted_movie()
# exp.actors_quantity()
exp.month_vs_revenue()