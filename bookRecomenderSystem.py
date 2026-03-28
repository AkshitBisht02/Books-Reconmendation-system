import pandas as pd
import numpy as np

books=pd.read_csv('book.csv',on_bad_lines='skip')  # "on_bad_lines='skip" this skips the wrong data from the data instead of generating an error
print(books.head())  #prints the top 5 rows of the data  and "print(books)""  prints the whole data  

user=pd.read_csv('user.csv',on_bad_lines='skip') 

rateing=pd.read_csv('ratings.csv',on_bad_lines='skip') 