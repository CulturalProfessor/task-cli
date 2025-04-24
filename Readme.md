Task Tracker CLI

Avalable commands :
add : adds an task
delete : deletes an task by position
update : updates an task by position
toggle : Toggles tasks status
show : display all tasks
--help : provides description regarding commands

Getting Started:
Prerequisites:

Python 3.7+ , typer, rich

Install dependencies:
pip install typer rich

Examples :

add : python3 main.py add "Learn python" "Study" --due_date "15:30 24-04-2025"
![CLI Screenshot](https://github.com/CulturalProfessor/task-cli/blob/main/assets/Screenshot%20from%202025-04-24%2016-32-34.png)

delete : python3 main.py delete 1
![CLI Screenshot](https://github.com/CulturalProfessor/task-cli/blob/main/assets/Screenshot%20from%202025-04-24%2016-33-05.png)

update : python3 main.py update 1 --task "Learn php" --category "Study" --due_date "16:30 24-04-2025"
![CLI Screenshot](https://github.com/CulturalProfessor/task-cli/blob/main/assets/Screenshot%20from%202025-04-24%2016-33-32.png)

toggle : python3 main.py toggle 1
![CLI Screenshot](https://github.com/CulturalProfessor/task-cli/blob/main/assets/Screenshot%20from%202025-04-24%2016-34-00.png)

show : python3 main.py show
![CLI Screenshot](https://github.com/CulturalProfessor/task-cli/blob/main/assets/Screenshot%20from%202025-04-24%2016-34-17.png)

--help : python3 main.py --help
![CLI Screenshot](https://github.com/CulturalProfessor/task-cli/blob/main/assets/Screenshot%20from%202025-04-24%2016-34-40.png)
command screenshots are present in assets folder
