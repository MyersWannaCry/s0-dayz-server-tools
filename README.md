# S0's DayZ Server Tools
A pack of DayZ server tools, helping you manage your server mods and their keys automatically. It also helps you create a simple and quick modlist and set your mods priority up properly, evading mod load conflicts and batch file crashes. The program also automatically moves keys from all of your installed mods into a folder, so the only thing you have to do after that is copying this folder to your server directory. 
**Don't forget about the default dayz.bikey!**
# How to use S0's DayZ Server Tools
The repository holds an existing modlist and mod priority, just as an example. After you set your server directory in *config.txt* and run *modlist_creator.py*, *modlist.txt* will serve as an output for program's execution. Put the output straight into your batch file and feel free to start your server.
Running *key_mover.py* will automatically move all your mod keys straight into *keys* folder in script's directory.
# Requirements
OS, Shutil