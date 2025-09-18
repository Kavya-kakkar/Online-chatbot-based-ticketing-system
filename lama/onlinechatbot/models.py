from django.db import models
from django.contrib.auth.models import User

# 1. Museum Exhibits
class Exhibit(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title


# 2. Events
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.name


# 3. Ticket Booking
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, blank=True, null=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Ticket for {self.user.username} - {self.event or self.exhibit}"


# 4. Visitor Feedback
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField(default=5)  # 1 to 5 stars
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"
    

# 5. Musem Staff
class Staff(models.Model):
    name = models.CharField(max_length=100),
    role = models.CharField(max_length=100),
    contact_info = models.CharField(max_length=200),
    photo = models.ImageField(upload_to='staff/', blank=True, null=True),
    bio=models.TextField(blank=True,null=True),
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    

