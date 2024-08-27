import traceback
from clear_screen import clear
import time

p = print

print("use 'connect {path of file here}\nthan to run file use 'run' \nuse quit or exit to get out ")
p("cls,clean and clear can be used")
def wait(wait):
    time.sleep(wait)
def main():
    print("Burst.runner")
    while True:
        
        text = input("basic > ").lower()
        if text == "exit" or text == "quit":
            break
        elif text.startswith("connect "):
            file_path = text.split(" ")[1]
            connect_py_file(file_path)
        elif text.startswith('pip '):
            handle_command()
        elif text == 'cls' or text == 'clear' or text == 'clean':
            clear()
            print("Burst.runner")
        
        else:
            print(text)
import subprocess

def handle_command(text):
    if text.startswith('pip '):
        command_parts = text.split()
        command = command_parts[1] if len(command_parts) > 1 else None
        package_name = command_parts[2] if len(command_parts) > 2 else None

        if command == 'install' and package_name:
            try:
                subprocess.check_call(["python", "-m", "pip", "install", package_name])
                print(f"Successfully installed {package_name}.")
            except subprocess.CalledProcessError:
                print(f"Failed to install {package_name}. Please check the package name and try again.")
        
        elif command == 'uninstall' and package_name:
            try:
                subprocess.check_call(["python", "-m", "pip", "uninstall", package_name, "-y"])
                print(f"Successfully uninstalled {package_name}.")
            except subprocess.CalledProcessError:
                print(f"Failed to uninstall {package_name}. Please check the package name and try again.")
        
        elif command == 'list':
            try:
                subprocess.check_call(["python", "-m", "pip", "list"])
            except subprocess.CalledProcessError:
                print("Failed to list installed packages.")
        
        else:
            print("Invalid pip command. Please use 'install <package>', 'uninstall <package>', or 'list'.")
    else:
        print("Unknown command. Please start with 'pip'.")

# Example usage
user_input = input("Enter a command: ")
handle_command(user_input)
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

