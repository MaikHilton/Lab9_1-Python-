def create_file():
    try:
        with open('TF23_1.txt', 'w') as file:
            lines = [
                "Життя — це те, щ0 з тобою в1дбувається, поки ти будуєш плани. - Джон Леннон",
                "Єдиний спос1б робити св0ю роботу добре — це любити її. Якщо ти ще не знайшов свою улюблену справу, продовжуй шукати. - Стів Джобс",
                "Успіх — це вміння рухатись в1д невдачі д0 невдачі, не втрачаючи ентузіазму. Вінстон Черчилль.",
                "Тепер замінимо 1 на 0 і 0 на 1."
            ]
            for line in lines:
                file.write(line + '\n')
        print("Файл TF23_1 створено.")
    except:
        print("Помилка під час створення або запису у файл TF23_1.")


def replace_symbols():
    try:
        with open('TF23_1.txt', 'r') as file1, open('TF23_2.txt', 'w') as file2:
            content = file1.read()
            # Замінюємо символи '1' на '0' і навпаки(щоб не виникла помилка використовуємо X , як тимчасова змінна)
            replaced_content = content.replace('1', 'X').replace('0', '1').replace('X', '0')

            # Розбиваємо контент на блоки по 15 символів
            for i in range(0, len(replaced_content), 15):
                file2.write(replaced_content[i:i+15] + '\n')

        print("Файл TF23_2 створено з заміненими символами.")
    except:
        print("Помилка під час роботи з файлами TF23_1 або TF23_2.")


def read_and_print_file():
    try:
        with open('TF23_2.txt', 'r') as file:
            print("Вміст файлу TF23_2:")
            for line in file:
                print(line.strip())
    except:
        print("Помилка під час читання файлу TF23_2.")


# Виклик функцій
create_file()
replace_symbols()
read_and_print_file()
