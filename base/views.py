from django.shortcuts import render
import os
from .models import Room
from .models import Window
from django.conf import settings

from django.core.mail import send_mail
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

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Sending the email
        try:
            send_mail(
                f"{name}, {subject}",  # Subject
                message,               # Message
                settings.DEFAULT_FROM_EMAIL,  # From email (set in settings)
                ['erwazhan@gmail.com'], # To email
                fail_silently=False,    # Set to True if you want to suppress errors
            )
            success_message = "Your message has been sent successfully!"
        except Exception as e:
            success_message = f"An error occurred: {e}"

        context = {
            'MEDIA_URL': settings.MEDIA_URL,
            'name': name,
            'success_message': success_message,  # Add success message to context
        }

        return render(request, 'contact.html', context)

    else:
        context = {
            'MEDIA_URL': settings.MEDIA_URL,
        }
        return render(request, 'contact.html', context)


