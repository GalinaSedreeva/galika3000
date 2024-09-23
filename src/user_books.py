import pandas as pd
import json

users_df = pd.read_json(
    "users.json", orient="records"
)  # открыть файл с пользователями в датафрейме
users_df = users_df[
    ["name", "gender", "address", "age"]
].copy()  # удалить ненужные поля
users_df.to_json(
    "users_small_records.json", orient="records", indent=4
)  # сохранить измененные данные в новый файл

books_df = pd.read_csv("books.csv")  # открыть файл с книгами в датафрейме
books_df = books_df.drop("Publisher", axis=1)  # удалить ненужное поле
books_df = books_df[
    list(("Title", "Author", "Pages", "Genre"))
]  # расставить поля в нужном порядке
books_df.to_json(
    "books_small.json", orient="records", indent=4
)  # сохранить измененные данные в новый файл

with open("users_small.json", "r") as file:
    users = json.load(file)

with open("books_small.json", "r") as file:
    books = json.load(file)

for user in users:
    user["books"] = books[:8]

with open("result.json", "w") as file:
    json.dump(users, file, indent=4)
