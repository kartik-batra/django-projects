from django.contrib import admin
from .models import SocialAccount, UserPost, Campaign, Schedule
# Register your models here.
@admin.register(SocialAccount)
class AdminSocialAccount(admin.ModelAdmin):
    list_display = ['user_id', 'account_type', 'access_token']

@admin.register(UserPost)
class AdminUserPost(admin.ModelAdmin):
    list_display = ['id','user_id',SocialAccount, 'description', 'attachments', 'insta_desc', 'insta_story', 'insta_first_comment',
                    'linkedin_desc', 'pinterest_desc', 'twitter_desc', 'youtube_desc', 'isDraft', 'isScheduled',Schedule, 'campaign']

@admin.register(Campaign)
class AdminCampaign(admin.ModelAdmin):
    list_display = ['campaign_id', 'name', 'date', 'description', 'status']

@admin.register(Schedule)
class AdminSchedule(admin.ModelAdmin):
    list_display = ['schedule_id', 'date_time', 'time_zone']
