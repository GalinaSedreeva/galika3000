import pandas as pd
import json

# %% Открываю файл с данными о читателях в формате датафрейма. Избавляюсь от ненужных полей. Сохраняю уменьшенную копию исходного файла с данными
users_df = pd.read_json("C:\\Users\\gsedreeva\\OTUS1\\galika3000\\src\\users.json", orient="records")
users_df = users_df[["name", "gender", "address", "age"]].copy()
users_df.to_json("users_small.json", orient="records", indent=4)

# %% Открываю файл с данными о книгах в формате датафрейма. Удаляю ненужное поле и переставляю поля в нужном порядке. Сохраняю полученный файл.
books_df = pd.read_csv("C:\\Users\\gsedreeva\\OTUS1\\galika3000\\src\\books.csv")
books_df = books_df.drop("Publisher", axis=1)
books_df = books_df[list(("Title", "Author", "Pages", "Genre"))]
books_df.to_json("books_small.json", orient="records", indent=4)

with open("users_small.json", "r") as file:
    users = json.load(file)

with open("books_small.json", "r") as file:
    books = json.load(file)
books_list = iter(books)

# %% Функция выдает по 7 книг
j = len(users) * 7


def lib():
    for i in range(0, j, 7):
        yield books[i : i + 7]


a = lib()

# %% Вызываю функцию для каждого читателя
for user in users:
    user["books"] = next(a)

# %% Выдаю оставшиеся книги по одной тем пользователям кому их хватит
for user in users:
    if j < len(books):
        user["books"].append(books[j])
        j += 1

# %% Записываю результат в файл
with open("result.json", "w") as file:
    json.dump(users, file, indent=4)
