from CONSTANTS import user, password, host, port, sample_database_name, TABLES
from mysqlCtrl import MysqlCtrl
import pandas as pd

ctrl = MysqlCtrl(user, password, host, port, sample_database_name)

for x in TABLES:
    result = ctrl.query(f"SELECT * FROM {x};")

    print(len(pd.DataFrame(result)))