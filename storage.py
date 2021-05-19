import csv
import pandas as pd

'''all_movies = []

with open ('final.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    print(reader)

popular_movies = []'''

data = pd.read_csv('final.csv')

all_movies = data.values.tolist()