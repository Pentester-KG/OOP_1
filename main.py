class Book:
    def __init__(self, title, author, year, book_id):
        self.title = title
        self.author = author
        self.year = year
        self.book_id = book_id
        self.status = "доступный"

    def get_info(self):
        print(
            f"Название: {self.title}\n Автор: {self.author}\n Год выпуска: {self.year}\n ID: {self.book_id},\n Статус: {self.status}")

    def change_status(self, status):
        self.status = status


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.issued_books = []

    def borrow_book(self, book):
        self.issued_books.append(book)

    def return_book(self, book):
        self.issued_books.remove(book)


class Library:
    def __init__(self):
        self.books = []  # List of Book objects
        self.users = []  # List of User objects

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def issue_book(self, book_id, user_id):
        # Find the book by its ID
        book = next((b for b in self.books if b.book_id == book_id), None)
        user = next((u for u in self.users if u.user_id == user_id), None)

        # Check if the book and user exist
        if book is None:
            raise ValueError("Книга не найдена.")
        if user is None:
            raise ValueError("Пользователь не найден")

        # Check if the book is available
        if book.status != "available":
            raise ValueError("Эта книга уже выдана.")

        # Issue the book
        book.change_status("выдан")
        user.borrow_book(book)
        print(f"{user.name} одолжил книгу '{book.title}'.")

    def return_book(self, book_id, user_id):
        # Find the book by its ID
        book = next((b for b in self.books if b.book_id == book_id), None)
        user = next((u for u in self.users if u.user_id == user_id), None)

        # Check if the book and user exist
        if book is None:
            raise ValueError("Книга не найдена.")
        if user is None:
            raise ValueError("Пользователь не найден.")

        # Check if the book is issued to the user
        if book not in user.issued_books:
            raise ValueError("Эта книга не была выдана пользователю.")

        # Return the book
        book.change_status("available")
        user.return_book(book)
        print(f"{user.name} вернул книгу '{book.title}'.")


def main():
    library = Library()

    while True:
        print("\n Меню библиотеки:")
        print("1. Добавить книгу")
        print("2. Зарегистрировать пользователя")
        print("3. Выдать книгу")
        print("4. Вернуть книгу")
        print("5. Склад")
        print("6. Инфо по пользователю")
        print("7. Выход")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите имя автора: ")
            year = int(input("Введите год выпуска: "))
            book_id = input("Введите ID книги: ")
            book = Book(title, author, year, book_id)
            library.add_book(book)
            print(f"Книга '{title}' успешно добавлена.")

        elif choice == "2":
            name = input("Введите имя пользователя: ")
            user_id = input("Введите ID пользователя: ")
            user = User(name, user_id)
            library.register_user(user)
            print(f"Пользователь '{name}' успешно зарегистрирован.")

        elif choice == "3":
            book_id = input("Введите ID книги для выдачи: ")
            user_id = input("Введите ID пользователя: ")
            try:
                library.issue_book(book_id, user_id)
                print(f"Книга под номером '{book_id}' выдана пользователю '{user_id}'.")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            book_id = input("Введите ID книги для возвращения: ")
            user_id = input("Введите ID пользователю: ")
            try:
                library.return_book(book_id, user_id)
                print(f"Книга под номером '{book_id}' вернута пользователем '{user_id}'.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            print("\nИнвентарь библиотеки:")
            for book in library.books:
                book.get_info()

        elif choice == "6":
            user_id = input("Введите ID пользователя для информации: ")
            user_found = False
            for user in library.users:
                if user.user_id == user_id:
                    user_found = True
                    print(f"Пользователь: {user.name}")
                    if user.issued_books:
                        print("Выданные книги:")
                        for issued_book in user.issued_books:
                            issued_book.get_info()
                    else:
                        print("Нет выданных книг.")
                    break
            if not user_found:
                print("Пользователь не найден.")

        elif choice == "7":
            print("Выход из системы.")
            break

        else:
            print("Неправильный выбор. Введите правильно.")


if __name__ == "__main__":
    main()
