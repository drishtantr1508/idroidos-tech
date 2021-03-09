from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# from django.contrib.contenttypes.fields import GenericRelation,GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
# Create your models here.
class UserProfileInfo(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.TextField(max_length=50)
    middlename=models.TextField(max_length=50,blank=True)
    lastname=models.TextField(max_length=50,blank=True)
    contact=models.PositiveIntegerField(blank=True)

    # def get_asolute_url(self):
    #     return reverse('homepage')
    def __str__(self):
        return self.user.username

# class Comment(models.Model):
#     author=models.CharField(max_length=50)
#     text=models.CharField(max_length=500)
#     create_date=models.DateTimeField(default=timezone.now)
#     approved_comment=models.BooleanField(default=False)
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
#
#     def approve(self):
#         self.approved_comment=True
#
#     def __str__(self):
#         return self.text


class SmartphonesInfo(models.Model):
    smartphone=models.CharField(max_length=50)
    title=models.CharField(max_length=500)
    intro=models.TextField()
    overview=models.TextField()
    display=models.TextField()
    design=models.TextField()
    performance=models.TextField()
    camera=models.TextField()
    battery=models.TextField()
    software=models.TextField()
    extras=models.TextField()
    conclusion=models.TextField()
    display_pic=models.ImageField(blank=True,upload_to='smartphones')
    design_pic=models.ImageField(blank=True,upload_to='smartphones')
    extra_pic=models.ImageField(blank=True,upload_to='smartphones')
    create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    #comments = GenericRelation(Comment)
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.smart_comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("smartphone_list")

    def __str__(self):
        return self.smartphone

class SmartphoneComment(models.Model):
    smartphone= models.ForeignKey(SmartphonesInfo,related_name='smart_comments', on_delete=models.CASCADE)
    author= models.CharField(max_length=100)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse("smartphone_details",kwargs={'pk':self.pk})

    def __str__(self):
        return self.text

class ComparisonInfo(models.Model):
    smartphone_one=models.CharField(max_length=50)
    smartphone_two=models.CharField(max_length=50)
    title=models.TextField()
    intro=models.TextField()
    overview=models.TextField()
    display=models.TextField()
    design=models.TextField()
    performance=models.TextField()
    camera=models.TextField()
    battery=models.TextField()
    software=models.TextField()
    extras=models.TextField()
    conclusion=models.TextField()
    phonepic1=models.ImageField(blank=True,upload_to='comparisons')
    phonepic2=models.ImageField(blank=True,upload_to='comparisons')
    extra_pic=models.ImageField(blank=True,upload_to='comparisons')
    create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    #comments = GenericRelation(Comment)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comparison_comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('comparison_details',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class ComparisonComment(models.Model):
    comparison= models.ForeignKey(ComparisonInfo,related_name='comparison_comments', on_delete=models.CASCADE)
    author= models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse('comparison_details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.text

class NewsArticle(models.Model):
    heading=models.CharField(max_length=300)
    para1=models.TextField()
    para2=models.TextField()
    para3=models.TextField()
    conclusion=models.TextField()
    article_pic1=models.ImageField(blank=True,upload_to='newsarticles')
    article_pic2=models.ImageField(blank=True,upload_to='newsarticles')
    create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    #comments = GenericRelation(Comment)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.news_comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("news_list")


    def __str__(self):
        return self.heading

class NewsComment(models.Model):
    news= models.ForeignKey(NewsArticle,related_name='news_comments', on_delete=models.CASCADE)
    author= models.CharField(max_length=100)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse('news_details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.text


class QuickLinks(models.Model):
    post=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse("homepage")
