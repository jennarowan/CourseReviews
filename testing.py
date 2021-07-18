# The purpose of this file is to test code snippets before incorporating them in the main files

import pandas as pd

data = pd.read_csv("reviews.csv")

print(data["Course Name"].unique())