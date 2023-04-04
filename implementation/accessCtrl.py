from CONSTANTS import user, password, host, port, sample_database_name
from mysqlCtrl import MysqlCtrl

class Access:
    ctrl = MysqlCtrl(user, password, host, port, sample_database_name)

    def try_lock_S(self, person_id: int, table_name: str) -> bool:
        result = self.ctrl.query(f"SELECT person_id, operation FROM Access WHERE table_name = '{table_name}';")
        if len(result) == 0:
            self.ctrl.execute(f"INSERT INTO Access Values ({person_id}, '{table_name}', 'read');")
            return True
        elif person_id in result['person_id'].to_list():
            return False
        elif "write" in result['operation'].to_list():
            return False
        else:
            self.ctrl.execute(f"INSERT INTO Access Values ({person_id}, '{table_name}', 'read');")
            return True
    
    def try_unlock_S(self, person_id: int, table_name: str) -> bool:
        result = self.ctrl.query(f"SELECT person_id, operation FROM Access WHERE table_name = '{table_name}' AND person_id = {person_id} AND operation = 'read';")
        if len(result) == 0:
            return False
        else:
            self.ctrl.execute(f"DELETE FROM Access WHERE table_name = '{table_name}' And person_id = {person_id} AND operation = 'read';")
            return True
    
    def try_lock_X(self, person_id: int, table_name: str) -> bool:
        result = self.ctrl.query(f"SELECT person_id, operation FROM Access WHERE table_name = '{table_name}';")
        if len(result) == 0:
            self.ctrl.execute(f"INSERT INTO Access Values ({person_id}, '{table_name}', 'write');")
            return True
        else:
            return False
    
    def try_unlock_X(self, person_id: int, table_name: str) -> bool:
        result = self.ctrl.query(f"SELECT person_id, operation FROM Access WHERE table_name = '{table_name}' AND person_id = {person_id} AND operation = 'write';")
        if len(result) == 0:
            return False
        else:
            self.ctrl.execute(f"DELETE FROM Access WHERE table_name = '{table_name}' And person_id = {person_id} AND operation = 'write';")
            return True