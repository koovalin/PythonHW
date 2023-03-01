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
            case False:
                if view.confirm_open_file():
                    data.open_file()
                    view.print_file_status('успешно загружен')
                    flag = True
            case 1:
                if not data.is_file_exist() and view.confirm_creat_file():
                    data.create_file()
                else:
                    continue
                data.open_file()
                flag = True
            case 2:
                if view.confirm_save():
                    data.save_file()
                    view.print_file_status('успешно сохранен')
            case 3:
                view.show_contacts(phone_book)
            case 4:
                new_contact_info = view.new_contact_input()
                new_name = new_contact_info.get('name')
                if view.confirm('добавить', new_name):
                    data.add_in_phone_book(new_contact_info)
                    view.print_status('успешно добавлен')
                else:
                    view.print_status('не добавлен')
            case 5:
                while True:
                    view.show_contacts(phone_book)
                    contact_index = view.input_id()
                    if not contact_index:
                        break
                    elif contact_index - 1 not in range(len(data.get())):
                        view.print_status('отсутствует')
                        continue
                    contact_name = data.get_name(contact_index)
                    take_info = data.get_contact(contact_index)
                    info_to_change = view.change_contact(take_info)
                    if view.confirm('изменить', contact_name):
                        data.change_contact(contact_index, info_to_change)
                        view.print_status('успешно изменен')
                        continue
                    else:
                        view.print_status('не был изменен')
                        continue
            case 6:
                find = view.find_contact()
                result = data.find_contacts(find)
                view.show_contacts(result)
            case 7:
                while True:
                    view.show_contacts(phone_book)
                    contact_index = view.input_id()
                    if not contact_index:
                        break
                    elif contact_index - 1 not in range(len(data.get())):
                        view.print_status('отсутствует')
                        continue
                    contact_name = data.get_name(contact_index)
                    if view.confirm('удалить', contact_name):
                        data.delete_contact(contact_index)
                        view.print_status('успешно удален')
                        continue
                    else:
                        view.print_status('не был удален')
                        continue
            case 8:
                if data.check_chenges():
                    if view.confirm_changes():
                        data.save_file()
                        view.print_file_status('сохранен')
                    else:
                        view.print_file_status('не был сохранен')
                print('До свидания!')
                break

