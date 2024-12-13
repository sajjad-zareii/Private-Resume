from django.db import models


#Form Class control in Views
class Message(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f"{self.name}-{self.email}"


#Category Class control in Admin
class Category(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




#Articles Class control in Admin
class Article(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}-{self.body[:30]}"


#News Class control in Admin
class News(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title}-{self.body[:30]}"


    class Meta:
        ordering=('-created',)





