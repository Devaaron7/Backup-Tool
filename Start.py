from guizero import App, Box, PushButton, TextBox, Picture, Window, Text, MenuBar
from tkinter.filedialog import askopenfilenames, askdirectory


def main():
    
    #Allows you to choose folder, adds it to list & displays path in GUI. Adds another folder if needed ( Up to 5 )
    def add_folder1():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_1.value = short_file_path(folder_selection)
        dir_2.show()
        dir_2.disable()
        select_dir_1._command = add_folder2
        print(folders_to_copy)
        
    
    def add_folder2():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_2.value = short_file_path(folder_selection)
        dir_3.show()
        dir_3.disable()
        print(folders_to_copy)
        select_dir_1._command = add_folder3
        
    def add_folder3():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_3.value = short_file_path(folder_selection)
        dir_4.show()
        dir_4.disable()
        print(folders_to_copy)
        select_dir_1._command = add_folder4
        
    def add_folder4():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_4.value = short_file_path(folder_selection)
        dir_5.show()
        dir_5.disable()
        print(folders_to_copy)
        select_dir_1._command = add_folder5
        
    def add_folder5():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_5.value = short_file_path(folder_selection)
        print(folders_to_copy)
        select_dir_1._command = max_folders_error
    
    
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
    
    
    def load_show_save_device():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        hdd.show()
        hdd_text.show()
        hdd_text.value = folder_selection
        #choose_hdd.destroy()


    def file_function():
        pass
             
    #List that holds paths to selected folders to copy
    folders_to_copy = []
    
    
    #Gui Frame
    #app = App(title="Backup Tool", width=500, height=250, bg="white", layout="grid")
    app = App(title="Backup Tool", width=500, height=250, bg="white")
    box_top_row = Box(app, width="fill", height="fill",  align="top")
    box_bottom_row = Box(app, width="fill", height="fill",  align="bottom")
    box_left = Box(box_top_row, width="fill", height="fill",  align="left")
    box_center = Box(box_top_row, width="fill", height="fill", align="right")
    box_right = Box(box_top_row, width="fill", height="fill", align="right")
    box_bottom_status = Box(box_bottom_row, width="fill", align="bottom")
    box_bottom_progress = Box(box_bottom_row, width="fill", align="bottom")
    
    
    button1 = PushButton(box_left, text="1", height="fill", width="fill")

    button2 = PushButton(box_center, text="2", height="fill", width="fill")

    button3 = PushButton(box_right, text="3", height="fill", width="fill")
    
    button4 = PushButton(box_bottom_status, text="4", width="fill")
    
    button5 = PushButton(box_bottom_progress, width="fill", text="5")
    
    
    
    '''
    #test1 = PushButton(app, grid=[0,0])
    #test2 = PushButton(app, grid=[3,0])
    
    
    #button1 = PushButton(app, text="1", align="left", grid=[0,0])
    #button2 = PushButton(app, text="2", width=17, grid=[1,0])
    #button3  = PushButton(app, text="3", align="right", grid=[2,0])
    #button4  = PushButton(app, text="4", grid=[0,1])
    #button5  = PushButton(app, text="5", grid=[1,1])
    #button6  = PushButton(app, text="6", grid=[2,1])
    #Button to add device where folders will be copied to
    hdd = Picture(app, image="./src/folder.png", grid=[0,0])
    hdd.hide()
    hdd_text = Text(app, text="folder_selection", grid=[0,1])
    hdd_text.hide()
    choose_hdd = PushButton(app, text="Select Backup Destination", grid=[0,2], command=load_show_save_device)
    
    
    
    #button7  = PushButton(app, text="7", grid=[0,2])
    #button8  = PushButton(app, text="8", grid=[1,2])
    #button9  = PushButton(app, text="9", grid=[2,2])
    
    button0  = PushButton(app, text="10", grid=[9,0])
    button0  = PushButton(app, text="11", grid=[10,0])
    button0  = PushButton(app, text="12", grid=[11,0])
    button0  = PushButton(app, text="13", grid=[12,0])
 
    
    
    
    
    
    
    #Button to add device where folders will be copied to
    hdd = Picture(box_left, image="./src/folder.png", align="top")
    hdd.hide()
    hdd_text = Text(box_left, text="folder_selection", align="top")
    hdd_text.hide()
    choose_hdd = PushButton(box_left, text="Select Backup Destination", align="top", command=load_show_save_device)
    
   
    
    
    #Display of folder paths in the GUI - Programming 5 folders max
    dir_1 = TextBox(box_right, text="", width=20, align="right", grid=[0,0])
    dir_1.disable()
    
    dir_2 = TextBox(box_right, text="", width=20, grid=[0,1])
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
    select_dir_1 = PushButton(box_right, image="./src/plus.png", command=add_folder1, grid=[0,2])
    
    
    '''
    menubar = MenuBar(app,
                  toplevel=["File"],
                  options=[
                      [ ["Save Settings", file_function], ["Load Settings", file_function] ],
                  ])
    
    
    
    
    app.display()
    


if __name__ == "__main__":
    main()