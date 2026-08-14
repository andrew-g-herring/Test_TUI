import sys
from blessed import Terminal

def main():

    term = Terminal()

    message = "hello"

    x = (term.width - len(message)) // 2
    y = term.height // 2

    print(term.clear)

    with term.hidden_cursor(), term.cbreak():

        print(term.move_xy(x, y) + term.red(message))

        exit_msg = "Press any key to exit..."

        exit_x = (term.width - len(exit_msg)) // 2

        print(term.move_xy(exit_x, term.height - 2) + term.normal + exit_msg)

        term.inkey()

    print(term.clear)

if __name__ == "__main__":
    main()