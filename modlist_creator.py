import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'modlist.txt')
config_path = os.path.join(script_dir, 'config.txt')
priority_path = os.path.join(script_dir, 'modlist_priority.txt')
moddirs = []
priority_dict = {}

#Getting server path from config
with open(config_path, "r") as file:
    try:
        path_to_server = file.readline()
        print(path_to_server)
    except Exception as E:
        print(f"Error while getting server path from config: {E}")
    file.close()
dirs_in_server = os.listdir(path_to_server)

def rename_dir(elem):
    '''Renames file in server directory if it has blank space'''
    dir_index = dirs_in_server.index(elem)
    new_dirname = elem.replace(" ", "")
    os.rename(f"{path_to_server}\\{elem}", f"{path_to_server}\\{new_dirname}")
    print(f"Renamed {elem} to {new_dirname}.")
    dirs_in_server[dir_index] = new_dirname

def get_modlist():
    '''Getts an old modlist from modlist.txt and compares them to new mods'''
    different_elems = []
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            try:
                old_modlist = [line.replace(';', '').replace('^', '').strip() for line in lines]
            except Exception as E:
                print(f"Error in reading old modlist:\n {E}")
            file.close()
    except:
        print("File reading error.")
    for elem in moddirs:
        if elem not in old_modlist:
            different_elems.append(elem)
    if len(different_elems) > 0:
        print(f"New mods:\n{different_elems}")
    else:
        print("No new mods found.")

def sort_modlist():
    '''Sorts the modlist, considering modlist priority'''
    with open(priority_path, "r") as priority_file:
        for i, line in enumerate(priority_file):
            filename = line.strip()
            priority_dict[filename] = i
    priority_file.close()
    sorted_file_list = sorted(moddirs, key=lambda x: priority_dict.get(x, float('inf')))
    return sorted_file_list

def write_modlist_file():
    '''Wtrites sorted modlist into a file'''
    sorted_modlist = sort_modlist()
    try:
        with open(file_path, "w") as file:
            for dir in sorted_modlist:
                file.write(f"{dir};^\n")
            file.close()
    except:
        print("File writing error.")


for dir in dirs_in_server:
    if " " in dir:
        rename_dir(dir)

    if dir[0] == "@":
        moddirs.append(dir)


get_modlist()
write_modlist_file()