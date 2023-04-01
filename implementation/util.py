from CONSTANTS import user, password, host, port, sample_database_name
from mysqlCtrl import MysqlCtrl
from datetime import datetime


def isAmadefromB(A, B):
    for x in A:
        if x not in B:
            return False
    return True


def getUniqueID(table_name: str) -> int:
    ctrl = MysqlCtrl(user, password, host, port, sample_database_name)
    result = int(
        ctrl.query(
            f"SELECT item_value FROM Unique_id WHERE item_name='{table_name}';"
        ).iloc[0][0]
    )
    ctrl.execute(
        f"UPDATE Unique_id SET item_value = {result+1} WHERE item_name='{table_name}';"
    )
    return result


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    getUniqueID("Rating")
