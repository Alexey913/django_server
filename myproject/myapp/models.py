from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_body = models.TextField()
    date_publication = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default='post')
    count_view = models.IntegerField(default=0)
    publication = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.title}'
    
    def get_summary(self):
        body = self.post_body.split()
        return f'{" ".join(body[:3])}...'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date_create = models.DateField()
    date_change = models.DateField()

    def __str__(self) -> str:
        return f'{self.comment}'
