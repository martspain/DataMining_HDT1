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
        df = df.sort_values('count', ascending=False).head(25)
        # DataFrame is sortered, then the top value name it's extracted
        maxYearProd = df.iloc[0].name
        
        print("-------------------------")
        print("Top year production:",maxYearProd)
        print("-------------------------")
        print(df.head())

        ax = df.plot.bar(y='count', use_index=True)
        plt.show()

exp = main('movies.csv')
exp.films_per_year()
