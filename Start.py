from guizero import App, Box, PushButton, TextBox, Picture, Window, Text
from tkinter.filedialog import askopenfilenames, askdirectory


def main():
    
    #Allows you to choose folder, adds it to list & displays path in GUI. Adds another folder if needed ( Up to 5 )
    def add_folder1():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_1.value = folder_selection
        dir_2.show()
        dir_2.disable()
        select_dir_1._command = add_folder2
        print(folders_to_copy)
        
    
    def add_folder2():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_2.value = folder_selection
        dir_3.show()
        dir_3.disable()
        print(folders_to_copy)
        select_dir_1._command = add_folder3
        
    def add_folder3():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_3.value = folder_selection
        dir_4.show()
        dir_4.disable()
        print(folders_to_copy)
        select_dir_1._command = add_folder4
        
    def add_folder4():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_4.value = folder_selection
        dir_5.show()
        dir_5.disable()
        print(folders_to_copy)
        select_dir_1._command = add_folder5
        
    def add_folder5():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        folders_to_copy.append(folder_selection)
        dir_5.value = folder_selection
        print(folders_to_copy)
        select_dir_1._command = max_folders_error
    
    
    #Error message that displays once the 5 folder limit is reached 
    def max_folders_error():
        error_popup = Window(app, height= 50, width=300)
        error_popup.hide()
        error_popup.error("Error", "Maximum Number of Folders Reached")
        
    
        
             
    #List that holds paths to selected folders to copy
    folders_to_copy = []
    
    
    #Gui Frame
    app = App(title="Backup Tool", width=500, height=250, bg="white")
    box = Box(app)
    
    #Button to add device where folders will be copied to
    choose_hdd = PushButton(app, text="Select Backup Destination", align="left")
    
    
    #Display of folder paths in the GUI - Programming 5 folders max
    dir_1 = TextBox(app, text="")
    dir_1.disable()
    
    dir_2 = TextBox(app, text="")
    dir_2.disable()
    dir_2.hide()
    
    dir_3 = TextBox(app, text="")
    dir_3.disable()
    dir_3.hide()
    
    dir_4 = TextBox(app, text="")
    dir_4.disable()
    dir_4.hide()
    
    dir_5 = TextBox(app, text="")
    dir_5.disable()
    dir_5.hide()
    
    #Button to add folders to copy list
    select_dir_1 = PushButton(app, image="./src/plus.png", command=add_folder1)
    

    
    app.display()
    


if __name__ == "__main__":
    main()