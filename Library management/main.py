import tkinter as tk

from tkinter import messagebox


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Book '{book.title}' added successfully!"

    def display_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(
                f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print(
                        f"You have borrowed the book '{book.title}'. Enjoy reading!")
                    return f"You have borrowed the book '{book.title}'. Enjoy reading!"
                else:
                    print("Sorry, the book is not available for borrowing.")
                    return "Sorry, the book is not available for borrowing."
                return
        print("Book not found in the library.")
        return "Book not found in the library."

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print(f"Thank you for returning the book '{book.title}'.")
                    return f"Thank you for returning the book '{book.title}'."
                else:
                    print("This book is already available in the library.")
                    return "This book is already available in the library."
        print("Book not found in the library.")
        return "Book not found in the library."


class LibraryGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("600x400")  # Set the window size

        self.library = Library()

        self.choice_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self, text="Library Management System", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        options = [
            "Add Book",
            "Display Books",
            "Borrow Book",
            "Return Book",
            "Exit"
        ]

        for idx, option in enumerate(options, start=1):
            tk.Radiobutton(
                self,
                text=option,
                variable=self.choice_var,
                value=str(idx),
                font=("Helvetica", 12)
            ).pack(anchor="w", padx=10, pady=5)

        submit_button = tk.Button(
            self, text="Submit", command=self.handle_choice, font=("Helvetica", 12, "bold"))
        submit_button.pack(pady=15)

    def handle_choice(self):
        choice = self.choice_var.get()

        if choice == "1":
            self.add_book_window()
        elif choice == "2":
            self.display_books()
        elif choice == "3":
            self.borrow_book_window()
        elif choice == "4":
            self.return_book_window()
        elif choice == "5":
            self.destroy()

    def add_book_window(self):
        window = tk.Toplevel(self)
        window.title("Add Book")

        tk.Label(window, text="Enter Book ID:",
                 font=("Helvetica", 12)).pack(pady=5)

        # Increase the width of the Entry widget
        book_id_entry = tk.Entry(window, font=("Helvetica", 12), width=30)
        book_id_entry.pack(pady=5)

        tk.Label(window, text="Enter Title:",
                 font=("Helvetica", 12)).pack(pady=5)
        title_entry = tk.Entry(window, font=("Helvetica", 12), width=30)
        title_entry.pack(pady=5)

        tk.Label(window, text="Enter Author:",
                 font=("Helvetica", 12)).pack(pady=5)
        author_entry = tk.Entry(window, font=("Helvetica", 12), width=30)
        author_entry.pack(pady=5)

        tk.Button(
            window,
            text="Add Book",
            command=lambda: self.add_book(
                book_id_entry.get(),
                title_entry.get(),
                author_entry.get()
            ),
            font=("Helvetica", 12, "bold")
        ).pack(pady=10)

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        message = self.library.add_book(book)
        messagebox.showinfo("Success", message)

    def display_books(self):
        books_window = tk.Toplevel(self)
        books_window.title("Available Books")

        text_widget = tk.Text(books_window)
        text_widget.pack()

        for book in self.library.books:
            status = "Available" if book.is_available else "Not Available"
            book_info = (
                f"Book ID: {book.book_id}\n"
                f"Title: {book.title}\n"
                f"Author: {book.author}\n"
                f"Status: {status}\n\n"
            )
            text_widget.insert(tk.END, book_info)

    def borrow_book_window(self):
        window = tk.Toplevel(self)
        window.title("Borrow Book")

        tk.Label(window, text="Enter Book ID:",
                 font=("Helvetica", 12)).pack(pady=5)

        # Increase the width of the Entry widget
        book_id_entry = tk.Entry(window, font=("Helvetica", 12), width=30)
        book_id_entry.pack(pady=5)

        tk.Button(
            window,
            text="Borrow Book",
            command=lambda: self.borrow_book(book_id_entry.get()),
            font=("Helvetica", 12, "bold")
        ).pack(pady=10)

    def borrow_book(self, book_id):
        message = self.library.borrow_book(book_id)
        messagebox.showinfo("Success", message)

    def return_book_window(self):
        window = tk.Toplevel(self)
        window.title("Return Book")

        tk.Label(window, text="Enter Book ID:",
                 font=("Helvetica", 12)).pack(pady=5)

        # Increase the width of the Entry widget
        book_id_entry = tk.Entry(window, font=("Helvetica", 12), width=30)
        book_id_entry.pack(pady=5)

        tk.Button(
            window,
            text="Return Book",
            command=lambda: self.return_book(book_id_entry.get()),
            font=("Helvetica", 12, "bold")
        ).pack(pady=10)

    def return_book(self, book_id):
        message = self.library.return_book(book_id)
        messagebox.showinfo("Success", message)


if __name__ == "__main__":
    app = LibraryGUI()
    app.mainloop()
