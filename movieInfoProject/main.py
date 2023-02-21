from CONSTANTS import user, password, host, port, database_name
from mysqlCtrl import MysqlCtrl

ctrl = MysqlCtrl(user, password, host, port, database_name)

result = ctrl.query("SELECT * FROM staff;")

print(result)

result = ctrl.query("DESC staff;")

print(result)

result = ctrl.execute("INSERT INTO staff VALUES ('test2', 'test2_last', 123456789);")

print(result)

result = ctrl.query("SELECT * FROM staff;")

print(result)