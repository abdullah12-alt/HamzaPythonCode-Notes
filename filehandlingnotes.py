import os 



# with open("hello.txt","r") as f:
#     file=f.readlines()
#     print(file[4:8])
#     f.close()

# content="Hello this is a python code ,we are learning file handling right now"
# with open("hello.txt",'w+') as f:
#     f.write(content)
#     f.seek(0)
#     file=f.read()
#     print(file)


content="\nHello this is a cpp code ,we are learning file handling right now"
with open("hello.txt",'a+') as f:
    f.write(content)
    f.seek(0)
    file=f.read()
    print(file)

