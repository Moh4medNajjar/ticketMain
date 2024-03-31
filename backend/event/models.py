from django.db import models
from feedback.models import Feedback
from User.models import User

class Event(models.Model):
    STATUS_CHOICES = (
        ('upcoming', 'Upcoming'),
        ('finished', 'Finished'),
    )
    AGE_CATEGORY_CHOICES = (
    ('children', 'Children (0-12)'),
    ('teens', 'Teens/Adolescents (13-19)'),
    ('young_adults', 'Young Adults (20s-30s)'),
    ('adults', 'Adults (30s+)'),
    ('seniors', 'Seniors/Elderly (65+)'),
    ('all_ages', 'All Ages/Family'),
    ('youth', 'Youth/School-Aged (5-18)'),
    ('young_professionals', 'Young Professionals (20s-30s)'),
    )

    id = models.AutoField(primary_key=True)
    OrganizerID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events') 
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    launch_time = models.TimeField()
    available_seats = models.IntegerField()
    ticket_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_tickets = models.IntegerField(default=0)
    attendees = models.ManyToManyField('User', through='Attendance', related_name='attending_events')
    event_feedbacks = models.ManyToManyField(Feedback, related_name='events_feedbacks', blank=True) 
    registration_link = models.URLField(blank=True)
    organizer_contact = models.CharField(max_length=100, blank=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    age_category = models.CharField(max_length=100, choices=AGE_CATEGORY_CHOICES, default='all_ages')
    is_approved = models.BooleanField(default=False)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)  # ImageField for event image


    def __str__(self):
        return self.title
