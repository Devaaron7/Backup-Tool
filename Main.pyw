from tkinter.constants import TRUE
from typing import Counter
from guizero import App, Box, PushButton, TextBox, Picture, Window, Text, MenuBar
from tkinter.filedialog import askopenfilenames, askdirectory, asksaveasfile
from tkinter.ttk import Progressbar
import os
import threading
import time
import subprocess
import os.path
import configparser
from shutil import copyfile

def main():
    
    #Allows you to choose folder, adds it to list & displays path in GUI. Adds another folder if needed ( Up to 5 )
    def add_folder1():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_1.value = short_file_path(folder_selection)
        dir_2.show()
        dir_2.disable()
        close_dir.show()
        select_dir._command = add_folder2
        if len(folders_to_copy) >= 1 and hdd_text._text.__contains__("//") == True:
            start_button.enable()
        else:
            start_button.disable()
        print(folders_to_copy)
        
    def add_folder2():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_2.value = short_file_path(folder_selection)
        dir_3.show()
        dir_3.disable()
        print(folders_to_copy)
        select_dir._command = add_folder3
        
    def add_folder3():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_3.value = short_file_path(folder_selection)
        dir_4.show()
        dir_4.disable()
        print(folders_to_copy)
        select_dir._command = add_folder4
        
    def add_folder4():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_4.value = short_file_path(folder_selection)
        dir_5.show()
        dir_5.disable()
        print(folders_to_copy)
        select_dir._command = add_folder5
        
    def add_folder5():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_5.value = short_file_path(folder_selection)
        print(folders_to_copy)
        select_dir._command = max_folders_error
    
    def remove_folder():
        target = short_file_path(folders_to_copy[-1])
        if dir_1.value == target:
            dir_1.value = ""
            dir_2.hide()
            folders_to_copy.clear()
            select_dir._command = add_folder1
            if len(folders_to_copy) >= 1 and hdd_text._text.__contains__("//") == True:
                start_button.enable()
            else:
                start_button.disable()
        if dir_2.value == target:
            dir_2.value = ""
            dir_3.hide()
            folders_to_copy.pop(-1)
            select_dir._command = add_folder2
        if dir_3.value == target:
            dir_3.value = ""
            dir_4.hide()
            folders_to_copy.pop(-1)
            select_dir._command = add_folder3
        if dir_4.value == target:
            dir_4.value = ""
            dir_5.hide()
            folders_to_copy.pop(-1)
            select_dir._command = add_folder4
        if dir_5.value == target:
            dir_5.value = ""
            folders_to_copy.pop(-1)
            select_dir._command = add_folder5
    
    #Error message that displays once the 5 folder limit is reached 
    def max_folders_error():
        error_popup = Window(app, height= 50, width=300)
        error_popup.hide()
        error_popup.error("Error", "Maximum Number of Folders Reached")
        
    # Shortens folder path for GUI
    def short_file_path(path):
        temp = ""
        count = -1
        for letters in path:
            temp += path[count]
            if temp.count("/") == 2:
                break
            if temp.count("\\") == 2:
                temp = temp.replace("\\", "//")
                break
            count -= 1
            
        return temp[::-1]
    
    # Stores path to storage device / path + enables image
    def load_show_save_device():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        hdd.show()
        hdd_text.show()
        hdd_text.value = folder_selection
        if len(folders_to_copy) >= 1 and hdd_text._text.__contains__("//") == True:
            start_button.enable()
        else:
            start_button.disable()
      

    # Starts the main copy feature
    def start_copy():
        box_bottom_progress.show()
        status_text.show()
        start_button.disable()
        status_text.value = "Copying Files..."
        folder_names_to_create.clear()
        pb.start()

        # Creates root "Backup_Folder" on directory selected
        if os.path.isdir(hdd_text.value + "Backup_Folder/") == False:
            os.mkdir(hdd_text.value + "Backup_Folder")
            time.sleep(1)
        
       # Creates list of subfolders to create on destination folder
        for short_paths in folders_to_copy:
            folder_names_to_create.append(short_file_path(short_paths))
        
       
        create_num = 0
        for real_items in folders_to_copy: 
            subprocess.run('cmd /c "robocopy "{folder}" "{source}Backup_Folder{copy_folder}" /e /np /xo /ns /nc /tee /njh /log+:{source}Backup_Folder/result.txt"'.format(folder = real_items, source = hdd_text.value, copy_folder = folder_names_to_create[create_num]), shell=True)
            create_num += 1
        

        start_button.enable()
        status_text.value = "Backup Complete!" 

        copyfile("{source}Backup_Folder/result.txt".format(source = hdd_text.value), "{source}Backup_Folder/copy_result.txt".format(source = hdd_text.value))
        os.remove("{source}Backup_Folder/result.txt".format(source = hdd_text.value))
        pb.stop()
        

    #Threading Start    
    def background():
        thread1 = threading.Thread(target=start_copy)
        thread1.start()


    # Save / Load ini features
    def save_settings():
        config['Backup Destination'] = {}
        config['Backup Destination']['Path'] = hdd_text.value

        config['Folders To Copy'] = {}
        config['Folders To Copy']['Folder 1'] = folders_to_copy[0]

        if len(folders_to_copy) > 1:
            folder_num = 2
            for saves in range(1, len(folders_to_copy)):
                config['Folders To Copy']['Folder {}'.format(folder_num)] = folders_to_copy[saves]
                folder_num += 1
        

        save_ini = asksaveasfile(mode='w', defaultextension=".ini")
        if save_ini is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return

        config.write(save_ini)

    def load_settings():
        config.read(askopenfilenames())
        hdd_text.show()
        hdd.show()
        hdd_text.value = config['Backup Destination']['Path']
        folders_to_copy.clear()
        
        if config['Folders To Copy']['Folder 1']:
            folders_to_copy.append(config['Folders To Copy']['Folder 1'])
            dir_1.value = short_file_path(config['Folders To Copy']['Folder 1'])
            dir_2.show()
            close_dir.show()
            start_button.enable()  
        if config['Folders To Copy']['Folder 2']:
            folders_to_copy.append(config['Folders To Copy']['Folder 2'])
            dir_2.value = short_file_path(config['Folders To Copy']['Folder 2'])
            dir_3.show()  
        if config['Folders To Copy']['Folder 3']:
            folders_to_copy.append(config['Folders To Copy']['Folder 3'])
            dir_3.value = short_file_path(config['Folders To Copy']['Folder 3'])
            dir_4.show()
            print(folders_to_copy)
        if config['Folders To Copy']['Folder 4']:
            folders_to_copy.append(config['Folders To Copy']['Folder 4'])
            dir_4.value = short_file_path(config['Folders To Copy']['Folder 4'])
            dir_5.show()
            print(folders_to_copy)
        if config['Folders To Copy']['Folder 5']:
            folders_to_copy.append(config['Folders To Copy']['Folder 5'])
            dir_5.value = short_file_path(config['Folders To Copy']['Folder 5'])
            print(folders_to_copy)
        
    
    # Create instance of ini module
    config = configparser.ConfigParser()

    #List that holds paths to selected folders to copy
    folders_to_copy = []

    folder_names_to_create = []

    #Gui Frame Start Section -------------------------------------------------------------------------------------
    app = App(title="Backup Tool", width=500, height=250, bg="white")

    app.tk.iconbitmap("./icons/disk.ico")
    
    # Splits The GUI into Two Parts
    box_top_row = Box(app, width="fill", height="fill",  align="top")
    box_bottom_row = Box(app, width="fill", height="fill",  align="bottom")
    
    
    # Splits the Two portion into three columns
    box_left = Box(box_top_row, width="fill", height="fill",  align="left")
    box_center = Box(box_top_row, width="fill", height="fill", align="left")
    box_right = Box(box_top_row, width="fill", height="fill", align="right", border=False)
    
    
    # Empty Space to separate the left column from the right. Filled with an invisible button
    button2 = PushButton(box_center, text="2", height="fill", width="fill", visible=False)

    # Splits the bottom portion into two parts - One for Status Text & One for the Progress bar
    box_bottom_progress = Box(box_bottom_row, width="fill", align="bottom", border=True)
    box_bottom_status = Box(box_bottom_row, width="fill", align="bottom")

    # Adds a progress bar to the box
    pb = Progressbar(box_bottom_progress.tk, length=500, mode = 'indeterminate')
    box_bottom_progress.add_tk_widget(pb)
    box_bottom_progress.hide()

    #Status Text
    status_text = Text(box_bottom_status, size=9, text="This will show the current files being transfered")
    status_text.hide()
    
    #Display of folder paths in the GUI - Programming 5 folders max
    dir_1 = TextBox(box_right, text="", width=20, align="top")
    dir_1.disable()
    
    dir_2 = TextBox(box_right, text="", width=20, align="top")
    dir_2.disable()
    dir_2.hide()
    
    dir_3 = TextBox(box_right, text="", width=20)
    dir_3.disable()
    dir_3.hide()
    
    dir_4 = TextBox(box_right, text="", width=20)
    dir_4.disable()
    dir_4.hide()
    
    dir_5 = TextBox(box_right, text="", width=20)
    dir_5.disable()
    dir_5.hide()


    #Button Groups -------------------------------------------------------------------------------------

    
    #Button to add device where folders will be copied to
    hdd = Picture(box_left, image="./icons/folder.png", align="top")
    hdd.hide()
    hdd_text = Text(box_left, size=9, text="folder_selection", align="top")
    hdd_text.hide()
    choose_hdd = PushButton(box_left, text="Select Backup Destination", align="top", command=load_show_save_device)
    
    #Button to add folders to copy list
    box_bottom_row_buttons = Box(box_right, width=50, height=25,  align="top", border=False)
    select_dir = PushButton(box_bottom_row_buttons, image="./icons/plus.png", command=add_folder1, align="right")
    close_dir = PushButton(box_bottom_row_buttons, image="./icons/close.png", command=remove_folder, align="right")
    close_dir.hide()
    
    #Start Button
    start_button = PushButton(box_bottom_status, text="Start", align="top", command=background)
    start_button.disable()
    
    
    # Menu Items
    menubar = MenuBar(app,
                  toplevel=["File"],
                  options=[
                      [ ["Save Settings", save_settings], ["Load Settings", load_settings] ],
                  ])
    

    app.display()
    


if __name__ == "__main__":
    main()
