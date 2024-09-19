import pandas as pd
import json

users_df = pd.read_json('users.json' , orient='records')
users_df = users_df[['name', 'gender' , 'address', 'age']].copy()
users_df.to_json ('users_small_records.json', orient='records', indent = 4)
books_df = pd.read_csv('books.csv')

books_df = books_df.drop('Publisher', axis=1)
books_df = books_df[list(('Title', 'Author', 'Pages', 'Genre'))]
books_df.to_json ('books_small.json', orient='records', indent = 4)

with open('users_small.json', 'r') as file:
    users = json.load(file)

with open('books_small.json', 'r') as file:
    books = json.load(file)

for user in users:
    user['books'] = books[:8] 

with open('result.json', 'w') as file:
    json.dump(users, file, indent=4)
