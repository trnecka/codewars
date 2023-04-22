import os

from parse_int import parse_int

tasks = [
    {
        'option': 0,
        'title': 'Terminate this program',
    },
    {
        'option': 1,
        'title': 'Parsing from string format of the number to numeric format',
        'file': 'parse_int.py'
    }
]


def parse_int_api():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Parsing from string format of the number to numeric format.")
        print("Example: two hundred and twenty-two => 222")
        print("For ending program you write <quit>")
        string = input("Input the number in english in the text format:\n")
        if string.strip().lower() == 'quit':
            break
        try:
            print(parse_int(string.strip().lower()))
        except KeyError:
            print("You do not enter valid text. Try again.")
            key_enter = input("Press <ENTER> to continue.")
            continue
        exit_continue = input("Do you want to continue press <ENTER>? Write 'quit' for ending this program: ")
        if exit_continue.strip().lower() == 'quit':
            break


if __name__ == '__main__':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("List of the tasks from the www.codewars.com")
        options = dict()
        for task in tasks:
            if task['option'] == 0:
                print(f"{task['option']} - {task['title']}")
                options['0'] = "exit()"
                continue
            print(f"{task['option']} - {task['title']} <{task['file']}>")
            options['1'] = f"{task['file'].split('.')[0]}_api()"
        option = input('Select the task: ')
        try:
            exec(options[option])
        except KeyError:
            continue


