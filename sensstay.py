import os
import shutil
import tkinter as tk
from tkinter import filedialog

def backup_game_config():
    # Create a new Tkinter window
    window = tk.Tk()
    
    # Name the window
    window.title('SensStay')

    # Set the window size and position
    # find the center point
    center_x = int(window.winfo_screenwidth() / 2 - 300)
    center_y = int(window.winfo_screenheight() / 2 - 200)
    window.geometry(f'600x400+{center_x}+{center_y}')

    # create a label for the backup frame
    back_frame_label = tk.Label(window, text="Game Backup")
    
    # pack the label
    back_frame_label.pack()

    # create a frame for the config backup
    back_frame = tk.Frame(window, bd=1, relief='solid')

    # pack the frame into the window
    back_frame.pack(ipadx= 10, ipady = 10)

    # Create a button that lets the user select the config file
    def select_config_file():
        config_path = filedialog.askopenfilename()
        config_path_var.set(config_path)
        
        # Stops the directory from displaying too much
        if len(config_path) <= 40:
            config_path_label.config(text=config_path)  
        else:
            config_path_label.config(text=config_path[0:40]+"...")  

        game_name_entry.config(state='normal')

    config_path_var = tk.StringVar()
    config_path_button = tk.Button(back_frame, 
                                   text="Select Config File", 
                                   command=select_config_file)
    config_path_button.pack(padx=10, pady=10)

    # Create a label to display the selected configuration path
    config_path_title_label = tk.Label(back_frame, text="Configuration Selected:")
    config_path_title_label.pack()

    # Create a label to display the selected configuration path
    config_path_label = tk.Label(back_frame, text="No configuration selected")
    config_path_label.pack()

    # Create a StringVar for the game's name
    game_name_var = tk.StringVar()

    # Create a label for the game's name entry field
    game_name_label = tk.Label(back_frame, text="Game Name:")
    game_name_label.pack()

    # Create an entry field for the game's name
    game_name_entry = tk.Entry(back_frame, 
                               textvariable=game_name_var, 
                               state='disabled')
    game_name_entry.pack()

    # Create a button that backs up the config file when clicked
    def backup_config():
        game_name = game_name_var.get()
        config_path = config_path_var.get()

        # Check if the config file exists
        if not os.path.isfile(config_path):
            print("The provided config file path does not exist.")
            return

        # Create the backup directory
        backup_dir = os.path.join(os.getcwd(), "Configs", game_name)
        os.makedirs(backup_dir, exist_ok=True)

        # Copy the config file to the backup directory
        backup_path = os.path.join(backup_dir, os.path.basename(config_path))
        shutil.copy2(config_path, backup_path)

        print(f"Config file for {game_name} has been backed up to {backup_path}")

    backup_button = tk.Button(back_frame, text="Backup Config", command=backup_config)
    backup_button.pack(padx=10, pady= 10)

    # Start the Tkinter event loop
    window.mainloop()

# Call the function
backup_game_config()
