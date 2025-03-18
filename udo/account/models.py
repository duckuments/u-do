from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
import os


class User(AbstractUser):
    ImgName = models.ImageField(upload_to="userImage",null=True,blank=True,default="userImage/default.jpg") 
    ActiveCode = models.CharField(max_length=72)
    Rating = models.IntegerField(null=True,validators=[MinValueValidator(0),MaxValueValidator(5)])
    slug = models.SlugField(default="",null=False)
    Information = models.TextField(default="im using u-do in my job!")

    def get_absolute_url(self):
        return reverse('account-profile',args=[self.slug])

    def save(self, *args, **kwargs):
        try:
            old_instance = User.objects.get(id=self.id)
            if old_instance.ImgName != "userImage/default.jpg" and old_instance.ImgName != self.ImgName:
                old_image_path = os.path.join(settings.MEDIA_ROOT, str(old_instance.ImgName))
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
        except: 
            pass
        self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

    def get_active_code(self):
        return self.ActiveCode

    def get_email(self):
        return self.email
