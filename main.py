from flask import Flask, render_template, request, redirect,     url_for

app = Flask(__name__)


class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category


book_list = [
    Book("1984", "George Orwell", "Dystopian"),
    Book("To Kill a Mockingbird", "Harper Lee", "Classic"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
    Book("Brave New World", "Aldous Huxley", "Dystopian"),
    Book("Moby Dick", "Herman Melville", "Adventure"),
    Book("Pride and Prejudice", "Jane Austen", "Romance"),
    Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    Book("Fahrenheit 451", "Ray Bradbury", "Dystopian"),
    Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy"),
    Book("The Catcher in the Rye", "J.D. Salinger", "Classic"),
    Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy"),
    Book("Crime and Punishment", "Fyodor Dostoevsky", "Philosophical"),
    Book("The Brothers Karamazov", "Fyodor Dostoevsky", "Philosophical"),
    Book("War and Peace", "Leo Tolstoy", "Historical"),
    Book("Anna Karenina", "Leo Tolstoy", "Romance"),
    Book("The Alchemist", "Paulo Coelho", "Adventure"),
    Book("The Picture of Dorian Gray", "Oscar Wilde", "Gothic"),
    Book("The Martian", "Andy Weir", "Science Fiction"),
    Book("Dune", "Frank Herbert", "Science Fiction"),
    Book("Dracula", "Bram Stoker", "Gothic"),
]

@app.route('/')
def home():
    selected_category = request.args.get("category", "all")
    msg = request.args.get("msg", None)

    if selected_category == "all":
        filtered_books = book_list
    else:
        filtered_books = [book for book in book_list if book.category == selected_category]

    # Унікальні категорії:
    categories = sorted(set(book.category for book in book_list))

    return render_template("index.html", books=filtered_books, categories=categories, selected_category=selected_category, msg=msg)



@app.route("/add_book")
def add_book():
    name = request.args.get("name")
    author = request.args.get("author")
    category = request.args.get("category")

    if name and author and category:
        book_list.append(Book(name, author, category))
        return redirect(url_for("home", msg=name))

    return render_template("add_book.html", categories = sorted(set(book.category for book in book_list))
)

# @app.rout("/edit")
# def edit():
#     name = request.args.get("name")
#     author = request.args.get("author")
#     category = request.args.get("category")
#     old_title = request.args.get("old_title")

#     if name and author and category:
#         for book in book_list:
#             if book.title == request.args.get("title"):
#                 book.title 
#     else:
#         our_book = None
#         for book in book_list:
#             if book.title == request.args.get("title"):
#                 our_book = book

#         return render_template("edit.html", book=our_book, categories = sorted(set(book.category for book in book_list))
# )


@app.route("/edit")
def edit():
    new_title = request.args.get("title")
    new_author = request.args.get("author")
    new_category = request.args.get("category")
    old_title_value = request.args.get("old_title")


    if new_title and new_author and new_category and old_title_value:
        for book in book_list:
            if book.title == old_title_value:
                book.title = new_title
                book.author = new_author
                book.category = new_category
                return redirect(url_for("home", msg=f"Книга '{new_title}' оновлена"))

    if request.args.get("title"):
        title_to_edit = request.args.get("title")
        book_to_edit = None

        for book in book_list:
            if book.title == title_to_edit:
                book_to_edit = book
                break 


        return render_template("edit.html", book=book_to_edit, old_title=title_to_edit, categories = sorted(set(book.category for book in book_list))
)












if __name__ == "__main__":
    app.run(debug=True)

