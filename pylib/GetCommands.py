import typer
from rich import print
from rich.console import Console
from rich.table import Table
from pylib.DatabaseHelper import DatabaseHelper
from pylib.YAMLConfigHelper import YAMLConfigHelper


app = typer.Typer()
console = Console()


class GetCommandHelper:
    def __init__(self, **dbconfig):
        self._dbh = DatabaseHelper(**dbconfig)
        self.app = app

    @app.command()
    def set_default_instance(self, instance: str = typer.Argument("", "--set-default-instance")):
        print(f"Setting default instance to {instance}.")

        pxcfg = YAMLConfigHelper().load()
        pxcfg.set_default_instance(instance)

    @app.command()
    def get_admin_users(self, full: bool = typer.Option(False, "--full")):
        print("Getting admin users with credentials.")

        sql = "SELECT variable_value FROM global_variables where variable_name = 'admin-admin_credentials'"
        self._dbh.execute(sql)
        users = self._dbh.fetchone()

        table = Table("Username", show_lines=True)

        if full:
            table.add_column("Password")
            if ";" in users[0]:
                users = users[0].split(";")
                for user in users:
                    up = user.split(":")
                    table.add_row(up[0], up[1])
            else:
                up = users[0].split(":")
                table.add_row(up[0], up[1])
        else:
            if ";" in users[0]:
                users = users[0].split(";")
                for user in users:
                    up = user.split(":")
                    table.add_row(up[0])
            else:
                up = users[0].split(":")
                table.add_row(up[0])

        console.print(table)

    @app.command()
    def get_mysql_servers(self):
        print("Getting MySQL servers.")

        sql = "SELECT * FROM mysql_servers ORDER BY hostgroup_id, hostname ASC"
        self._dbh.execute(sql)
        servers = self._dbh.fetchall()

        table = Table(
            "Hostgroup",
            "Hostname",
            "Port",
            "Status",
            "Weight",
            "Compression",
            "Max_connections",
            "Max_replication_lag",
            "Use_ssl",
            "Max_latency_ms",
            show_lines=True,
        )
        for server in servers:
            table.add_row(
                server[0],
                server[1],
                server[2],
                server[3],
                server[4],
                server[5],
                server[6],
                server[7],
                server[8],
                server[9],
            )

        console.print(table)
        print()

    @app.command()
    def get_proxysql_servers(self):
        print("Getting ProxySQL servers.")
        print()

        sql = "SELECT * FROM proxysql_servers ORDER BY hostname ASC"
        self._dbh.execute(sql)
        servers = self._dbh.fetchall()

        table = Table("Hostname", "Port", "Weight", "Comment")
        for server in servers:
            table.add_row(server[0], server[1], server[2], server[3])

        console.print(table)
        print()
