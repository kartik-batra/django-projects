from django.db import models
import pytz

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
# Create your models here.
social_platforms = (('Facebook' , 'Facebook' ),
                    ('Instagram', 'Instagram'),
                    ('Twitter' , 'Twitter' ),
                    ('Pinterest' , 'Pinterest' ),
                    ('LinkedIn' , 'LinkedIn' ),
                    ('Youtube', 'Youtube'),
                    )
class SocialAccount(models.Model):
    user_id = models.CharField(max_length=100,primary_key=True,unique=True, blank=False)
    account_type = models.CharField(max_length=500,unique=True,choices=social_platforms, blank=False)
    access_token = models.TextField(blank=False)

    def __str__(self):
        return self.account_type
    
class Schedule(models.Model):
    schedule_id = models.CharField(primary_key=True,max_length=50)
    date_time = models.DateTimeField(unique=True)
    time_zone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

    def __str__(self):
        return self.schedule_id

STATUS_CHOICES = (('Active', 'Active'),
                  ('Inactive','Inactive'),
                  ('Finished','Finished'),)

class Campaign(models.Model):
    campaign_id = models.CharField(primary_key=True,max_length=50)
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.campaign_id


class UserPost(models.Model):
    user_id = models.CharField(max_length=100)
    selected_accounts = models.ManyToManyField(SocialAccount)
    description = models.TextField(max_length=500,)

    attachments = models.ImageField(upload_to="uploads/", null=False , blank=False)
    
    insta_desc = models.TextField(max_length=500,)
    insta_story = models.BooleanField(default=False)
    insta_first_comment = models.BooleanField(default=False)
    linkedin_desc = models.TextField(max_length=500,)
    pinterest_desc = models.TextField(max_length=500,)
    twitter_desc = models.TextField(max_length=500,)
    youtube_desc = models.TextField(max_length=500,)
    isDraft = models.BooleanField(default=False)
    isScheduled = models.BooleanField(default=False)

    schedule = models.ManyToManyField(Schedule)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, to_field='campaign_id')
