import typer

from rich import print
from typing import Annotated

from pylib.DatabaseHelper import DatabaseHelper
from pylib.YAMLConfigHelper import YAMLConfigHelper


set = typer.Typer()


class SetCommandHelper:
    def __init__(self, **dbconfig):
        self._dbh = DatabaseHelper(**dbconfig)
        self.set = set

    @staticmethod
    @set.command("--set-default-instance")
    def set_default_instance(
        self, instance: Annotated[str, typer.Argument(prompt=True)]
    ):
        print(f"Setting default instance to {instance}.")

        pxcfg = YAMLConfigHelper.load()
        pxcfg.set_default_instance(instance)

    @staticmethod
    @set.command("--set-admin-variable")
    def set_admin_variable(
        self,
        variable_name: Annotated[str, typer.Argument()],
        variable_value: Annotated[str, typer.Argument()],
    ):
        print(f"Setting {variable_name} to {variable_value}.")

        self._dbh.set_admin_variable(variable_name, variable_value)
