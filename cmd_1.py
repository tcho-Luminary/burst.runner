import traceback
from clear_screen import clear
import time


def wait(wait):
    time.sleep(wait)
def main():
    print("Burst.runner")
    while True:
        
        text = input("basic > ")
        if text == "exit" or text == "quit":
            break
        elif text.startswith("connect "):
            file_path = text.split(" ")[1]
            connect_py_file(file_path)
        elif text == 'cls' or text == 'clear' or text == 'clean':
            clear()
            print("Burst.runner")
        
        else:
            print(text)

def connect_py_file(file_path):
    print("Burst.runner")
    while True:
        text = input(f"{file_path} > ")
        if text == "run":
            # Run the Python program
            try:
                print(f"Running {file_path}...")
                wait(0.2)
                exec(open(f'{file_path}').read())
            except Exception as e:
                # Handle any exception
                print("An error occurred:", e)
                traceback.print_exc()
        elif text == "exit" or text == "quit":
            break
        elif text == 'cls' or text == 'clear' or text == 'clean':
            clear()
        else:
            print(text)

if __name__ == "__main__":
    main()

