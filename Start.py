from guizero import App, Box, PushButton, TextBox, Picture
from tkinter.filedialog import askopenfilenames, askdirectory


def main():
    
    
    
    def add_folder():
        folder_selection = str((askdirectory(title="Select a Folder") + "/"))
        dir_1.value = folder_selection
        dir_2.show()
        #dir_2.disable()
         

    
    app = App(title="Backup Tool", width=500, height=250, bg="white")
    
    
    
    box = Box(app)
    
    save_gif = Picture(box, image="./src/save1.gif" )
    
    choose_hdd = PushButton(app, text="Select Backup Destination", align="left")
    
    dir_1 = TextBox(app, text="")
    dir_1.disable()
    
    dir_2 = TextBox(app, text="test")
    dir_2.disable()
    dir_2.hide()
    
    dir_3 = TextBox(app, text="test")
    dir_3.disable()
    dir_3.hide()
    
    dir_4 = TextBox(app, text="test")
    dir_4.disable()
    dir_4.hide()
    
    dir_5 = TextBox(app, text="test")
    dir_5.disable()
    dir_5.hide()
    
    select_dir_1 = PushButton(app, image="./src/plus.png", command=add_folder)
    
    #add_dir = PushButton(app, image="./src/plus.png")
    
    app.display()
    











if __name__ == "__main__":
    main()