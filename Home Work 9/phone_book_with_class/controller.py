from view import View
from db_manager import Manager


def start():
    data = Manager()
    view = View()
    phone_book = data.get()
    flag = False

    while True:
        choice = view.menu(flag)

        match choice:
            case 1:
                data.open_file()
                flag = True
            case 2:
                data.save_file()
            case 3:
                view.show_contacts(phone_book)
            case 4:
                new = view.new_contact_input()
                name = new.get('name')
                if view.confirm('добавить', name):
                    data.add_phone_book(new)
                    view.print_status('успешно добавлен')
                else:
                    view.print_status('не добавлен')
            case 5:
                view.show_contacts(phone_book)
                index = view.input_id()
                name = data.get_name(index)
                contact = view.new_contact_input()
                if view.confirm('изменить', name):
                    data.change_contact(index, contact)
                    view.print_status('успешно изменен')

            case 6:
                find = view.find_contact()
                result = data.get_contact(find)
                view.show_contacts(result)
            case 7:
                view.show_contacts(phone_book)
                index = view.input_id()
                name = data.get_name(index)
                if view.confirm('удалить', name):
                    data.delete_contact(index)
                    view.print_status('успешно удален')
            case 8:
                if data.check_chenges():
                    if view.confirm_changes():
                        data.save_file()
                print('До свидания!')
                break
