import os
import shutil

FOLDERS_TO_FIX = os.path.join(os.getcwd(), 'FoldersToFix')
print('Folders to Fix:', FOLDERS_TO_FIX)

# for each folder in the current directory,
for folder in os.listdir(FOLDERS_TO_FIX):
    #print('Folder:', folder)
    # if it's a folder,
    folder_path = os.path.join(FOLDERS_TO_FIX, folder)
    if os.path.isdir(folder_path):
        # for each subfolder in the folder,
        for subfolder in os.listdir(folder_path):
            #print('Subfolder:', subfolder)
            subfolder_path = os.path.join(folder_path, subfolder)
            # if the subfolder is a directory,
            if os.path.isdir(subfolder_path):
                # move the files from the subfolder to the directory and delete the subfolder;
                # if the file exist in the directory, overwrite it;
                for file in os.listdir(subfolder_path):
                    shutil.move(os.path.join(subfolder_path, file), os.path.join(folder_path, file))
                print('Files Moved.')
                os.rmdir(subfolder_path)
                print('Subfolder Deleted:', subfolder)                

        # if the folder name contains '+_+', replace it with ' - ';
        new_folder = folder.replace('+_+', ' - ')
        # if the folder name contains _ or +, replace it with spaces;
        new_folder = new_folder.replace('_', ' ').replace('+', ' ')
        # if the folder name ends with stls, remove it;
        if new_folder.endswith('stls'):
            new_folder = new_folder[:-4]
        # capitalize the first letter of each word;
        new_folder = ' '.join([word.capitalize() for word in new_folder.split()])
        # if the folder name ends with a space, remove it;
        if new_folder.endswith(' '):
            new_folder = new_folder[:-1]
        # if the folder name starts with a space, remove it;
        if new_folder.startswith(' '):
            new_folder = new_folder[1:]

        # rename the folder, if the folder already exists, add a number to the end;
        new_folder_path = os.path.join(FOLDERS_TO_FIX, new_folder)
        if (folder_path != new_folder_path) & (os.path.exists(new_folder_path)):
            i = 1
            while os.path.exists(new_folder_path + ' ' + str(i)):
                i += 1
            new_folder_path = new_folder_path + ' ' + str(i)
        os.rename(folder_path, new_folder_path)
        print('Folder Renamed: old name =', folder, ', new name =', new_folder)
