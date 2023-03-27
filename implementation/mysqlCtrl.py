from sqlalchemy import create_engine
import pandas as pd

class MysqlCtrl:

    def __init__(self, user, password, host, port, database_name):
        self.engine = create_engine(f'mysql://{user}:{password}@{host}:{port}/{database_name}')

    # def execute(self, sql_stmt):
    #     with self.engine.connect() as connection:
    #         connection.execution_options(isolation_level="AUTOCOMMIT")
    #         connection.execute(sql_stmt)

    def query(self, sql_stmt):
        # print(sql_stmt)
        with self.engine.connect() as connection:
            connection.execution_options(isolation_level="AUTOCOMMIT")
            result = connection.execute(sql_stmt)
        return pd.DataFrame(result.fetchall())

if __name__ == "__main__":
    from CONSTANTS import user, password, host, port, sample_database_name
    sqlctrl = MysqlCtrl(user, password, host, port, sample_database_name)
    result = sqlctrl.query("SELECT * FROM Movie Limit 5;")
    print(result)