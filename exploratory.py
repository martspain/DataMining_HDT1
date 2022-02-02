# Universidad del Valle de Guatemala
# Mineria de Datos
# HDT1-Exploratory Analysis
#------------------------------------
# Sofia Rueda    19xxx
# Martin Espana  19xxx
# Oliver de Leon 19270

import pandas as pd
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
        df = self.df['releaseDate']
        print(df.head())
        pass


exp = main('movies.csv')
exp.films_per_year()
