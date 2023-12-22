import os

# Get the current working directory
# current_directory = os.getcwd()
# print("Current Directory:", current_directory)

# Change the current working directory
new_directory = "F:\Douments of min\My teaching stuff\Hamza"  # Change this to your desired path
os.chdir(new_directory)
print("Changed to:", os.getcwd())

# # List all files and directories in the current directory
# contents = os.listdir()
# print("Contents of current directory:", contents)

# # Create a new directory
# new_folder = "NewFolder"
# os.mkdir(new_folder)
# print("Created new folder:", new_folder)

# # Remove an empty directory
# os.rmdir(new_folder)
# print("Removed folder:", new_folder)

# # Delete a file (Note: Replace 'filename.txt' with an actual file in your directory)
# file_to_delete = "filename.txt"
# os.remove(file_to_delete)
# print("Deleted file:", file_to_delete)



# # Note:
# #     Remember to replace "C:\\Users\\YourUsername\\Documents" with the path you want for the new directory and "filename.txt" with the actual file you want to delete.