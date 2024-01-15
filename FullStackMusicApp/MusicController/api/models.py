from django.db import models
import string
import random

def generateUniqueCode():
    length = 6
    # Generates a random code of only uppercase ascii characters of a length of 6 characters
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k = length))
        # If code is unique break the loop
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length = 8, default = "", unique = True)
    host = models.CharField(max_length = 50, unique = True)
    guestCanPause = models.BooleanField(null = False, default = False)
    voteToSkip = models.IntegerField(null = False, default = 1)
    createdAt = models.DateTimeField(auto_now_add = True)   