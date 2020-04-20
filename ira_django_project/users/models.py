from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} profile"
    
    def save(self):
        # method that is run after our model is saved -- override default save method
        super().save()  # run the save method of our parent save method (call super)

        img = Image.open(self.image.path)
        print('hit')

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)        
            img.save(self.image.path)

