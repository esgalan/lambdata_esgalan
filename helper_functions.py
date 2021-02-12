# imports
import pandas as pd
import numpy as np
from sklearn.utils import shuffle


class Helper:
    """Helper class containing helper functions"""

    def __init__(self, DataFrame):
        self.df = DataFrame

    def null_count(self):  # first helper function
        """
        null_count takes a df as an argument and returns
        sum of null values
        """
        return self.df.isnull().sum().sum()

    def randomize(self, seed):  # second helper function
        """
        randomize takes a df and an integer as arguments and performs
        a random shuffle on df values
        """
        return shuffle(self.df, random_state=seed)

# df for testing purposes
# df = pd.DataFrame({
#     "A": [1, 2, 3],
#     "B": [4, 5, 6],
#     "C": [7, 8, 9]
# })

# testing class and methods
# test_df = Helper(df)
# print(test_df.null_count())
# print(test_df.randomize(10))
