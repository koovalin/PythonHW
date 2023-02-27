from copy import deepcopy
import os


class Manager:
    """
    Менеджер контактов
    """

    path = 'phone_db.txt'
    phone_book = []
    new_phone_book = []
    flag = False

    def __init__(self):
        if not os.path.exists(Manager.path):
            with open(Manager.path, 'w') as f:
                f.write('')

    def open_file(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                new_contact = {'name': new[0], 'phone': new[1], 'comment': new[2]}
                self.phone_book.append(new_contact)
            print('=====[Файл загружен]=====')
            self.flag = True
        self.new_phone_book = deepcopy(self.phone_book)

    def get(self):
        return self.phone_book

    def get_contact(self, find_contact: str):
        all_find = []
        for contact in self.phone_book:
            for element in contact.values():
                if find_contact.lower() in element.lower():
                    all_find.append(contact)
        return all_find

    def save_file(self):
        data = [';'.join(contact.values()) for contact in self.phone_book]
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(data)
        print('=====[Файл сохранен]=====')

    def add_phone_book(self, new_contact: dict):
        self.phone_book.append(new_contact)

    def change_contact(self, index: int, contact: dict):
        self.phone_book.pop(index-1)
        self.phone_book.insert(index-1, contact)

    def delete_contact(self, index: int):
        self.phone_book.pop(index-1)

    def get_name(self, index: int) -> str:
        return self.phone_book[index-1].get('name')

    def get_number(self, index: int):
        return self.phone_book[index-1].get('phone')

    def check_chenges(self) -> bool:
        if self.phone_book != self.new_phone_book:
            return True
        else:
            return False

    def check_file_open(self):
        if not self.flag:
            return False
        else:
            return True
