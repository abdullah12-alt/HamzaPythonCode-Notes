# import os

# def list_display():
#     currect_dir=os.getcwd()
#     item=os.listdir(currect_dir)
#     for i in item:
#         full_path=os.path.join(currect_dir,i)
#         print(full_path)
# list_display()
# [exersise.py,abdullah,hassan]
import sys

if len(sys.argv)==4:
    a=sys.argv[0]
    file_name=sys.argv[1]
    first_name=sys.argv[2]
    last_name=sys.argv[3]
    print(f"Welcome back to the Python classes {first_name}{last_name} {a}")
else:
    print("ex.py <file name> <firstname> <last name>")
