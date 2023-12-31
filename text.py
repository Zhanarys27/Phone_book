menu = ['Главное меню',
        'Открыть файл',
        'Сохранить файл',
        'Показать контакты',
        'Создать контакт',
        'Найти контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Выход']
input_menu = 'Выберите пункт меню: '
input_menu_error = f'Ввести нужно ЧИСЛО (от 0 до {len(menu) - 1})'

load_succesfull = 'Телефонна книга загружена успешно!'
save_succesfull = 'Телефонна книга сохранена успешно!'

empty_book_error = 'Телефонная книга пуста или не открыта!'

input_search_word = 'Введите ключевое слово для поиска: '

input_edit_contact_id = 'Введите ID контакта, который хотите изменить: '

operation = ['создан', 'изменен', 'удален']

input_del_contact_id = 'Введите ID контакта, который хотите удалить: '

confirm_changes = 'У вас есть несохраненные изменения! Сохранить? (y/n): '

exit_programm = 'До свидания! до новых встреч!'


def input_contact(new: bool = False) -> list[str]:
    add = 'или ENTER, чтоб оставить без изменений' if new else ''
    return [f'Введите имя нового контакта {add}: ',
            f'Введите номер нового контакта {add}: ',
            f'Введите комментарий {add}: ']


def contact_action(name: str, action: str) -> str:
    return f'Контакт {name} успешно {action}!'


def not_find(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены!'
