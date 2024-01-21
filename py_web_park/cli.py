import typer
from py_web_park import enums
from py_web_park import app_maker


app = typer.Typer()


@app.callback()
def callback():
    """
    Web Park manager
    """


@app.command()
def create_app(
    name: str,
    kind: enums.AppKind = typer.Option(
        enums.AppKind.FLASK, help="The kind of app to make"
    ),
):
    """
    Creating app
    """
    typer.echo(f"Creating app {name} with {kind}")
    app_maker.create_app(name, python_version="3.11", app_kind=kind)


@app.command()
def launch_app(name: str):
    """
    Launch app from park
    """
    typer.echo(f"Launching {name}")
