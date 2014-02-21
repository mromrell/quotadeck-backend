from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    ''' Creates a token whenever a User is created '''
    if created:
        Token.objects.create(user=instance)


class Address(models.Model):
    ''' Model features for an address '''
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.street, self.city, self.state)

    class Meta:
        verbose_name_plural = 'Address'


class Company(models.Model):
    companyName = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    employeeCount = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    productsServices = models.CharField(max_length=200, blank=True, null=True)
    companyDescription = models.CharField(max_length=1000, blank=True, null=True)
    companyType = models.CharField(max_length=200, blank=True, null=True)  # ex: public, private, government etc..
    dateJoined = models.DateField(default=datetime.now, blank=True, null=True)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.companyName, self.industry, self.state)

    class Meta:
        verbose_name_plural = 'Company'


class CompanyUser(models.Model):
    user = models.ForeignKey(User)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(Company)
    dateJoined = models.DateField(default=datetime.now)

    def __unicode__(self):
        return u'%s, %s' % (self.user, self.company)

    class Meta:
        verbose_name_plural = 'CompanyUser'


class SalesUser(models.Model):
    user = models.ForeignKey(User)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    productsServices = models.CharField(max_length=200, blank=True, null=True)
    salePriceLow = models.IntegerField(blank=True, null=True)
    salePriceHigh = models.IntegerField(blank=True, null=True)
    userDescription = models.CharField(max_length=1000, blank=True, null=True)
    contacts = models.CharField(max_length=2000, blank=True, null=True)
    dateJoined = models.DateField(default=datetime.now)

    def __unicode__(self):
        return u'%s, %s' % (self.user, self.industry)

    class Meta:
        verbose_name_plural = 'SalesUser'


class Job(models.Model):
    user = models.ForeignKey(User)
    company = models.ForeignKey(Company)
    dateAdded = models.DateField(default=datetime.now)
    listingTitle = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    startDate = models.CharField(max_length=200)
    totalCost = models.CharField(max_length=200)
    commissionAmount = models.CharField(max_length=200)
    linkUrl = models.CharField(max_length=200)

    

    def __unicode__(self):
        return u'%s, %s' % (self.jobTitle, self.company)

    class Meta:
        verbose_name_plural = 'Job'


class Application(models.Model):
    user = models.ForeignKey(User)
    job = models.ForeignKey(Job)
    dateApplied = models.DateField(default=datetime.now)
    appTitle = models.CharField(max_length=200, blank=True, null=True)
    appDescription = models.CharField(max_length=200, blank=True, null=True)
    appCost = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.job, self.user, self.dateApplied)

    class Meta:
        verbose_name_plural = 'Application'


class Chat(models.Model):
    user = models.ForeignKey(User)
    job = models.ForeignKey(Job)
    company = models.ForeignKey(Company)
    dateSent = models.DateField(default=datetime.now, blank=True, null=True)
    chatContent = models.CharField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.job, self.user, self.dateSent)

    class Meta:
        verbose_name_plural = 'Chat'


class Rating(models.Model):
    user = models.ForeignKey(User)
    job = models.ForeignKey(Job)
    company = models.ForeignKey(Company)
    dateRated = models.DateField(default=datetime.now, blank=True, null=True)
    ratingDetails = models.CharField(max_length=1000, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True, max_length=2)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.job, self.user, self.dateSent)

    class Meta:
        verbose_name_plural = 'Chat'
