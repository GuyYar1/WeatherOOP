# A   Let's create a concise step-by-step guide for starting a new Python project using Poetry, including the `poetry init` command:
#
# 1. **Install Poetry (if not already done):**
#    - If you haven't installed Poetry yet, open your terminal and run:
#      ```
#      pip install poetry
#      ```
#
# 2. **Create a New Project:**
#    - Open your terminal and navigate to the desired directory where you want to create your project.
#    - Run the following command to create a new project (replace `my-package` with your preferred project name):
#      ```
#      poetry new my-package
#      ```
#    - This will create a basic project structure with a `pyproject.toml` file, a `README.md`, and some initial Python files.
#
# 3. **Navigate to Your Project Folder:**
#    - Change into your project folder:
#      ```
#      cd my-package
#      ```
#
# 4. **Edit `pyproject.toml`:**
#    - Open the `pyproject.toml` file in a text editor.
#    - Add your project dependencies under the `[tool.poetry.dependencies]` section. For example:
#      ```
#      [tool.poetry.dependencies]
#      python = "^3.8"
#      requests = "^2.26.0"
#      ```
#
# 5. **Install Dependencies:**
#    - Run the following command to install the dependencies listed in `pyproject.toml`:
#      ```
#      poetry install
#      ```
#
# 6. **Write Your Code:**
#    - Create your Python files in the appropriate directories (`my_package` or `src/my_package` if you chose the `--src` option).
#    - Start writing your code!
#
# 7. **Run Your Project:**
#    - To run your project, use:
#      ```
#      poetry run python my_package/main.py
#      ```
#    - Replace `my_package/main.py` with the actual path to your main Python file.
#
# Remember to adjust the project name, dependencies, and other details according to your specific requirements. If you encounter any issues or need further assistance, feel free to ask! 😊🚀

# B  error:
# module 'virtualenv.create.via_global_ref.builtin.cpython.mac_os' has no attribute 'CPython2macOsArmFramework'
# PS C:\Users\DELL\Documents\GitHub\WeatherOOP> python -m venv venv
# PS C:\Users\DELL\Documents\GitHub\WeatherOOP> venv\Scripts\activate
# (venv) PS C:\Users\DELL\Documents\GitHub\WeatherOOP> pip install --require-hashes -r requirements.txt
# Install all if there issues you may: remove  but first ask chatgpt.
# (venv) PS C:\Users\DELL\Documents\GitHub\WeatherOOP> poetry shell
# Spawning shell within C:\Users\DELL\Documents\GitHub\WeatherOOP\venv
# Windows PowerShell
# Copyright (C) Microsoft Corporation. All rights reserved.
#
# Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows
#
# (venv) PS C:\Users\DELL\Documents\GitHub\WeatherOOP>



#  C   While the poetry export command is commonly used to generate a requirements.txt file, there are other useful commands in Poetry. Here are a few:
#
# poetry new: Creates a new Python project with a suitable directory structure. You can customize the project name and choose whether to use the src layout:
# poetry new my-package
# poetry new --src my-package
#
# poetry init: Interactively creates a pyproject.toml file by prompting you for basic package information (name, description, author, etc.):
# poetry init
#
# poetry install: Reads the pyproject.toml file, resolves dependencies, and installs them. If a poetry.lock file exists, it uses exact versions from there:
# poetry install

# D   Error
# Especially on Windows, self add and self remove may be problematic so that other methods should be preferred.

# E   --PART
# Terminal: pip install poetry==1.4.2

# pip install --require-hashes -r requirements.txt
#
# Python version using:
# python --version
#
# Update Poetry: Ensure you have the latest version of Poetry installed. Run:
# pip install --upgrade poetry
#
# Virtual Environment: Activate the virtual environment created by Poetry:
# poetry shell
# reate a new virtual environment
# python -m venv venv

# poetry init     # click on all enter and at the end YES approve config
# poetry self update
# create the main with the init function
# yet not import moduls or packs
# poetry install   # after that there are file: toml and lock
# poetry --version
# poetry env list  can remove it if needed.

#source:
# https://www.twilio.com/en-us/blog/introduction-python-dependency-management-poetry-package


#C:\Users\DELL\Documents\GitHub>where poetry
# C:\Python311\Scripts\poetry.exe


# pip and poetry are 2 separate mechanize
# poetry add streamlit is basically install it on the shell environment and also update the lock and toml files.
# There is option to use install and then use  poetry lock --no-update,
# but it didn't work
# just use this poetry add modulename
# by that it will import and update the poetry files

# dont forget to export the requirments before commit and after the verification that all modules that were added are in the poetry files.
# if not do  so and then use the export command as followed, The command:
# poetry export -f requirements.txt -o requirements.txt

#
# ertainly! Let’s walk through the steps to create a new Python project in PyCharm and set up Poetry for dependency management:
#
# Install Poetry:
# Open Terminal (on macOS and Linux) or PowerShell (on Windows).
# Execute the following command to install Poetry:
# curl -sSL [^1^][4] | python3 -
#
# Verify the installation by running:
# poetry --version
#
# Create a New Project in PyCharm:
# Open PyCharm.
# Click “Create New Project” on the welcome screen.
# Choose a location and name for your project.
# Select the Python interpreter you want to use (install Python directly from PyCharm if needed).
# Click “Create” to finish.
# Configure Poetry Environment in PyCharm:
# Click the Python Interpreter selector (or press Ctrl + Alt + S).
# Go to Project: <project name> | Python Interpreter.
# Click “Add Interpreter” next to the list of available interpreters.
# Select “Poetry Environment.”
# Choose the base interpreter and decide whether to install packages from pyproject.toml.
# If PyCharm doesn’t detect the poetry executable, specify its path (e.g., /Users/username/Library/Application Support/pypoetry/venv/bin/poetry on macOS).