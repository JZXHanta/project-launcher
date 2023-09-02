import typer
from rich import print
from rich.console import Console
from rich.table import Table
import os
import subprocess

console = Console()


# Welcome Banner
def welcome():
    print("Welcome to Project_Launcher!")
    print("\nSelect a number to scaffold a new project to create")
    

# Table to display project options
def main_menu_table():
    table = Table("", "Language", "Pkg mgr")
    table.add_row("1", "Python", "--")
    table.add_row("2", "Go", "--")
    table.add_row("3", "React/JS (not working...)", "npm")
    table.add_row("4", "React/TS (not working...)", "npm")
    console.print(table)


# Input to select from list
def select_from_table():
    selection = typer.prompt("enter a number (1-4)")
    language = ""
    if selection == "1" or selection == "2" or selection == "3" or selection == "4":
        if selection == "1":
            language = "Python"
        elif selection == "2":
            language = "Go"
        elif selection == "3":
            language = "React/JS"
        elif selection == "4":
            language = "React/TS"
        print(f"You have selected {language}")
        return language
    else:
        raise Exception("Invalid selection, please try again")
        select_from_table()


# Clears screen between function calls
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
        

# Creates python file corresponding to chosen project name
def init_python(project_name):
    os.mknod(f"{project_name}.py")
    print(f"[green]{project_name}.py[/green] has been created.")

# Created go.mod and go file corresponding to chosen project name
def init_go(project_name):
    os.system(f"go mod init {project_name}")
    os.system(f"touch {project_name}.go")
    print(f"Both go.mod and [green]{project_name}.go[/green] have been created")
    

# Creates react/js project using vite and installs npm modules
# TODO cd/npm i not working properly
def init_react_js(project_name):
    os.sysconftem(f"npm create vite@latest {project_name} -- --template react")
    os.system(f"cd {project_name}")
    subprocess.run(['npm', 'i'])
    clear()
    print(f"\f\n\n  [green]{project_name}[/green] folder has been created and all node dependencies have been installed for you.\n\n  To start the dev server:\n      'cd {project_name}'\n      'npm run dev'\n\n  [blue]Happy Coding![/blue]\n")


# Creates react/ts project using vite and installs npm modules
# TODO cd/npm i not working properly
def init_react_ts(project_name):
    os.system(f"npm create vite@latest {project_name} -- --template react-ts")
    os.system(f"cd {project_name}")
    subprocess.run(['npm', 'i'])
    clear()
    print(f"\f\n\n  [green]{project_name}[/green] folder has been created and all node dependencies have been installed for you.\n\n  To start the dev server:\n      'cd {project_name}'\n      'npm run dev'\n\n  [blue]Happy Coding![/blue]\n")    


# Creates new directory corresponding to chosen project name and changes directory (not for use with functions that use npm for install)
def mkdir_cd(project_name):
    os.mkdir(f"{project_name}")
    os.chdir(f"{project_name}")
    
# Calls init functions for corresponding projects
# TODO create option to use alternate directory 
def init_location():
    language = select_from_table()
    cwd = os.getcwd()
    project_name = get_project_name().lower()
    print(f"Do you wish to initialize this project in the current directory? [green]({cwd})[/green]")
    selection = typer.prompt("yes/no (y/n):")
    if selection == "yes" or selection == "y":
        if language == "Python":
            mkdir_cd(project_name)
            init_python(project_name)
        elif language == "Go":
            mkdir_cd(project_name)
            init_go(project_name)
        elif language == "React/JS": 
            init_react_js(project_name)
        elif language == "React/TS":
            init_react_ts(project_name)
    else:
        return "Bye, have a beautiful time"

# User input for project name
def get_project_name():
    return typer.prompt("Enter a project name")            
    
        
def main():
    welcome()
    main_menu_table()
    init_location()


    
if __name__ == "__main__":
    typer.run(main)