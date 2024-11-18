from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

class AdwaitappContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    map = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adwaitapp_contact'

class AdwaitappMainServices(models.Model):
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    show = models.SmallIntegerField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    dept_id_id = models.BigIntegerField()
    img = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    seo_keywords = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adwaitapp_main_services'


class AdwaitappSubServices(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)
    main_service_id_id = models.BigIntegerField()
    img = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    seo_keywords = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adwaitapp_sub_services'

class AdwaitappInquiries(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'adwaitapp_inquiries'

class AdwaitappTechnologies(models.Model):
   name = models.CharField(max_length=255)
   icon = models.CharField(max_length=100, blank=True, null=True)
   main_service_id = models.ManyToManyField(AdwaitappMainServices)
   
   class Meta:
        managed = False
        db_table = 'adwaitapp_technologies'

class AdwaitappTechnologiesService(models.Model):
    main_services = models.ForeignKey(AdwaitappMainServices, on_delete=models.CASCADE)
    technologies = models.ForeignKey(AdwaitappTechnologies, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'adwaitapp_technologies_service'

class AdwaitappBlogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateTimeField()
    subject = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    dept_id_id = models.BigIntegerField()
    main_service_id_id = models.BigIntegerField()
    seo_keywords = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adwaitapp_blogs'
    
    def get_absolute_url(self):
        # return reverse('blog', kwargs={'item_name': self.url}) #it also works
        return f'/blog/{self.url}'

class AdwaitappNewsletterSubscriber(models.Model):
   email = models.EmailField(max_length=255)
   subscribed_on = models.DateTimeField(default=datetime.now)
   
   class Meta:
        managed = False
        db_table = 'adwaitapp_newslettersubscriber'