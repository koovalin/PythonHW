from copy import deepcopy
import os

path = 'phone_db.txt'
phone_book = []
new_phone_book = []


def open_file():
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        for contact in data:
            new = contact.strip().split(';')
            new_contact = {'name': new[0], 'phone': new[1], 'comment': new[2]}
            phone_book.append(new_contact)
        print('=====[Файл загружен]=====')
    new_phone_book = deepcopy(phone_book)


def get():
    global phone_book
    return phone_book


def get_contact(find_contact: str):
    all_find = []
    for contact in phone_book:
        for element in contact.values():
            if find_contact.lower() in element.lower():
                all_find.append(contact)
    return all_find


def save_file():
    data = [';'.join(contact.values()) for contact in phone_book]
    data = '\n'.join(data)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(data)
    print('=====[Файл сохранен]=====')


def add_phone_book(new_contact: dict):
    phone_book.append(new_contact)


def change_contact(index: int, contact: dict):
    phone_book.pop(index-1)
    phone_book.insert(index-1, contact)


def delete_contact(index: int):
    phone_book.pop(index-1)


def get_name(index: int) -> str:
    return phone_book[index-1].get('name')


def get_number(index: int):
    return phone_book[index-1].get('phone')


def check_chenges() -> bool:
    if phone_book != new_phone_book:
        return True
    else:
        return False
