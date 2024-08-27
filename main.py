import traceback
from clear_screen import clear
import time
import os
import subprocess

p = print

p("use 'connect {path of file here}\nthan to run file use 'run' \nuse quit or exit to get out ")
p("cls,clean and clear can be used")
p("pip support + code . commands support")
p("version 0.2")

def wait(wait):
    time.sleep(wait)

def main():
    print("Burst.runner")
    while True:
        text = input("burst.run > ").lower()
        if text == "exit" or text == "quit":
            break
        elif text == "code .":
            b = input("enter the direct path to code editor exe: ")
            try:
                with open("code_editor_path.txt", "w") as file:
                    file.write(b)
                    print("Path saved successfully!")
                with open("code_editor_path.txt", "r") as file:
                    vscode_path = file.read().strip()
                if os.path.isfile(vscode_path):
                    # Run the executable
                    subprocess.Popen([vscode_path])
                    print("Code editor is now running.")
                else:
                    print("The saved path does not exist. Please save a valid path first.")
            except FileNotFoundError:
                print("No path saved. Please save the path first.")
        elif text.startswith("connect "):
            file_path = text.split(" ")[1]
            connect_py_file(file_path)
        elif text.startswith('pip '):
            handle_command(text)  # Pass the user input to handle_command
        elif text == 'cls' or text == 'clear' or text == 'clean':
            clear()
            print("Burst.runner")
        else:
            print(text)

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
