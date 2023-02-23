def menu():
    print('''\n Главное Меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Создать контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход''')
    # while True:
    #     try:
    choice = int(input('Введите номер пункта меню: '))
    if choice in range(1, 9):
        return choice
    else:
        print('Введите число от 1 до 8')
        # except:
        #     print('Вводи только цифры')


def show_contacts(pb: list[dict]) -> print:
    if not pb:
        print('Нет контактов или файл не открыт')
    else:
        for i, contact in enumerate(pb, 1):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{i}. {name:<20} - {phone:<20} - {comment:<20}')


def new_contact_input() -> dict:
    name = input('Введите имя и фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return dict(name=name, phone=phone, comment=comment)


def find_contact() -> any:
    return input('Введите элемент контакта: ')


def input_id() -> int:
    return int(input('Введите индекс: '))


def confirm(condition: str, name: str) -> bool:
    answer = input(f'Вы действительно хотите {condition} контакт {name}? [y/n]: ')
    if answer.lower() == 'y':
        return True
    else:
        return False


def confirm_changes():
    answer = input('У вас есть несохраненные изменения, хотите сохранить? [y/n]: ')
    if answer.lower() == 'y' or answer.lower() == 'н':
        return True
    else:
        return False


def print_status(status: str):
    print(f"[Контакт {status}!]")
