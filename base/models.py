from django.db import models

# Create your models here.

class Room(models.Model):
  #host =
  #topic =
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)
  #participants =
  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)
  folders = models.TextField(null=True, blank=True)

  def _str_(self):
    return self.name


class Window(models.Model):
    name = models.CharField(max_length=200)  # Window name
    description = models.TextField(blank=True, null=True)  # Optional description
    foldername = models.CharField(max_length=10, blank=True, null=True)  # New foldername field
    updated = models.DateTimeField(auto_now=True)  # Auto-update timestamp when modified
    created = models.DateTimeField(auto_now_add=True)  # Auto-set timestamp on creation

    def __str__(self):
        return self.name

class Message(models.Model):
    #user =
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # Auto-update timestamp when modified
    created = models.DateTimeField(auto_now_add=True)  # Auto-set timestamp on creation

    def __str__(self) -> str:
        return self.body[0:50]


