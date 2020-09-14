from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save
import datetime


from django.contrib.auth.models import User


# Create your models here.

#---------------------------------
#++++++++RESEARCH GROUPS++++++++++
#---------------------------------

class ResearchGroups(models.Model):
    title = models.CharField(max_length=245)
    slug = models.SlugField(max_length=250,unique=True,editable=False,null=False)
    information = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def unique_slug(self, slug, new_slug, idx):
        if ResearchGroups.objects.filter(slug=new_slug):
            
            new_slug = '{}-{}'.format(slug,idx)
            idx += 1
            return self.unique_slug(slug, new_slug, idx)
        return new_slug

    def save(self, *args, **kwargs):
        idx = 1
        new_slug = slugify(self.title)
        self.slug = self.unique_slug(new_slug, new_slug, idx)
        super(ResearchGroups,self).save(*args,**kwargs)

    class Meta:
        ordering = ['createDate']

#---------------------------------
#++++++++++USER_PROFILE+++++++++++
#---------------------------------
def user_upload_to(instance,filename):
    return "{}/{}/{}".format('profiles',instance.user.username,filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250,unique=True,editable=False,null=False)
    profile_photo = models.ImageField(upload_to=user_upload_to,blank=True,default='profiles/user_default.jpg')
    researchGroup = models.ManyToManyField(ResearchGroups)
    information = RichTextField(blank=True)
    linkedin = models.CharField(max_length=255,blank=True)
    twitter = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.user.get_full_name()

    def unique_slug(self, slug, new_slug, idx):
        if UserProfile.objects.filter(slug=new_slug):
            new_slug = '{}-{}'.format(slug,idx)
            idx += 1
            return self.unique_slug(slug, new_slug, idx)
        return new_slug

    def save(self, *args, **kwargs):
        idx = 1
        fullName = self.user.get_full_name()
        new_slug = slugify(fullName)
        self.slug = self.unique_slug(new_slug, new_slug, idx)
        super(UserProfile,self).save(*args,**kwargs)

    def update(self, *args, **kwargs):
        idx = 1
        fullName = self.user.get_full_name()
        new_slug = slugify(fullName)
        self.slug = self.unique_slug(new_slug, new_slug, idx)
        super(UserProfile,self).update(*args,**kwargs)

def create_profile(instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)

#---------------------------------
#+++++++++++++++NEWS++++++++++++++
#---------------------------------

class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250,unique=True,editable=False,null=False)
    content = RichTextUploadingField()
    excerpt = models.TextField()
    author = models.ForeignKey(User,related_name='News',on_delete=models.SET_NULL,null=True,editable=False)
    researchGroup = models.ForeignKey(ResearchGroups,related_name='News',on_delete=models.SET_NULL,null=True)
    draft = models.BooleanField(default=False)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def unique_slug(self, slug, new_slug, idx):
        if News.objects.filter(slug=new_slug):
            
            new_slug = '{}-{}'.format(slug,idx)
            idx += 1
            return self.unique_slug(slug, new_slug, idx)
        return new_slug

    def save(self, *args, **kwargs):
        idx = 1
        new_slug = slugify(self.title)
        self.slug = self.unique_slug(new_slug, new_slug, idx)
        super(News,self).save(*args,**kwargs)

    class Meta:
        ordering = ['-createDate']


#---------------------------------
#+++++++++++++PROJECT+++++++++++++
#---------------------------------

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250,unique=True,editable=False,null=False)
    content = RichTextUploadingField()
    excerpt = models.TextField()
    duration = models.CharField(max_length=50)
    involvedPeople = models.ManyToManyField(UserProfile)
    researchGroup = models.ForeignKey(ResearchGroups,related_name='Project',on_delete=models.SET_NULL,null=True)
    draft = models.BooleanField(default=False)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def unique_slug(self, slug, new_slug, idx):
        if Project.objects.filter(slug=new_slug):
            new_slug = '{}-{}'.format(slug,idx)
            idx += 1
            return self.unique_slug(slug, new_slug, idx)
        return new_slug

    def save(self, *args, **kwargs):
        idx = 1
        new_slug = slugify(self.title)
        self.slug = self.unique_slug(new_slug, new_slug, idx)
        super(Project,self).save(*args,**kwargs)

    class Meta:
        ordering = ['-createDate']

#---------------------------------
#+++++++++++++RESEARCH++++++++++++
#---------------------------------

class Research(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250,unique=True,editable=False,null=False)
    content = RichTextUploadingField()
    excerpt = models.TextField()
    duration = models.CharField(max_length=50)
    involvedPeople = models.ManyToManyField(UserProfile)
    researchGroup = models.ForeignKey(ResearchGroups,related_name='Research',on_delete=models.SET_NULL,null=True)
    draft = models.BooleanField(default=False)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def unique_slug(self, slug, new_slug, idx):
        if Research.objects.filter(slug=new_slug):
            new_slug = '{}-{}'.format(slug,idx)
            idx += 1
            return self.unique_slug(slug, new_slug, idx)
        return new_slug

    def save(self, *args, **kwargs):
        idx = 1
        new_slug = slugify(self.title)
        self.slug = self.unique_slug(new_slug, new_slug, idx)
        super(Research,self).save(*args,**kwargs)

    class Meta:
        ordering = ['-createDate']


#---------------------------------
#+++++++++++PUBLICATION+++++++++++
#---------------------------------

year_choices = [(r,r) for r in range(1984, datetime.date.today().year+1)]

current_year =datetime.date.today().year

class Publication(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(choices=year_choices, default=current_year)
    information = RichTextUploadingField(blank=True)
    links = RichTextField(blank=True)
    pdf = models.FileField(blank=True)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-year']

#---------------------------------
#++++++++++++RESOURCE+++++++++++++
#---------------------------------

class Resource(models.Model):
    title = models.CharField(max_length=255)
    information = RichTextUploadingField()
    link = models.CharField(max_length=255)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']