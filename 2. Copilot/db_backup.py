import os
import shutil

active_db_file = '/full/path/to/app.db'
backup_db_file = '/full/path/to/backup.db'

def backup_database():

    # Check if the active database file exists
    if os.path.exists(active_db_file):
        # Copy the active database file to the backup location
        shutil.copyfile(active_db_file, backup_db_file)
        print(f"Backup of {active_db_file} created as {backup_db_file}.")
    else:
        active_db_file = './app.db'
        backup_db_file = './backup.db'

def restore_database():
    # Check if the backup database file exists
    if os.path.exists(backup_db_file):
        # Copy the backup database file to the active location
        shutil.copyfile(backup_db_file, active_db_file)
        print(f"Restored {active_db_file} from {backup_db_file}.")
    else:
        print(f"Error: {backup_db_file} does not exist.")

def main():
    print("1. Backup Database")
    print("2. Restore Database")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        backup_database()
    elif choice == '2':
        restore_database()
    elif choice == '3':
        print("Exiting the program.")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


