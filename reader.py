# Libs
import pandas as pd

"""
Universidad del Valle de Guatemala
Author: Oliver Milian
Purpose: CSV loader
"""
class reader(object):
    # Loads the CSV doc
    def __init__(self, csvDoc):
        self.movies = pd.read_csv(csvDoc)
    # Shows the CSV's first 5 rows
    def show_head(self):
        print(self.movies.head())
