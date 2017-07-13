import sqlite3


conn = sqlite3.connect('core.example.db')


class DBMan(object):

    def __init__(self):
        self.version = '0.1'

    @staticmethod
    def create_default_tables(self):
        c = conn.cursor()

        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS test_plans (
  plan_id     INTEGER PRIMARY KEY,
  name        TEXT,
  description TEXT,
  owner       TEXT,
  version     REAL
);''')

        conn.commit()

        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS test_suites (
  suite_id    INTEGER PRIMARY KEY,
  name        TEXT,
  description TEXT,
  planid      INTEGER NOT NULL,
  FOREIGN KEY (planid) REFERENCES testplans (plan_id)
);''')
        conn.commit()

        c.execute('''CREATE TABLE IF NOT EXISTS systems_under_test (
  sut_id      INTEGER PRIMARY KEY,
  name        TEXT,
  description TEXT,
  sut_type    TEXT /*app, device, cloud*/,
  sutid       INTEGER NOT NULL,
  FOREIGN KEY (sutid) REFERENCES testsuites (suite_id)
);''')
        conn.close()

