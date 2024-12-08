class User:
    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def login(self, username, password):
        return self.username == username and self.password == password

current_user = None
clients = []

def display_menu():
    global current_user
    print("\nМеню:")
    if current_user and current_user.is_admin:
        print("1. Добавить клиента")
    if current_user:
        print("2. Удалить клиента")
       
    print("3. Поиск клиента")
    print("4. Сортировка клиентов")
    print("5. Фильтрация клиентов")
    print("6. Показать всех клиентов")
    print("7. Обновить данные клиента")
    print("0. Выход")
def add_client():
    name = input("Введите имя клиента: ")
    account_number = input("Введите номер счета клиента: ")
    clients.append({"name": name, "account_number": account_number})
    print(f"Клиент '{name}' добавлен.")

def delete_client():
    account_number = input("Введите номер счета клиента для удаления: ")
    global clients
    clients = [client for client in clients if client["account_number"] != account_number]
    print(f"Клиент с номером счета '{account_number}' удален.")

def search_client():
    account_number = input("Введите номер счета клиента для поиска: ")
    found_clients = list(filter(lambda client: client["account_number"] == account_number, clients))
    
    if found_clients:
        print("Найденные клиенты:")
        for client in found_clients:
            print(f"- Имя: {client['name']}, Номер счета: {client['account_number']}")
    else:
        print("Клиенты не найдены.")

def sort_clients():
    global clients
    clients.sort(key=lambda client: client["name"])
    print("Клиенты отсортированы по имени.")

def filter_clients():
    keyword = input("Введите ключевое слово для фильтрации (по имени): ")
    filtered_clients = list(filter(lambda client: keyword.lower() in client["name"].lower(), clients))
    
    if filtered_clients:
        print("Отфильтрованные клиенты:")
        for client in filtered_clients:
            print(f"- Имя: {client['name']}, Номер счета: {client['account_number']}")
    else:
        print("Клиенты не найдены.")

def show_clients():
    if clients:
        print("Список клиентов:")
        for client in clients:
            print(f"- Имя: {client['name']}, Номер счета: {client['account_number']}")
    else:
        print("Список клиентов пуст.")

def update_client():
    account_number = input("Введите номер счета клиента для обновления: ")
    for client in clients:
        if client["account_number"] == account_number:
            new_name = input("Введите новое имя клиента: ")
            client["name"] = new_name
            print(f"Данные клиента с номером счета '{account_number}' обновлены.")
            return
    print(f"Клиент с номером счета '{account_number}' не найден.")

def main():
    global current_user
    users = [
        User("admin", "password", True),
        User("user", "userpassword", False)
    ]

    while True:
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        current_user = next((user for user in users if user.login(username, password)), None)
        if current_user:
            break
        else:
            print("Неверный логин или пароль.")

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == '1' and current_user and current_user.is_admin:
            add_client()
        elif choice == '2' and current_user:
            delete_client()
        elif choice == '3':
            search_client()
        elif choice == '4':
            sort_clients()
        elif choice == '5':
            filter_clients()
        elif choice == '6' and current_user:
            show_clients()
        elif choice == '7' and current_user:
            update_client()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный ввод. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()

