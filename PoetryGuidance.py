# Terminal: pip install poetry==1.4.2
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
