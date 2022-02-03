# Universidad del Valle de Guatemala
# Mineria de Datos
# HDT1-Exploratory Analysis
#------------------------------------
# Sofia Rueda    19xxx
# Martin Espana  19xxx
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
        df['genres'] = df['genres'].str.split("|").str[0]
        df = df[['genres', 'revenue']].sort_values('revenue', ascending=False)
        df = df.groupby(df['genres']).sum().sort_values('revenue', ascending=False)
        print(df)
        
        ax = df.plot.bar(use_index=True)
        """
        plt.title('Movies per Year (1920-2021)')
        plt.xlabel('Years')
        plt.ylabel('Amount of Movies')
        """
        plt.show()
        


exp = main('movies.csv')
# exp.films_per_year()
# exp.main_genre()
exp.most_profitable_films_by_genre()
