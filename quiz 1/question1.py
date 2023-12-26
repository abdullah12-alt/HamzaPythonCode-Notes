import os
# f= open("new_data.txt",'r')
# content=f.read()
# print(content)

content="""Hello, Python!
This is a quiz on file handling and OS functions.
"""
if os.path.exists("new_data.txt"):
    print("File 'new_data.txt' exists")
else:
    f=open("new_data.txt","w")
    f.write(content)
    print("new_data.txt is created")

