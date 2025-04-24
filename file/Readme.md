Task Tracker CLI

Avalable commands :
add : adds an task
delete : deletes an task by position
update : updates an task by position
toggle : Toggles tasks status
show : display all tasks


Getting Started:
Prerequisites:

Python 3.7+ , typer, rich

Install dependencies:
pip install typer rich


Examples :

add : python3 main.py add "Learn python" "Study"
delete : python3 main.py delete 1
update : python3 main.py update 1 --task "Learn php" --category "Study"
toggle : python3 main.py toggle 1
show : python3 main.py show
