import os
import shutil

def backup_game_config():
    # Ask the user for the game's name
    game_name = input("Enter the game's name: ")

    # Ask the user for the config file path
    config_path = input("Enter the full path to the game's config file: ")

    # Remove double quotes from the config_path
    config_path = config_path.replace('"', '')

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

# Call the function
backup_game_config()
