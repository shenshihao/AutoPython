import os

path = 'C:/Users/user/Downloads/python/'
for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))
