from django.db import models
import uuid

# Create your models here.

class Department(models.Model):
    dep_name        = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

class Doctor(models.Model):
    doc_name  = models.CharField(max_length=255)
    doc_spec  = models.CharField(max_length=255)
    dep_name  = models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='uploads/Doctors')

    def __str__(self):
        return 'Dr '+ self.doc_name+' - ( '+self.doc_spec +' )'

class Booking(models.Model):

    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    CANCELED = 'Canceled'
    VISITED = 'Visited'
    NOT_VISITED = 'Not Visited'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELED, 'Canceled'),
        (VISITED, 'Visited'),
        (NOT_VISITED, 'Not Visited'),
    ]



    p_name       = models.CharField(max_length=255)
    p_phone      = models.CharField(max_length=255)
    symptoms = models.CharField(max_length=300,null=True)
    doc_name     = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING,blank=True)
    token = models.PositiveIntegerField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        # Set token within the range 1-100
        if not self.token:
            existing_tokens = Booking.objects.values_list('token', flat=True)
            available_tokens = set(range(1, 1001)) - set(existing_tokens)
            if available_tokens:
                self.token = min(available_tokens)
            else:
                # Handle the case where all tokens are used
                raise ValueError("All tokens are used. Cannot generate a new token.")

        super().save(*args, **kwargs)

class Slider(models.Model):
    heading=models.CharField(max_length=250)
    content=models.TextField(max_length=250)
    image=models.ImageField(upload_to='uploads/slider')

    def __str__(self):
        return self.heading

class About(models.Model):
    heading=models.CharField(max_length=250)
    content=models.TextField(max_length=250)
    image=models.ImageField(upload_to='uploads/about')

    def __str__(self):
        return self.heading
    
