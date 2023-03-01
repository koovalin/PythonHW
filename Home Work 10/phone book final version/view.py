class View:
    """
    Это класс визуала
    """
    @staticmethod
    def menu(flag: bool) -> print:
        print('''\n Главное Меню
        1. Открыть файл
        2. Сохранить файл
        3. Показать контакты
        4. Создать контакт
        5. Изменить контакт
        6. Найти контакт
        7. Удалить контакт
        8. Выход''')
        choice = input('\nВведите номер пункта меню: ')
        if choice.isdigit():
            choice = int(choice)
            if (choice in range(1, 9) and flag) or (choice in [1, 8]):
                return choice
            elif choice in range(2, 8) and not flag:
                return False
            else:
                print('Введите число от 1 до 8')
        else:
            print('Введите число от 1 до 8')

    @staticmethod
    def show_contacts(pb: list[dict]) -> print:
        if not pb:
            print('\nКонтактов нет!')
        else:
            print('\n')
            for i, contact in enumerate(pb, 1):
                name = contact.get('name')
                phone = contact.get('phone')
                comment = contact.get('comment')
                print(f'{i}. {name:<20} | {phone:<20} | {comment:<20}')

    @staticmethod
    def change_contact(book):
        name = input('\nВведите имя и фамилию или нажмите Enter чтобы оставить как есть: ')
        phone = input('Введите номер телефона или нажмите Enter чтобы оставить как есть: ')
        comment = input('Введите комментарий или нажмите Enter чтобы оставить как есть: ')
        return dict(name=name if name else book['name'],
                    phone=phone if phone else book['phone'],
                    comment=comment if comment else book['comment'])

    @staticmethod
    def new_contact_input() -> dict:
        name = input('\nВведите имя и фамилию: ')
        phone = input('Введите номер телефона: ')
        comment = input('Введите комментарий: ')
        return dict(name=name, phone=phone, comment=comment)

    @staticmethod
    def find_contact() -> any:
        return input('\nВведите элемент контакта: ')

    @staticmethod
    def input_id() -> int:
        while True:
            try:
                return int(input('\nВведите индекс или 0 чтобы вернуться: '))
            except ValueError:
                print('Введите индекс контакта')

    @staticmethod
    def confirm(condition: str, name: str) -> bool:
        answer = input(f'\nВы действительно хотите {condition} контакт {name}? [y/n]: ')
        if answer.lower() == 'y':
            return True
        else:
            return False

    @staticmethod
    def confirm_changes() -> bool:
        answer = input('\nУ вас есть несохраненные изменения, хотите сохранить? [y/n]: ')
        if answer.lower() == 'y':
            return True
        else:
            return False

    @staticmethod
    def confirm_save():
        answer = input('\nВы действительно хотите сохранить изменения? [y/n]: ')
        if answer.lower() == 'y':
            return True
        else:
            return False

    @staticmethod
    def confirm_open_file() -> bool:
        answer = input('\nФайл закрыт, открыть файл? [y/n]: ')
        if answer.lower() == 'y':
            return True
        else:
            return False

    @staticmethod
    def print_status(status: str):
        print(f"\n[Контакт {status}!]")

    @staticmethod
    def print_file_status(status: str):
        print(f"\n[Файл {status}!]")

    @staticmethod
    def confirm_creat_file() -> bool:
        answer = input('Файл отсутствует, создать пустой файл? [y/n]: ')
        if answer.lower() == 'y':
            return True
        else:
            return False
