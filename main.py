import os
import importlib.util
import time
import ast

# Define ANSI escape codes for text colors
class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def list_projects():
    """List all files in the 'projects' folder."""
    projects_dir = 'projects'
    if not os.path.exists(projects_dir) or not os.path.isdir(projects_dir):
        print(colors.RED + "Error: 'projects' folder not found." + colors.RESET)
        return []

    files = os.listdir(projects_dir)
    return [f for f in files if os.path.isfile(os.path.join(projects_dir, f))]

def choose_project(projects):
    """Let the user choose a project from the list."""
    print("Select a project to run:")
    for i, project in enumerate(projects, 1):
        print(f"{colors.YELLOW}{i}. {project}{colors.RESET}")
    print(f"{colors.YELLOW}0. Cancel{colors.RESET}")

    choice = input("Enter the number of the project (0 to cancel): ")
    try:
        choice = int(choice)
        if choice == 0:
            return None
        elif 1 <= choice <= len(projects):
            return projects[choice - 1]
        else:
            print(f"{colors.RED}Invalid choice. Please enter a number between 0 and {len(projects)}{colors.RESET}")
            return choose_project(projects)
    except ValueError:
        print(f"{colors.RED}Invalid choice. Please enter a number.{colors.RESET}")
        return choose_project(projects)

def import_module(module_name):
    """Import a module dynamically if not already imported."""
    if module_name not in globals():
        try:
            globals()[module_name] = importlib.import_module(module_name)
            print(f"{colors.GREEN}Module '{module_name}' imported successfully.{colors.RESET}")
        except ImportError:
            print(f"{colors.RED}Module '{module_name}' not found.{colors.RESET}")
            return False
    return True

def import_dependencies(script_path):
    """Import all dependencies of the given script."""
    with open(script_path, 'r') as f:
        tree = ast.parse(f.read(), filename=script_path)

    imports = [node.names[0].name for node in tree.body if isinstance(node, ast.Import) for alias in node.names]
    for node in tree.body:
        if isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    if imports:
        for module_name in imports:
            import_module(module_name)
    else:
        print(f"{colors.YELLOW}No modules to import found in the script.{colors.RESET}")

def main():
    while True:
        projects = list_projects()
        if not projects:
            print(f"{colors.RED}No projects found in the 'projects' folder.{colors.RESET}")
            return

        chosen_project = choose_project(projects)
        if chosen_project is None:
            print("Selection canceled.")
            return

        print(f"{colors.GREEN}You chose: {chosen_project}{colors.RESET}")

        # Import dependencies of the chosen script
        script_path = os.path.join('projects', chosen_project)
        import_dependencies(script_path)

        # Import and run the chosen script
        try:
            chosen_module_name = os.path.splitext(chosen_project)[0]
            if not import_module(chosen_module_name):
                time.sleep(2)
                continue
            chosen_module = globals()[chosen_module_name]
            chosen_module.main()  # Assuming each script has a main() function
        except Exception as e:
            print(f"{colors.RED}Error importing and running the chosen script: {e}{colors.RESET}")
            time.sleep(5)  # Wait for 5 seconds
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

if __name__ == "__main__":
    main()
