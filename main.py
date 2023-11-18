import os
from uuid import uuid1

DIR = os.getcwd()

path = os.path.join(DIR, 'asd.md')
print(os.path.exists(path))


# import os
# from uuid import uuid1

# DIR = os.getcwd()
# print("Current directory: ", DIR)

# directory = uuid1()

# path = os.path.join(DIR, str(directory))

# os.mkdir(path)


# import os
# path = "D:/"
# dir_list = os.listdir(path)
# print(f"""List of dirs: 
# {dir_list}
# """)

# create_folder_path = os.path.join(path, 'H')
# os.removedirs(create_folder_path)