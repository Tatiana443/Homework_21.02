# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны
# реализовать функционал для изменения и удаления данных
def all_contacts():
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)
def find_contact(name):
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if name in line:
                print(line)
def add_contact(new_contact):
    with open('phone_book.txt', 'a', encoding='utf-8') as data:
        data.write('\n')
        data.write(new_contact)
def change_contact(old_data, change_data) -> str:
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        old_data = data.read()
        change_data = old_data.replace(old_data, change_data)
    with open('new_book.txt', 'w', encoding='utf-8') as data:
        data.write(change_data)
        print('Список изменен')
def delete_contact(del_data):
    with open("phone_book.txt", "r", encoding="utf-8") as data:
           data = data.readlines()
    with open("new_book.txt", "w") as data:
                for line in data:
                    if line.strip("\n") != "del_data":
                        data.write(line)
def main_menu(numb):
    if numb == 1:
        all_contacts()
    if numb == 2:
        name = input('Введите искомое имя: ')
        find_contact(name)
    if numb == 3:
        data = input('Введите новый контакт: ')
        add_contact(data)
    if numb == 4:
        old_data = input('Введите контакт для замены: ')
        change_data = input('Введите новый контакт для замены: ')
        change_contact(old_data, change_data)
    if numb == 5:
        del_data = input('Введите контакт, который должен быть удален: ')
        delete_contact(del_data)
while True:
    numb = int(input("Введите 1 - для печати; 2 - для поиска; 3 - для записи; 4 - для изменения; 5 - для удаления; 6 - для выхода: "))
    if numb == 6:
        break
    main_menu(numb)                                