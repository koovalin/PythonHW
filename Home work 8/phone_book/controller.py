import view
import db_manager


def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                db_manager.open_file()
            case 2:
                db_manager.save_file()
            case 3:
                pb = db_manager.get()
                view.show_contacts(pb)
            case 4:
                new = view.new_contact_input()
                name = new.get('name')
                if view.confirm('добавить', name):
                    db_manager.add_phone_book(new)
                    view.print_status('успешно добавлен')
                else:
                    view.print_status('не добавлен')
            case 5:
                pb = db_manager.get()
                view.show_contacts(pb)
                index = view.input_id()
                name = db_manager.get_name(index)
                contact = view.new_contact_input()
                if view.confirm('изменить', name):
                    db_manager.change_contact(index, contact)
                    view.print_status('успешно изменен')

            case 6:
                find = view.find_contact()
                result = db_manager.get_contact(find)
                view.show_contacts(result)
            case 7:
                pb = db_manager.get()
                view.show_contacts(pb)
                index = view.input_id()
                name = db_manager.get_name(index)
                if view.confirm('удалить', name):
                    db_manager.delete_contact(index)
                    view.print_status('успешно удален')
            case 8:
                if db_manager.check_chenges():
                    if view.confirm_changes():
                        db_manager.save_file()
                print('До свидания!')
                break

