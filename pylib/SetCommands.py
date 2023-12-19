import typer
from rich import print
from pylib.DatabaseHelper import DatabaseHelper
from pylib.YAMLConfigHelper import YAMLConfigHelper


app = typer.Typer()


class SetCommandHelper:
    def __init__(self, **dbconfig):
        self._dbh = DatabaseHelper(**dbconfig)
        self.app = app

    @app.command()
    def set_default_instance(
        self, instance: str = typer.Argument("", "--set-default-instance")
    ):
        print(f"Setting default instance to {instance}.")

        pxcfg = YAMLConfigHelper.load()
        pxcfg.set_default_instance(instance)