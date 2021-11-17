from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book 
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete 
- 'q' to quit

Your choice:"""

def menu():
  user_input=input(USER_CHOICE)
  while user_input != 'q':
    if user_input == 'a':
      book_name=input('Enter the name and author of the book seperated by a comma:\n').split(',')
      prompt_add_book(book_name)
      #menu()
    elif user_input=='l':
      prompt_list_books()
      #menu()
    elif user_input=='r':
      book=input('Enter the name of the book that was read:\n').strip()
      prompt_read_book(book)
      #menu()
    elif user_input=='d':
      book=input('Enter the name of the book that is to be deleted:\n').strip()
      prompt_delete_book(book)
      #menu()
    else:
      print('Invalid command.')
    user_input=input(USER_CHOICE)

def prompt_add_book(name):
  database.add_book(name)

def prompt_list_books():
  database.list_books()

def prompt_read_book(name):
  database.read_book(name)

def prompt_delete_book(name):
  database.delete_book(name)

menu()