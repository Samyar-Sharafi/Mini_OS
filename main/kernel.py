"""
author: Samyar-Sharafi

this is an Mini os that, you know, acts like the linux
terminal and have many features like
file manger, math, cmd, google search(or duckduckgo tbh)

IF any features were added, please add it to the help code.(line 233)

IF possible, optimize the code as much as you could and document the new code
with this format:
#---func_name---#
#author: {author} the changes
(the code)
#---func_name---end#

in the main() function:
#---app_name---#
if user_input == "{file command}":
    {call the function}
    {update the help text}
#---app_name---<end>#

IF possible, use "rich" anywhere you edit.

"""


import time
from os import name as os_name, path, system, remove
import subprocess # <--for File management
import getpass  # <-- for hidden password input
from rich import print as rich_print  # <-- Use rich_print for colored output
from rich.console import Console  # <-- Use rich_print for colored output too
import platform
import shutil
import psutil
from datetime import datetime
console = Console()

# ---login---<code>#


def login():
    global Name

    # ---load user info---#
    try:
        with open("user.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            Name = lines[0].strip() if len(lines) > 0 else "default(PASSWORD IS EMPTY STRING)"
            Password = lines[1].strip() if len(lines) > 1 else ""
    except FileNotFoundError:
        Name, Password = "default(PASSWORD IS EMPTY STRING)", ""
    # ---load user info---end#
    rich_print(f"[bold cyan]UserName: {Name}[/bold cyan]")
    wrong_password_count = 0

    while True:  # loop to let user retry after sleep
        Password_input = getpass.getpass("Password: ")  # <-- hidden input

        if Password_input == Password:
            rich_print(
                """

[bold green]
    █░░░█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀
    █▄█▄█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀
    ░▀░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀
[/bold green]
"""
            )
            # ---save user info---#
            with open("user.txt", "w", encoding="utf-8") as f:
                f.write(f"{Name}\n{Password}\n")
            # ---save user info---end#
            return True, Name  # Return both success and username
        else:
            wrong_password_count += 1
            rich_print("[red]Wrong Password, try again[/red]")

            if wrong_password_count == 5:
                rich_print(
                    "[yellow]Too many wrong attempts. Sleeping for 20 seconds... 😴[/yellow]"
                )
                for i in range(20, 0, -1):
                    rich_print(
                        f"[yellow]Please wait... {i}s[/yellow]", end="\r"
                    )  # dynamic countdown
                    time.sleep(1)
                rich_print("\n[bold cyan]Try again![/bold cyan]\n")
                wrong_password_count = 0  # reset count after sleep


# ---login---<code--->end#

#---logout---<code>#
def logout():
    login()

# ---logout---end#

# ---fileM---<code>#
def create_file():
    """Create a new empty file using subprocess, with colored output for status."""
    rich_print(
        "[bold magenta]Enter the full file name (with extension):[/bold magenta]"
    )
    filename = input()
    rich_print(
        "[bold magenta]Enter the directory to save the file (leave blank for current directory):[/bold magenta]"
    )
    directory = input()
    if directory.strip():
        full_path = path.join(str(directory), str(filename))
    else:
        full_path = str(filename)
    if os_name == "nt":
        cmd = f"type nul > \"{full_path}\""
    else:
        cmd = f"touch \"{full_path}\""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        rich_print(f"[green]File \"{full_path}\" created successfully via subprocess.[/green]")
    else:
        rich_print(f"[red]Subprocess error: {result.stderr}[/red]")


def delete_file():
    """Delete a file using os.remove, with colored output for status."""
    rich_print(
        "[bold magenta]Write file path to delete (if in current path, just write the file name with extension):[/bold magenta]"
    )
    removing_file = input()
    try:
        remove(removing_file)
        rich_print(
            f"[green]File \"{removing_file}\" deleted successfully.[/green]")
    except Exception as e:
        rich_print(f"[red]Error deleting file: {e}[/red]")


# ---fileM---<code--->end#


# ---Math---<code>#
def add(first_value: int, second_value: int) -> int:
    """Add two integers."""
    return first_value + second_value


def subtract(first_value: int, second_value: int) -> int:
    """Subtract two integers."""
    return first_value - second_value


def multiply(first_value: int, second_value: int) -> int:
    """Multiply two integers."""
    return first_value * second_value


def divide(first_value: int, second_value: int) -> float | None:
    """Divide two integers. Returns None on ZeroDivisionError."""
    try:
        return first_value / second_value
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None


# ---Math---<code--->end#


# ---Isearch---<code>#
def Isearch_search():
    import requests
    from bs4 import BeautifulSoup

    rich_print("[bold magenta]search the internet![/bold magenta]")
    query = input(">>> ")
    rich_print(f"[blue]Searching internet for: {query}...[/blue]")
    url = "https://html.duckduckgo.com/html/"
    params = {"q": query}
    try:
        response = requests.post(url, data=params, timeout=10)
        response.raise_for_status()
    except Exception as e:
        rich_print(f"[red]Error fetching search results: {e}[/red]")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for result in soup.find_all("a", class_="result__a", limit=10):
        title = result.get_text(strip=True)
        link = result.get("href") # type: ignore
        if title and link:
            results.append((title, link))
    if not results:
        rich_print(
            "[yellow]No results found or search engine blocked the request.[/yellow]"
        )
        return
    for title, link in results:
        rich_print(f"[bold green]{title}[/bold green]")
        rich_print(f"[blue]{link}[/blue]\n")
        print("\n" * 2)
# ---Isearch---<code--->



#---NeoFecth---<code>#
def neofetch():
    rich_print("""
    [bold blue]
                   .oodMMMMMMMMMMMMM
       ..oodMMM  MMMMMMMMMMMMMMMMMMM
 oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM
       ````^^^^  ^^MMMMMMMMMMMMMMMMM
                      ````^^^^^^MMMM  
    [/bold blue]""")
    rich_print(f"[bold green]User:[/bold green] {username}",)
    rich_print(f"[bold green]OS:[/bold green] {platform.system()} {platform.release()}")
    rich_print(f"[bold green]Machine:[/bold green] {platform.machine()}")
    rich_print(f"[bold green]Processor:[/bold green] {platform.processor()}")
    rich_print(f"[bold green]Python:[/bold green] {platform.python_version()}")
    rich_print(f"[bold green]Time:[/bold green] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    # Disk usage
    total, used, free = shutil.disk_usage('.')
    rich_print(f"[bold green]Disk:[/bold green] {used // (2**20)}MB / {total // (2**20)}MB used")
    # Memory usage
    mem = psutil.virtual_memory()
    rich_print(f"[bold green]RAM:[/bold green] {mem.used // (2**20)}MB / {mem.total // (2**20)}MB used")
    # Uptime
    uptime_seconds = int(time.time() - psutil.boot_time())
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    rich_print(f"[bold green]Uptime:[/bold green] {hours}h {minutes}m {seconds}s")


def main():
    
    # Get username from login
    global Name
    while True:
        prompt = (
            f"[bold green]{Name}[/bold green]---> [yellow]{time.strftime("%Y-%m-%d")}[/yellow] , "
            f"[cyan]{time.strftime("%H:%M:%S")}[/cyan]\n[magenta]>>> [/magenta]")
        console.print(prompt, end="")
        user_input = input()

    # ---neofetch---#
        if user_input == "neofetch":
              neofetch()
            
        # ---calculator app---#
        if user_input == "cal":
            console.print(
                "[magenta]What do you want to do? (e.g., 5 + 3, or 5+3)[/magenta]",
                end="",
            )
            user_input_math = input()
            user_input_math_no_spaces = user_input_math.replace(" ", "")
            operator_found = False
            for operator_char in ["+", "-", "*", "/"]:
                if operator_char in user_input_math_no_spaces:
                    parts = user_input_math_no_spaces.split(operator_char)
                    if len(parts) == 2:
                        try:
                            num1 = int(parts[0])
                            num2 = int(parts[1])
                            operator = operator_char
                            operator_found = True
                            result = None
                            if operator == "+":
                                result = add(num1, num2)
                            elif operator == "-":
                                result = subtract(num1, num2)
                            elif operator == "*":
                                result = multiply(num1, num2)
                            elif operator == "/":
                                result = divide(num1, num2)
                            if result is not None:
                                print(f"Result: {result}")
                            break
                        except ValueError:
                            print("Error: Invalid input. Please enter numbers.")
                            operator_found = True
                            break
                else:
                    print(
                        "Error: Invalid input format. Please ensure only one operator is used."
                    )
                    operator_found = True
                    break
            if not operator_found:
                print(
                    "Error: Invalid operator or format. Please use +, -, *, or / (e.g., 5+3)."
                )
        # ---calculator app---<end>#

        # ---file management app---#
        if user_input == "fileM":
            console.print(
                "[magenta]What do you want to do with files? (create, delete, etc.)>>>[/magenta]",
                end="",
            )
            file_user_input = input()
            if file_user_input == "create":
                create_file()
            elif file_user_input == "delete":
                delete_file()
            else:
                rich_print("[red]Error: Unknown file operation.[/red]")
        # ---file management app---<end>#

        # ---Isearch---#
        if user_input == "Isearch":
            Isearch_search()
        # ---Isearch---<end>#

        # ---user rename---#
        if user_input == "rename":
            Name = input("What username you want to rename to?")
            # ---save user info after rename---#
            try:
                with open("user.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                Password = lines[1].strip() if len(lines) > 1 else ""
            except FileNotFoundError:
                Password = ""
            with open("user.txt", "w", encoding="utf-8") as f:
                f.write(f"{Name}\n{Password}\n")
            # ---save user info after rename---end#
            rich_print(f"[green]Username changed to: {Name}[/green]")
        # ---user rename---<end>


        #---password change---#
        if user_input == "password change":
            new_password = input("Enter new password: ")
            # ---save user info after password change---#
            try:
                with open("user.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                Name = lines[0].strip() if len(lines) > 0 else ""
                Password = new_password
            except FileNotFoundError:
                rich_print("[red]Sorry, password change didn't work...[/red]")
            with open("user.txt", "w", encoding="utf-8") as f:
                f.write(f"{Name}\n{Password}\n")
            # ---save user info after password change---end#
            rich_print("[green]Password changed successfully.[/green]")
        # ---password change---end#

        # ---cmd mode---#
        if user_input == "cmd":
            # Enter a sub-loop for cmd mode
            while True:
                console.print("[magenta]cmd>>> [/magenta]", end="")
                cmd_input = input()
                if cmd_input == "cmd_exit":
                    break
                system(cmd_input)
        # ---cmd mode---<end>#

        # ---clear console---#
        if user_input == "clear":
            system("cls" if os_name == "nt" else "clear")
        # ---clear console---<end>#

        # ---help---#
        if user_input == "help":
            rich_print(
                """[blue]\n

fileM: opens file manager app__________.______.
                                       |      |
create:creates file using user input.<-"      |
                                              |
delete: deletes file using user input.<-------"

cal: opens calculator app______________.______.____._______.
                                       |      |    |       |
+ : addition (e.g., 5+3) <-------------"      |    |       |
- : subtraction (e.g., 10-2) <----------------"    |       |
* : multiplication (e.g., 4*7) <-------------------"       |
/ : division (e.g., 8/2) <---------------------------------"

Isearch: opens the Isearch app___________________.
                                                 |
search:  searches for files using user input.<---"

cmd___________________________________________________________.____________.______
                                                              |            |     |
opens the command line interface. [golden]|[/golden] Windows<-"            |     |
                                                                           |     |
opens the MacOS terminal. [golden]|[/golden] MacOS<----------------"     |
                                                                                 |
opens the linux terminal. [golden]|[/golden] Linux<------------------------------"



clear: clears the console

help: shows this help message

exit: exits the console

You can use the calculator by typing "cal" and then entering expressions like 5+3, 10-2, 4*7, or 8/2.
Use "fileM" to manage files (create or delete).

[/blue]"""
            )
        # ---help---<end>#

        # ---exit---#
        if user_input == "exit":
            for i in range(4):
                rich_print(
                    f"[bold yellow]Exiting the console{"." * i}{" " * (3 - i)}[/bold yellow]",
                    end="\r",
                )
                time.sleep(0.5)
            system("cls")
            break
        # ---exit---<end>#


if __name__ == "__main__":
    success, username = login()
    if success:
        system("runas /noprofile /user:Administrator cmd")
        system("cls")
        main()
