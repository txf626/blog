from django.db import models

class Banner(models.Model):
    name = models.CharField(max_length=20)
    name_alis = models.CharField(max_length=20)
    father_node = models.IntegerField()
    keyword = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    class Meta:
        db_table = 'banner'

class Article(models.Model):
    title = models.CharField(max_length=50)
    keyword = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    label = models.CharField(max_length=20)
    img = models.ImageField(upload_to='article')
    content = models.CharField(max_length=20000,default=None)
    father_node = models.ForeignKey(Banner)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'article'

class User(models.Model):
    name = models.CharField(max_length=20)
    new_password = models.CharField(max_length=100)
    old_password = models.CharField(max_length=100)
    tel = models.CharField(max_length=25)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class Token(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    user = models.OneToOneField(User)

    class Meta:
        db_table = 'token'