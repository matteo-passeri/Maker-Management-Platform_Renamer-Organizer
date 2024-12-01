import os
import shutil


FOLDERS_TO_FIX = os.path.join(os.getcwd(), 'FoldersToFix')
print('Folders to Fix:', FOLDERS_TO_FIX)

# For each folder in the current directory,
for folder in os.listdir(FOLDERS_TO_FIX):
    # if it's a folder,
    folder_path = os.path.join(FOLDERS_TO_FIX, folder)
    if os.path.isdir(folder_path):
        # for each file in the folder, move it to the parent directory;
        for dirpath, _, filenames in os.walk(folder_path, topdown=False):            
            for filename in filenames:
                i = 0
                source = os.path.join(dirpath, filename)
                target = os.path.join(folder_path, filename)

                # If the file already exists in the target directory, but is not the same file, add a number to the end;
                if target != source:
                    while os.path.exists(target):
                        i += 1
                        file_parts = os.path.splitext(os.path.basename(filename))

                        target = os.path.join(
                            folder_path,
                            file_parts[0] + "_" + str(i) + file_parts[1],
                        )

                shutil.move(source, target)

                print("Moved ", source, " to ", target)

            # Delete the empty directories if they are not the folder itself;
            if dirpath != folder_path:
                os.rmdir(dirpath)

                print("Deleted ", dirpath)
        
        # If the folder name contains '+_+', replace it with ' - ';
        new_folder = folder.replace('+_+', ' - ')
        # Temporally replace ' - ' with a symbol that is rarely use; to be able to distinguish "-" from " - ";
        new_folder = new_folder.replace(' - ', ' § ')    
        # then replace '-' with a space    
        new_folder = new_folder.replace('-', ' ')
        # and replace it back
        new_folder = new_folder.replace(' § ', ' - ')
        # If the folder name contains _ or +, replace it with spaces;
        new_folder = new_folder.replace('_', ' ').replace('+', ' ')
        # If the folder name ends with stls, remove it;
        if new_folder.endswith('stls'):
            new_folder = new_folder[:-4]
        # Capitalize the first letter of each word;
        new_folder = ' '.join([word.capitalize() for word in new_folder.split()])
        # If the folder name ends with 'model Files' or 'print Files', remove it;
        if new_folder.endswith(('model Files', 'print Files')):
            new_folder = new_folder[:-11]
        # If the folder name ends with a space, remove it;
        if new_folder.endswith(' '):
            new_folder = new_folder[:-1]
        # If the folder name starts with a space, remove it;
        if new_folder.startswith(' '):
            new_folder = new_folder[1:]

        # Rename the folder, if the folder already exists, add a number to the end;
        new_folder_path = os.path.join(FOLDERS_TO_FIX, new_folder)
        if (folder_path != new_folder_path) & (os.path.exists(new_folder_path)):
            i = 1
            while os.path.exists(new_folder_path + ' ' + str(i)):
                i += 1
            new_folder_path = new_folder_path + ' ' + str(i)
        os.rename(folder_path, new_folder_path)
        print('Folder Renamed: old name =', folder, ', new name =', new_folder)
