import os
from django.conf import settings

def populate_windows():
    # Define paths to the directories for each window
    window_folders = {
        'window1': os.path.join(settings.STATICFILES_DIRS[0], 'window1_contents'),
        'window2': os.path.join(settings.STATICFILES_DIRS[0], 'window2_contents'),
        'window3': os.path.join(settings.STATICFILES_DIRS[0], 'window3_contents'),
    }

    # Dictionary to hold window contents
    window_contents = {}

    # Iterate through each folder and list the files
    for window, folder_path in window_folders.items():
      # Check if the folder exists
      if os.path.exists(folder_path):
            # List the files in the folder (e.g., images, text files, etc.)
            files = os.listdir(folder_path)

            # Filter for images (or other types of files based on your need)
            contents = [file for file in files if file.endswith(('.png', '.jpg', '.jpeg', '.txt', '.pdf'))]

            # Add the content to the corresponding window
            window_contents[window] = contents

    return window_contents
