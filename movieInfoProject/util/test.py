from CONSTANTS import app_name
from functionalities import Functionalities

func_ctrl = Functionalities()

print(func_ctrl.count_entries("Movie"))
print(isinstance(func_ctrl.count_entries("Movie"), int))
print(type(func_ctrl.count_entries("Movie")))