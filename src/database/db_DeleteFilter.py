from db import mysql


class db_DeleteFilter():
    def Delete(name):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM parametersAdjustFilterImg WHERE name=%s", name)
