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
        R.show_head()
main('movies.csv')
