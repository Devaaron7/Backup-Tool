from guizero import App, Box, PushButton



def main():
    
    app = App(title="Backup Tool", width=500, height=250, bg="white")
    
    box = Box(app)
    
    choose_hdd = PushButton(app, text="Select Backup Destination", align="left")
    
    select_dir = PushButton(app, align="right")
    
    app.display()
    











if __name__ == "__main__":
    main()