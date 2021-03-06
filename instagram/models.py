from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
#a part of a URL which identifies a particular page on a website in a form readable by users-->slugify

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  bio = models.TextField(default='Happy to code. Share since its caring', max_length=500, blank=True)
  photo = models.ImageField(default='profile.jpg', upload_to='photos/')
  name = models.CharField(max_length=200)

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()

  def update_profile(self, id, updated_bio):
    profile = Profile.objects.filter(pk=id).update(bio = updated_bio)
    return profile.save_profile()

  @classmethod
  def search_profile(cls, search):
    profile = cls.objects.filter(user__username__icontains=search)
    return profile

  def __str__(self):
    return self.user.username

class Image(models.Model):
  image = models.ImageField(blank=True, upload_to='photos/')
  image_name = models.CharField(max_length = 61)
  image_caption = models.CharField(max_length = 61)
  posted_at = models.DateTimeField(auto_now_add=True)
  likes = models.ManyToManyField(User, blank=True, related_name='likes')
  slug = models.SlugField()
  profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  comments= models.TextField()

  def save_image(self):
    self.slug = slugify(self.image_name)
    return super(Image, self).save()

  def delete_image(self):
    self.delete()

  def update_profile(self, id, updated_caption):
    image = Image.objects.filter(pk=id).update(image_caption = updated_caption)
    return image.save_image()

  @classmethod
  def get_images(cls):
    images = cls.objects.all()
    return images

  def get_likes(self):
    return self.likes.count()

  def __str__(self):
    return self.image.url

  
class Comment(models.Model):
   posted_by=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
   comment_pic=models.ForeignKey(Image,on_delete=models.CASCADE,null=True)
   comment=models.CharField(max_length=20,null=True)
   def __str__(self):
       return self.posted_by


# cls methode: states that the methode is for the same class
#self specifies that the methode is of the class instance
#pk is the attribute that contains the value of the primary key for the model. id is the name of the field created as a primary key by default if none is explicitly specified