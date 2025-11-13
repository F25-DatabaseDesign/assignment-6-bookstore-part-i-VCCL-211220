from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

categories = [
    {"categoryId": 1, "categoryName": "Classics"},
    {"categoryId": 2, "categoryName": "Children's reading"},
    {"categoryId": 3, "categoryName": "Science fiction"},
    {"categoryId": 4, "categoryName": "Comics"}
]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]

books = [
    {
        "bookId": 1,
        "categoryId": 1,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "978-0000000001",
        "price": 14.99,
        "image": "classic 1.jpg",
        "readNow": 1
    },
    {
        "bookId": 2,
        "categoryId": 1,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "isbn": "978-0000000002",
        "price": 12.99,
        "image": "classic 2.jpg",
        "readNow": 0
    },
    {
        "bookId": 3,
        "categoryId": 1,
        "title": "The Wizard of Oz",
        "author": "L. Frank Baum",
        "isbn": "978-0000000003",
        "price": 10.99,
        "image": "classic 3.png",
        "readNow": 1
    },
    {
        "bookId": 4,
        "categoryId": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "isbn": "978-0000000004",
        "price": 11.99,
        "image": "classic 4.jpg",
        "readNow": 0
    },

    {
        "bookId": 5,
        "categoryId": 2,
        "title": "Percy Jackson",
        "author": "Rick Riordan",
        "isbn": "978-0000000005",
        "price": 13.99,
        "image": "children 1.jpg",
        "readNow": 1
    },
    {
        "bookId": 6,
        "categoryId": 2,
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "isbn": "978-0000000006",
        "price": 15.99,
        "image": "children 2.jpg",
        "readNow": 0
    },
    {
        "bookId": 7,
        "categoryId": 2,
        "title": "Warriors",
        "author": "Erin Hunter",
        "isbn": "978-0000000007",
        "price": 9.99,
        "image": "children 3.jpg",
        "readNow": 1
    },
    {
        "bookId": 8,
        "categoryId": 2,
        "title": "Charlotte's Web",
        "author": "E. B. White",
        "isbn": "978-0000000008",
        "price": 8.99,
        "image": "chilren 4.jpg",
        "readNow": 0
    },

    {
        "bookId": 9,
        "categoryId": 3,
        "title": "Dune",
        "author": "Frank Herbert",
        "isbn": "978-0000000009",
        "price": 16.99,
        "image": "sci fi 1.jpg",
        "readNow": 1
    },
    {
        "bookId": 10,
        "categoryId": 3,
        "title": "From the Dust Returned",
        "author": "Ray Bradbury",
        "isbn": "978-0000000010",
        "price": 12.49,
        "image": "sci fi 2.jpg",
        "readNow": 0
    },
    {
        "bookId": 11,
        "categoryId": 3,
        "title": "The Martian",
        "author": "Andy Weir",
        "isbn": "978-0000000011",
        "price": 13.50,
        "image": "sci fi 3.jpg",
        "readNow": 1
    },
    {
        "bookId": 12,
        "categoryId": 3,
        "title": "1984",
        "author": "George Orwell",
        "isbn": "978-0000000012",
        "price": 10.50,
        "image": "sci fi 4.jpg",
        "readNow": 0
    },

    {
        "bookId": 13,
        "categoryId": 4,
        "title": "The Amazing Spider-Man",
        "author": "Stan Lee",
        "isbn": "978-0000000013",
        "price": 11.49,
        "image": "comic 1.jpg",
        "readNow": 1
    },
    {
        "bookId": 14,
        "categoryId": 4,
        "title": "Batman",
        "author": "Bob Kane",
        "isbn": "978-0000000014",
        "price": 12.29,
        "image": "comic 2.png",
        "readNow": 0
    },
    {
        "bookId": 15,
        "categoryId": 4,
        "title": "Iron Man",
        "author": "Stan Lee",
        "isbn": "978-0000000015",
        "price": 10.99,
        "image": "comic 3.jpg",
        "readNow": 1
    },
    {
        "bookId": 16,
        "categoryId": 4,
        "title": "Superman",
        "author": "Jerry Siegel",
        "isbn": "978-0000000016",
        "price": 9.49,
        "image": "comic 4.jpg",
        "readNow": 0
    }
]
# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template('index.html', categories=categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable
    category_id=int(request.args.get('id'))
    # Create a new list called selected_books containing a list of books that have the selected category
    selected_books = []
    for i in books:
        if i['categoryId']==category_id:
            selected_books.append(i)
    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template('category.html', categories=categories, selected_books=selected_books, selected_category_id=category_id)

@app.route('/search')
def search():
    #Link to the search results page.
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
