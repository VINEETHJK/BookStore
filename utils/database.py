books=[]
def add_book(name):
    books.append({'name': name[0], 'author': name[1], 'read': False})

def read_book(name):
    for book in books:
        if  name==book['name']:
            book['read']=True


# def delete_book(name):
#     for book in books:
#         if name == book['name']:
#             books.remove(book)


def delete_book(name):
  global books # this statement ensures the global books variable is used inside the function.
  books=[book for book in books if book['name']!=name]

def list_books():
    for book in books:
        print(book)
