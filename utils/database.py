books_file = 'books.txt'

def add_book(name):
    with open(books_file, 'a') as file:
        file.write(f'{name[0]},{name[1]},0\n')

def read_book(name):
    books = list_books()
    for book in books:
      #print(book)
      #print(name)
      if book['name'] == name:
        book['read'] = '1'
    _save_all_books(books)

def _save_all_books(books):
  with open(books_file, 'w') as file:
    for book in books:
      file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    #global books # this statement ensures the global books variable is used inside the function.
    books=list_books()
    books = [book for book in books if book['name']!=name]
    _save_all_books(books)

def list_books():
   with open(books_file, 'r') as file:
     lines=[line.strip().split(',') for line in file.readlines()]
     return [
       {'name': line[0], 'author': line[1], 'read': line[2]} for line in lines
       ]