import pymysql


class DatabaseHelper:
    def __init__(self, **dbconfig):
        self._cxn = pymysql.connect(
            host=dbconfig["host"],
            user=dbconfig["user"],
            password=dbconfig["password"],
            db=dbconfig["db"],
        )
        self._cur = self._cxn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cxn.close()

    @property
    def connection(self):
        return self._cxn

    @property
    def cursor(self):
        return self._cur

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
