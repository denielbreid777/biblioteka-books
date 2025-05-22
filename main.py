from flask import Flask, render_template, request, make_response


app = Flask(__name__)


class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category



book_list = [
    Book( "1984", "George Orwell", "Dystopian"),
    Book( "To Kill a Mockingbird", "Harper Lee", "Classic"),
    Book( "The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
    Book( "Brave New World", "Aldous Huxley", "Dystopian"),
    Book( "Moby Dick", "Herman Melville", "Adventure"),
    Book( "Pride and Prejudice", "Jane Austen", "Romance"),
    Book( "The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    Book( "Fahrenheit 451", "Ray Bradbury", "Dystopian"),
    Book( "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy"),
    Book( "The Catcher in the Rye", "J.D. Salinger", "Classic"),
    Book( "The Lord of the Rings", "J.R.R. Tolkien", "Fantasy"),
    Book( "Crime and Punishment", "Fyodor Dostoevsky", "Philosophical"),
    Book( "The Brothers Karamazov", "Fyodor Dostoevsky", "Philosophical"),
    Book( "War and Peace", "Leo Tolstoy", "Historical"),
    Book( "Anna Karenina", "Leo Tolstoy", "Romance"),
    Book( "The Alchemist", "Paulo Coelho", "Adventure"),
    Book( "The Picture of Dorian Gray", "Oscar Wilde", "Gothic"),
    Book( "The Martian", "Andy Weir", "Science Fiction"),
    Book( "Dune", "Frank Herbert", "Science Fiction"),
    Book( "Dracula", "Bram Stoker", "Gothic"),
]



@app.route("/")
def home():
    return render_template("index.html", books=book_list)































app.run(debug=True)
