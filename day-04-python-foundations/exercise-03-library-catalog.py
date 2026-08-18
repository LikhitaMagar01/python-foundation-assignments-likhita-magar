# Question 3 - Filtering a JSON Library Catalog
import json

books = [
    {"title": "Deep Learning with Python", "author": "F. Chollet", "year": 2017, "available": True},
    {"title": "Fluent Python", "author": "L. Ramalho", "year": 2022, "available": True},
    {"title": "Automate the Boring Stuff", "author": "A. Sweigart", "year": 2015, "available": True},
    {"title": "Old Python Book", "author": "Someone", "year": 2010, "available": True},
    {"title": "Unavailable New Book", "author": "Someone Else", "year": 2020, "available": False},
]

with open("library.json", "w") as f:
    json.dump(books, f, indent=2)


# --- ANSWER ---
def available_books_after(json_path, year, output_path):
    with open(json_path, "r") as f:
        books = json.load(f)

    titles = [b["title"] for b in books if b["available"] and b["year"] > year]

    with open(output_path, "w") as f:
        json.dump(titles, f, indent=2)

    return titles


print(available_books_after("library.json", 2015, "available_books.json"))
