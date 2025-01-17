"""
Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на 
обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. 
Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять 
пользователя из системы.

Требования:

1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных 
сотрудников).

2.Класс `Admin`: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный 
для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и 
удалять пользователей из списка (представь, что это просто список экземпляров User).

3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к 
необходимым атрибутам через методы (например, get и set методы).

Вот пример реализации системы управления учетными записями пользователей для небольшой компании, включая классы `User` и 
`Admin`, с инкапсуляцией данных и необходимыми методами:
"""

class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Защищенный атрибут
        self._name = name         # Защищенный атрибут
        self._access_level = 'user'  # Защищенный атрибут

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Специфический уровень доступа для администраторов
        self._users = []  # Список пользователей, управляемых администратором

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: только объекты User могут быть добавлены.")

    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Ошибка: Пользователь с таким ID не найден.")

    def get_users(self):
        return [user.get_name() for user in self._users]

    def get_access_level(self):
        return self._access_level


# Пример использования

# Создание пользователей
user1 = User(1, "Иван")
user2 = User(2, "Мария")

# Создание администратора
admin = Admin(3, "Сергей")

# Добавление пользователей администратором
admin.add_user(user1)
admin.add_user(user2)

# Получение списка пользователей
print("Пользователи в системе:", admin.get_users())

# Удаление пользователя
admin.remove_user(1)

# Получение обновленного списка пользователей
print("Обновленный список пользователей:", admin.get_users())

# Проверка уровня доступа
print(f"Уровень доступа админа {admin.get_name()}: {admin.get_access_level()}")

"""
### Описание кода:

1. **Класс `User`:**
   - Содержит защищенные атрибуты `_user_id`, `_name` и `_access_level`.
   - Имеет методы для доступа к атрибутам (геттеры).

2. **Класс `Admin`:**
   - Наследуется от класса `User`.
   - Устанавливает уровень доступа как `'admin'`.
   - Содержит методы `add_user` и `remove_user` для управления списком пользователей, а также метод `get_users` для 
   получения списка всех пользователей.

3. **Пример использования:**
   - Создаются экземпляры пользователей и администратора.
   - Администратор добавляет пользователей, удаляет их и получает список пользователей.

Этот код демонстрирует инкапсуляцию данных и основные функции управления учетными записями пользователей. Вы можете 
дополнить его дополнительными функциями или методами по мере необходимости.
"""