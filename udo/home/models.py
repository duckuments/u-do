from django.db import models

# WARN : create date is not showed in admin.
class ContactModel(models.Model):
    fullName = models.CharField(max_length=300)
    email = models.CharField(max_length=350)
    subject = models.CharField(max_length=350)
    message = models.TextField()
    createdDate = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.subject
