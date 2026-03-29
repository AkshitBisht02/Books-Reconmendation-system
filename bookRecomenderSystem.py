import pandas as pd
import numpy as np

books=pd.read_csv('book.csv',on_bad_lines='skip')  # "on_bad_lines='skip" this skips the wrong data from the data instead of generating an error
#print(books.head())  #prints the top 5 rows of the data  and "print(books)""  prints the whole data  

user=pd.read_csv('user.csv',on_bad_lines='skip') 

rating=pd.read_csv('ratings.csv',on_bad_lines='skip') 

#print(books.shape) # prints number of rows then colmns

x=rating['userid'].value_counts()>4 #counts the number of reviews by users greater than 4

y=x[x].index #gives user id of the users which have reviewd more than 4 times

ratings=rating[rating ['userid'].isin(y)]

ratings_with_books=rating.merge(books,on='ISBN') #merge table book and rating on column ISBN

number_rating=ratings_with_books.groupby('Title')['rating'].count().reset_index()
number_rating.rename(columns={'rating':'numofrating'},inplace=True)

final_rating=ratings_with_books.merge(number_rating,on='Title')

final_rating=final_rating[final_rating['numofrating']>=50]

print(final_rating)