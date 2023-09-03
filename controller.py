from model import PhoneBook
import text
import view


def search_contact(pb):
    word = view.input_request(text.input_search_word)
    result = pb.find_contact(word)
    view.show_book(result, text.not_find(word))
    if result:
        return True


def start():
    pb = PhoneBook()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                pb.open_file()

                view.print_massage(text.load_succesfull)
            case 2:
                pb.save_file()
                view.print_massage(text.save_succesfull)

            case 3:
                view.show_book(pb, text.empty_book_error)
            case 4:
                new_contact = view.input_contact(text.input_contact())
                pb.add_contact(new_contact)
                view.print_massage(text.contact_action(new_contact[0], text.operation[0]))
            case 5:
                search_contact(pb)
            case 6:
                if search_contact(pb):
                    c_id = int(view.input_request(text.input_edit_contact_id))
                    new_contact = view.input_contact(text.input_contact(True))
                    name = pb.edit_contact(c_id, new_contact)
                    view.print_massage(text.contact_action(name, text.operation[1]))
            case 7:
                if search_contact(pb):
                    c_id = int(view.input_request(text.input_del_contact_id))
                    name = pb.delete_contact(c_id)
                    view.print_massage(text.contact_action(name, text.operation[2]))

            case 8:
                if pb.original_book != pb.phone_book:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        pb.save_file()
                        view.print_massage(text.save_succesfull)

                view.print_massage(text.exit_programm)

                break
