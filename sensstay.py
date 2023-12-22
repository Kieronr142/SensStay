import os
import shutil
import tkinter as tk
from tkinter import filedialog

def setup_tkinter_window():
    # Create a new Tkinter window
    window = tk.Tk()

    # Name the window
    window.title('SensStay')

    # Set the window size and position
    center_x = int(window.winfo_screenwidth() / 2 - 300)
    center_y = int(window.winfo_screenheight() / 2 - 200)
    window.geometry(f'600x400+{center_x}+{center_y}')

    # Set the icon
    window.iconbitmap('.\\assets\SensStay.ico')

    return window

def backup_game_config(window):

    # create a frame for the config backup
    back_frame = tk.Frame(window, bd=1, relief='solid')

    # pack the frame into the window
    back_frame.pack(padx=10, pady=10, ipadx= 10, ipady = 10, side=tk.LEFT)

    # create a label for the backup frame
    back_frame_label = tk.Label(back_frame, text="Game Backup", font=(25))
    
    # pack the label
    back_frame_label.pack()

    ### CONFIG FILE SELECTION ###



    # Create a button that lets the user select the config file
    def select_config_file():
        config_path = filedialog.askopenfilename()
        config_path_var.set(config_path)
        
        # Update the text box with the selected path
        config_path_text.config(state='normal') # Enable box editing
        config_path_text.delete('1.0', tk.END)  # Clear the text box
        config_path_text.insert(tk.END, config_path)  # Insert the selected path
        config_path_text.config(state='disabled') # Disable box editing

        # Allows the user to type in the box
        game_name_entry.config(state='normal')
        game_name_entry.delete(0,'end')

        # Resets the game name variable to clear the box
        game_name_var.set('')

    config_path_var = tk.StringVar()
    config_path_button = tk.Button(back_frame, 
                                   text="Select Config File", 
                                   command=select_config_file)
    config_path_button.pack(padx=10, pady=10)

    # Create a text box to display the selected configuration path
    # Limited to 30 characters long and wrap stops the output being displayed vertically
    config_path_text = tk.Text(back_frame, 
                               height=1, 
                               width=30, 
                               wrap="none",
                               bg='#f0f0f0',
                               state='disabled')
    config_path_text.pack()

    # Create a horizontal scrollbar and attach it to the text box
    x_scrollbar = tk.Scrollbar(back_frame,
                               orient='horizontal',
                               command=config_path_text.xview)
    x_scrollbar.pack(fill='x')
    config_path_text['xscrollcommand'] = x_scrollbar.set



    ### Game Name Input ###



    # Create a StringVar for the game's name
    game_name_var = tk.StringVar()

    # Create a label for the game's name entry field
    game_name_label = tk.Label(back_frame, text="Game Name:")
    game_name_label.pack()

    # Create an entry field for the game's name
    game_name_entry = tk.Entry(back_frame, 
                               textvariable=game_name_var,
                               width=40)
    game_name_entry.pack()

    # Insert the initial box text
    game_name_entry.insert(0, 'Select the games config file first')

    # Disable the game name field from modificaton
    game_name_entry.config(state='disabled')



    ### BACKUP THE GAME CONFIG FILE ###



    # Create a button that backs up the config file when clicked
    def backup_config():
        game_name = game_name_var.get()
        config_path = config_path_var.get()

        # Check if the config file exists
        if not os.path.isfile(config_path):
            backup_path_text.config(state='normal') # Enable box editing
            backup_path_text.delete('1.0', tk.END)  # Clear the text box
            backup_path_text.insert(tk.END, 'Configuration file path does not exist')
            backup_path_text.config(state='disabled') # Disable box editing
            return
        
        # Check if the game name exists
        if len(game_name) == 0:
            backup_path_text.config(state='normal') # Enable box editing
            backup_path_text.delete('1.0', tk.END)  # Clear the text box
            backup_path_text.insert(tk.END, 'Enter a valid game name')
            backup_path_text.config(state='disabled') # Disable box editing
        else:
            # Create the backup directory
            backup_dir = os.path.join(os.getcwd(), "Configs", game_name)
            os.makedirs(backup_dir, exist_ok=True)

            # Copy the config file to the backup directory
            backup_path = os.path.join(backup_dir, os.path.basename(config_path))
            shutil.copy2(config_path, backup_path)


            # Update the backup text box with the selected path
            backup_path_text.config(state='normal') # Enable box editing
            backup_path_text.delete('1.0', tk.END)  # Clear the text box
            backup_path_text.insert(tk.END, 
                                    f'Configuration file for {game_name} has been backed up to {backup_path}')
            backup_path_text.config(state='disabled') # Disable box editing

    backup_button = tk.Button(back_frame, text="Backup Config", command=backup_config)
    backup_button.pack(padx=10, pady= 10)

    # Create a text box to display the selected configuration path
    # Limited to 30 characters long
    backup_path_text = tk.Text(back_frame, 
                               height=5, 
                               width=30,
                               bg='#f0f0f0',
                               state='disabled')
    backup_path_text.pack()
    return back_frame

def installed_games(window):
    # lists all of the games with configurations saved
    
    # create a new frame that lines up horizontally with the existing frame
    install_frame = tk.Frame(window, bd=1, relief='solid')

    # pack the new frame into the window
    install_frame.pack(padx=10, pady=10, ipadx=10, ipady=10, side=tk.LEFT)

    # create a label for the backup frame
    install_frame_label = tk.Label(install_frame, text="Backed up games", font=(25))
    
    # pack the label
    install_frame_label.pack()

    # Get a list of all folder names in the 'configs/' directory
    folder_names = next(os.walk('configs/'))[1]

    # Add a label to install_frame for each folder name
    for folder in folder_names:
        label = tk.Label(install_frame, text=folder)
        label.pack()

    return install_frame

def resize_frames(event, frame1, frame2):
    # Resize the second frame based on the size of the first frame
    frame2.config(width=frame1.winfo_width(), height=frame1.winfo_height())

def main():
    # Call the Tkinter window setup function
    window = setup_tkinter_window()

    # Call the backup frame
    backup_frame = backup_game_config(window)

    # Call the games list
    games_frame = installed_games(window)

    # Bind the resize_frames function to the <Configure> event of both frames
    window.bind('<Configure>', lambda e: resize_frames(e, backup_frame, games_frame))

    # TO DO ADD MORE FUNCTIONS

    window.mainloop()

# Call the function
main()
