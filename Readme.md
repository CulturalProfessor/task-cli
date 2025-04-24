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

delete : python3 main.py delete 1

update : python3 main.py update 1 --task "Learn php" --category "Study" --due_date "16:30 24-04-2025"

toggle : python3 main.py toggle 1

show : python3 main.py show

--help : python3 main.py --help

command screenshots are present in assets folder