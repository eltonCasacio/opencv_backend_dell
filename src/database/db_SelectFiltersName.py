from db import mysql


class db_SelectFiltersName():
    def Select():
        with mysql.cursor() as cur:
            cur.execute("SELECT name FROM parametersAdjustFilterImg")
            data = cur.fetchall()
            return data
