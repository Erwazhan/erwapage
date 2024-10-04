from django.shortcuts import render
import os
from .models import Room
from .models import Window
from django.conf import settings
# Create your views here.


def navbar(request):
  rooms = Room.objects.all()
  context = {'rooms':rooms}
  return render(request, 'navbar.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    rooms = Room.objects.all()

    room_img = {}
    folder_descriptions = {}

    for room in rooms:
        folders = [f.strip() for f in room.folders.split(",")]
        descriptions = [d.strip() for d in room.description.split("::")]

        project_img = {}

        for f in folders:
            folder_path = os.path.join(settings.MEDIA_ROOT, f'project_img/{room.name}', f)

            if os.path.exists(folder_path):
                files = os.listdir(folder_path)
                files = [file for file in files if os.path.isfile(os.path.join(folder_path, file)) and file.lower().endswith(('.jpg', '.jpeg', '.png', 'pdf','txt'))]
                files.sort()
            else:
                files = []

            project_img[f] = files

        room_img[room.name] = project_img
        folder_descriptions[room.name] = descriptions

    current_room = Room.objects.get(id=pk)
    current_folders = [f.strip() for f in current_room.folders.split(",")]
    current_descriptions = [d.strip() for d in current_room.description.split("::")]

    room_info = zip(current_folders, current_descriptions)

    context = {
        'room_info': room_info,  # Pairs of folder and description for the current room
        'room_img': room_img,    # Images for all rooms
        'room': current_room,    # Current room object
        'rooms': rooms,          # All room objects
        'MEDIA_URL': settings.MEDIA_URL,
    }

    return render(request, 'base/room.html', context)




def home(request):
  rooms = Room.objects.all()
  windows = Window.objects.all()
  window_files = {}


  for window in windows:
    folder_path = os.path.join(settings.MEDIA_ROOT, 'images', str(window.foldername))

    if os.path.exists(folder_path):
        files = os.listdir(folder_path)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        files.sort()
    else:
        files = []

    window_files[window.foldername] = files

  context = {
      'windows': windows,
      'window_files': window_files,
      'MEDIA_URL': settings.MEDIA_URL,
      'rooms':rooms,
  }

  return render(request, 'base/index.html', context)


def gallery(request):

  return render(request, 'gallery.html')

from .forms import ContactForm

def contact(request):
    form = ContactForm()
    rooms = Room.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            # Extract form data
            message_email = form.cleaned_data['email']
            message_subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # You can now process the data (e.g., send an email or save it to a database)

            # Optionally, pass the data to the context for display
            context = {
                'form': form,
                'message_email': message_email,
                'message_subject': message_subject,
                'message': message,
                'success': True  # Add a flag to indicate the form was successfully submitted
            }

            return render(request, 'contact.html', context)

    context = {
      'form': form,
      'rooms':rooms,
      'MEDIA_URL': settings.MEDIA_URL,
    }

    return render(request, 'contact.html', context)
