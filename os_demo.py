import os

# if not os.path.exists('demo_dir'):  # Check if the directory 'demo_dir' exists
#     os.mkdir('demo_dir')  # If not, create the directory'


# os.makedirs('demo_dirs/sub_dir',exist_ok=True)  # Create a new subdirectory named 'sub_dir' inside 'demo_dir'

# #os.rename('demo_dir', 'new_demo_dir')  # Rename 'demo_dir' to 'new_demo_dir'

# #os.rmdir('new_demo_dir')

# os.removedirs('demo_dirs/sub_dir')  # Remove the subdirectory 'sub_dir' inside 'demo_dir'

all_files = os.listdir('error')  # List all files and directories in 'demo_dir'

print(type(all_files))  # Print the list of files and directories