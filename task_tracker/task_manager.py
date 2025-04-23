import typer
from rich.console import Console
from rich.table import Table
from complete.storage import load_default_tasks

app = typer.Typer()

console = Console()

data = load_default_tasks()
tasks = data["default_task"]
current_tasks = data["current_tasks"]


@app.command(short_help="adds an task")
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    show()


@app.command(short_help="deletes an task by position")
def delete(position: int):
    typer.echo(f"deleting {position} task")
    show()


@app.command(short_help="updates an task by position")
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position} task")
    show()


@app.command(short_help="marks task as complete")
def complete(position: int):
    typer.echo(f"complete {position}")
    show()


@app.command(short_help="display all tasks")
def show():
    console.print("[bold magenta]Todos[/bold magenta]!", "🛠️")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=2)
    table.add_column("Task", min_width=20)
    table.add_column("Category", min_width=8, justify="right")
    table.add_column("Done", min_width=5, justify="right")

    def get_category_color(category):
        COLORS = {"Learn": "cyan", "Youtube": "red", "Sports": "cyan", "Study": "green"}
        if category in COLORS:
            return COLORS[category]
        return "white"

    for index, task in enumerate(tasks):
        category=task["category"]
        category_color = get_category_color(task["category"])
        is_done_str = "✔" if True == task["done"] else "✘"
        table.add_row(
            str(index+1),
            task["task"],
            f"[{category_color}]{category}[/{category_color}]",
            is_done_str,
        )

    console.print(table)
