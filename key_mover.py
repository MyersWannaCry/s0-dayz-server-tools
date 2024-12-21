import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
key_folder_path = f'{script_dir}\\keys'
config_path = os.path.join(script_dir, 'config.txt')

#Getting server path from config
with open(config_path, "r") as file:
    try:
        server_path = file.readline()
    except Exception as E:
        print(f"Error while getting server path from config: {E}")
    file.close()
dirs_in_server = os.listdir(server_path)

moddirs = []
counter = 0
for dir in dirs_in_server:
    if dir[0] == "@":
        moddirs.append(dir)
for dir in moddirs:
    try:
        key_path = os.listdir(f'{server_path}\\{dir}\\Keys')
        key = f'{server_path}\\{dir}\\Keys\\{key_path[0]}'
        shutil.copy(key, key_folder_path)
        print(f"Moved {key} to key folder from {dir}")
        counter+=1
    except FileNotFoundError as e:
        key_path = os.listdir(f'{server_path}\\{dir}\\Key')
        key = f'{server_path}\\{dir}\\Key\\{key_path[0]}'
        shutil.copy(key, key_folder_path)
        print(f"Moved {key} to key folder from {dir}")
        counter+=1
print(f"Moved {counter} files in total from {len(moddirs)} mod dirs.")
