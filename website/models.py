from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    info=models.CharField(max_length=200)
    description=models.CharField(max_length=1000,null=True)
    img_project=models.FileField()
    homePage=models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url=self.img_project.url
        except:
            url=''
        return url



class imageProject(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    imgproj=models.FileField()
    
    @property
    def imageURL(self):
        try:
            url=self.imgproj.url
        except:
            url=''
        return url

class getInTouch(models.Model):
    name=models.CharField(max_length=200)
    subject=models.CharField(max_length=300)
    email=models.CharField(max_length=100)
    message=models.TextField(max_length=2000)

    
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse ('portfolio:index',kwargs={'pk': self.pk})

class Info(models.Model):
    homeTitle=models.CharField(max_length=200)
    previewTitle=models.CharField(max_length=200)
    previewInfo=models.CharField(max_length=700)
    moreInfo=models.CharField(max_length=700)
    moreInfo2=models.CharField(max_length=700)
    expertise=models.CharField(max_length=700)
    profileImage=models.ImageField(null=True)
    socialImage=models.ImageField(null=True)
    resume=models.FileField(null=True)

   
    def __str__(self):
       return self.homeTitle

    
class Skills(models.Model):
    skillname=models.CharField(max_length=200)
    def __str__(self):
        return self.skillname
