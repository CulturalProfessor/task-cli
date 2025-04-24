from datetime import datetime
import typer
from rich.console import Console
from rich.table import Table
from complete.storage import (
    load_default_tasks,
    add_task,
    delete_task,
    update_task,
    toggle_task,
    sort_tasks_by_due_date,
)

app = typer.Typer()

console = Console()


@app.command(short_help="adds an task")
def add(
    task: str,
    category: str,
    due_date: str = typer.Option(
        None, "--due_date", help="Due date and time (HH:MM DD-MM-YYYY)"
    ),
):
    typer.echo(f"adding {task}, {category}")
    add_task(task=task, category=category, due_date=due_date)
    show()


@app.command(short_help="deletes an task by position")
def delete(position: int):
    typer.echo(f"deleting task at {position} position")
    delete_task(position=position)
    show()


@app.command(short_help="updates an task by position")
def update(
    position: int,
    task: str = None,
    category: str = None,
    due_date: str = typer.Option(
        None, "--due_date", help="Due date and time (HH:MM DD-MM-YYYY)"
    ),
):
    typer.echo(f"updating {position} task")
    update_task(position=position, task=task, category=category, due_date=due_date)
    show()


@app.command(short_help="Toggles tasks status")
def toggle(position: int):
    typer.echo(f"Toggling {position} position task")
    toggle_task(position=position)
    show()


@app.command(short_help="display all tasks")
def show():
    console.print("[bold magenta]Todos[/bold magenta]!")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=2)
    table.add_column("Task", min_width=20)
    table.add_column("Category", min_width=8, justify="right")
    table.add_column("Due Date", min_width=8, justify="right")
    table.add_column("Done", min_width=5, justify="right")

    def get_category_color(category):
        COLORS = {
            "learn": "cyan",
            "youtube": "red",
            "sports": "yellow",
            "study": "green",
            "work": "blue",
            "personal": "bright_yellow",
            "health": "magenta",
            "shopping": "brown",
            "tech": "bright_blue",
        }
        if category.lower() in COLORS:
            return COLORS[category.lower()]
        return "white"

    data = load_default_tasks()
    tasks = sort_tasks_by_due_date(tasks=data["default_tasks"])

    for index, task in enumerate(tasks):
        category = task["category"]
        category_color = get_category_color(task["category"])
        is_done_str = "✔" if True == task["done"] else "✘"
        table.add_row(
            str(index + 1),
            task["task"],
            f"[{category_color}]{category}[/{category_color}]",
            task["due_date"],
            is_done_str,
        )

    console.print(table)
