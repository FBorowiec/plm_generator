# pylint: disable=too-many-locals
import unittest
import testing.postgresql
from freezegun import freeze_time
from logger.logger import Logger


class LoggerTest(unittest.TestCase):
    @freeze_time("2022-02-25 12:00:01")
    def test_logger(self):
        with testing.postgresql.Postgresql() as postgresql:
            psql = postgresql.dsn()
            db = Logger(
                host=psql["host"], db_name=psql["database"], port=psql["port"], user=psql["user"], password="postgres"
            )

            form = "test_form"

            db.add_form(form)

            values = db.display_all_forms()

            expected_values = [()]

        self.assertEqual(values, expected_values)
