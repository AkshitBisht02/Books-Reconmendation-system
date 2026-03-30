import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

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

final_rating=final_rating[final_rating['numofrating']>=5]

book_pivot=final_rating.pivot_table(columns='userid',index='Title',values='rating') #creates pivot table

book_pivot.fillna(0,inplace=True) #replaces NAN values with 0

book_sparse=csr_matrix(book_pivot) # converted to sparse matrix 

model=NearestNeighbors(algorithm='brute') # nearest neighbour model

model.fit(book_sparse) #model training

# ---------------- RECOMMENDATION PART ---------------- #

# function to recommend books
def recommend(book_name):
    
    # check if book exists in pivot table
    if book_name not in book_pivot.index:
        print("Book not found in dataset ")
        return
    
    # get index of the book
    book_id = np.where(book_pivot.index == book_name)[0][0]
    
    # find nearest neighbors (similar books)
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)
    
    print("\n Recommended Books:\n")
    
    # loop through suggestions (skip first because it's the same book)
    for i in range(1, len(suggestions[0])):
        print(book_pivot.index[suggestions[0][i]])  # print book title


# ---------------- USER INPUT PART ---------------- #

while True:
    user_input = input("\nEnter a book name (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Goodbye 👋")
        break
    
    recommend(user_input)  # call recommendation function

