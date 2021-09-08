import os
import os.path
import pathlib
import platform

#(Root Directory) Bright Green \u001b[32;1m
#(Current Directory unless root dir) Yellow \u001b[33m
#(Folder Color) Bright Blue \u001b[34;1m
#(Normal Files) White \u001b[37m
#(Audio/Video/Image Files) Bright Magenta \u001b[35;1m
#(Reset Colors) \u001b[0m

directorytab = '';
plt = platform.system(); #Determines what os you're on to use the correct directory seperator
ogdirectory = str(pathlib.Path().resolve());
ogDirIter = ogdirectory; 
directoryFiles = os.listdir(ogdirectory);

if plt == "Windows":
    splitDirectory = ogdirectory.split('\\');
else:
    splitDirectory = ogdirectory.split('/');

splitDirectory = splitDirectory[1:]; #Takes off the blank directory aka first '/'
count = 0;
modOgDir = ogdirectory.rindex('/');
for i in splitDirectory:
    if os.path.isdir(ogdirectory) == True:
       print(directorytab,'\u001b[34;1m--|', i , '\u001b[0m');
       directorytab += '    ';
       for j in range(len(directoryFiles)):
           print(directorytab,'|-',directoryFiles[j]);
#NO CLUE WHAT TO DO RN
