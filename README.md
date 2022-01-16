# Backup-Tool
Program to backup multiple folders / items to device of choice

I wrote this program to allow the user to quickly backup the folders the choose to the device they choose.
This uses the Robocopy features from Microsoft to copy the folders.
I've used a similar script to backup my creative work daily

Features:
- Save / Load settings allowing quick setup of copy paths.
- Uses the "/xo" copy flag for Robocopy, allowing for backups that excludes older files.
- Current version allows up to 5 directories to be copied to destination of choice.

Required Modules:
Guizero

Usage:

1. Download & unzip the folder.
2. Run the file labeled "Main.pyw" ( It should be in the same directory as the "icons" folder ).
3. Select the "Select Backup Destination" button, and choose your device path.
4. Select the "+" icon to add the folders you would like to copy to your selected device.
5. Select the "Start" button. The copying process will start.
6. Once the copy is finished, you can now close the program. A copy of the files / folders will be inside "Backup_Folder" inside the destination folder.

You can use the save / load options, under the file menu, to save your settings to a .ini file for quick setup!

Thank you for downloading!

Aaron T
