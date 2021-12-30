from tkinter.constants import TRUE
from guizero import App, Box, PushButton, TextBox, Picture, Window, Text, MenuBar
from tkinter.filedialog import askopenfilenames, askdirectory
from tkinter.ttk import Progressbar
import os
import threading
import time
import subprocess

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
        


    def start_copy():
        #robocopy "C:\Users\ATHQ\Documents\DAZ 3D" "D:\2021 bkup\3D Backup\DAZ 3D" /e /xo /eta
        #robocopy "C:\Users\ATHQ\Documents\Edits" "D:\2021 bkup\3D Backup\Edits" /e /xo /eta
        #robocopy "C:\Users\ATHQ\Desktop\Python Projects" "D:\2021 bkup\Python Projects" /e /xo /eta
        #os.system('cmd /c "robocopy "{folder}" "{source}" /e /np /xo /tee /log:result.txt"'.format(folder = folders_to_copy[0], source = hdd_text.value))
        copy_process_text = subprocess.run('cmd /c "robocopy "{folder}" "{source}" /e /np /xo /ns /nc /tee /njh /l /log:result.txt"'.format(folder = folders_to_copy[0], source = hdd_text.value), shell=True)
        with open("./result.txt") as f:
            file_status = f.readlines()
        #print(file_status[2].strip())
        #print(file_status[2:-11])  [2:- 11] pulls just the file names from the results text file
        for x in file_status[2:-11]:
            status_text.clear()
            status_text.value = x.strip()
            time.sleep(2)
       
            #n += 1
        #copy_process = subprocess.Popen('cmd /c "robocopy "{folder}" "{source}" /e /np /xo /ns /nc /tee /njh /log:result.txt"'.format(folder = folders_to_copy[0], source = hdd_text.value), shell=True)

        #("start command -flags arguments", shell=True)
        #stdout = copy_process.communicate()[0]
        #print(str(stdout))
        #t = threading.Thread(os.popen('cmd /c "robocopy "{folder}" "{source}" /e /np /xo /tee /log:result.txt"'.format(folder = folders_to_copy[0], source = hdd_text.value)).read())
        #t.start()
        #print(log)
        
        #new_output = log.split("\n")
        
        '''
        n = 0
        print(new_output[19])
        status_text.value = new_output[19]
        
        for x in (log):
            print(x + str(n))
            n += 1
        '''
        #print(folders_to_copy[0])
        #pass
    
    '''
    def thread_start():
        t = threading.Thread(start_copy())
        q = threading.Thread(print("Running Concerrently"))
        t.start()
        q.start()
    '''
    
    def file_function():
        pass
             
    #List that holds paths to selected folders to copy
    folders_to_copy = []
    
    
    #Gui Frame Start Section -------------------------------------------------------------------------------------
    app = App(title="Backup Tool", width=500, height=250, bg="white")
    
    
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
    

    
    #Button to add device where folders will be copied to
    hdd = Picture(box_left, image="./src/folder.png", align="top")
    hdd.hide()
    hdd_text = Text(box_left, text="folder_selection", align="top")
    hdd_text.hide()
    choose_hdd = PushButton(box_left, text="Select Backup Destination", align="top", command=load_show_save_device)
    
   
    
    
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
    
    #Button to add folders to copy list
    box_bottom_row_buttons = Box(box_right, width=50, height=25,  align="top", border=False)
    select_dir = PushButton(box_bottom_row_buttons, image="./src/plus.png", command=add_folder1, align="right")
    close_dir = PushButton(box_bottom_row_buttons, image="./src/close.png", command=remove_folder, align="right")
    close_dir.hide()
    
    
    #Start Copy Button
    #start_button = PushButton(box_bottom_status, text="Start", align="top", command=start_copy)
    start_button = PushButton(box_bottom_status, text="Start", align="top", command=start_copy)
    start_button.disable()
    
    #Status Text
    status_text = Text(box_bottom_status, text="This will show the current files being transfered")
    
    
    # add a progress bar to the box
    pb = Progressbar(box_bottom_progress.tk, length=500)
    box_bottom_progress.add_tk_widget(pb)
    
    
    # Menu Items
    menubar = MenuBar(app,
                  toplevel=["File"],
                  options=[
                      [ ["Save Settings", file_function], ["Load Settings", file_function] ],
                  ])
    
    
    
    
    app.display()
    


if __name__ == "__main__":
    main()