import logging
from time import gmtime, strftime
from typing import List
import psycopg2
from config.config_handler import PresetsHandler

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(message)s")


class Logger:
    params = PresetsHandler().handler["postgres"]
    HOST = params["host"]
    DB_NAME = params["db_name"]
    PORT = params["port"]
    USER = params["user"]
    PASSWORD = params["password"]

    def __init__(self, host=HOST, db_name=DB_NAME, port=PORT, user=USER, password=PASSWORD):
        self.conn = psycopg2.connect(host=host, database=db_name, port=port, user=user, password=password)
        self.c = self.conn.cursor()

        self.create_form_table()

    def create_form_table(self) -> None:
        logging.info("Creating form table...")
        self.c.execute(
            """
            CREATE TABLE IF NOT EXISTS form_table (
            id SERIAL PRIMARY KEY,
            form_time TIMESTAMP,
            form TEXT NOT NULL);
            """
        )
        self.conn.commit()
        logging.info("Logger form table creation successful")

    def add_form(self, form: str) -> None:
        with self.conn:
            self.c.execute(
                """INSERT INTO form_table
                        (id,
                        form_time,
                        form,
                        )
                VALUES (DEFAULT,%s,%s);""",
                (
                    strftime("%Y-%m-%dT%H:%M:%S", gmtime()),
                    form,
                ),
            )

    def display_all_forms(self) -> List:
        with self.conn:
            self.c.execute(
                """
                SELECT
                    id,
                    form_time,
                    form,
                FROM form_table
                ORDER BY id DESC;
                """
            )

            return self.c.fetchall()

    def display_last_form(self):
        with self.conn:
            self.c.execute(
                """
                SELECT
                    id,
                    form_time,
                    form
                FROM form_table
                ORDER BY id DESC;
                """
            )

            return self.c.fetchone()

    def __del__(self) -> None:
        self.conn.commit()
        self.c.close()
        self.conn.close()
