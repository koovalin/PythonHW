from copy import deepcopy
import os


class Manager:
    """
    Менеджер контактов
    """
    def __init__(self, path: str = 'phone_db.txt'):
        self.path = path
        self.phone_book = []
        self.new_phone_book = []

    def open_file(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                new_contact = {'name': new[0], 'phone': new[1], 'comment': new[2]}
                self.phone_book.append(new_contact)
        self.new_phone_book = deepcopy(self.phone_book)

    def get(self):
        return self.phone_book

    def save_file(self):
        data = [';'.join(contact.values()) for contact in self.phone_book]
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(data)

    def add_in_phone_book(self, new_contact: dict):
        self.phone_book.append(new_contact)

    def change_contact(self, index: int, contact: dict):
        self.phone_book[index-1] = contact

    def delete_contact(self, index: int):
        self.phone_book.pop(index-1)

    def find_contacts(self, find_contact: str):
        all_find = []
        for contact in self.phone_book:
            for element in contact.values():
                if find_contact.lower() in element.lower():
                    all_find.append(contact)
        return all_find

    def get_contact(self, index: int) -> str:
        return self.phone_book[index-1]

    def get_name(self, index: int) -> str:
        return self.phone_book[index-1].get('name')

    def get_number(self, index: int):
        return self.phone_book[index-1].get('phone')

    def get_comment(self, index: int) -> str:
        return self.phone_book[index-1].get('comment')

    def check_chenges(self) -> bool:
        if self.phone_book != self.new_phone_book:
            return True
        else:
            return False

    def is_file_exist(self):
        if os.path.exists(self.path):
            return True
        else:
            return False

    def create_file(self):
        with open(self.path, 'w') as f:
            f.write('')
