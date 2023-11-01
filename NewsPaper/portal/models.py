from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default = 0)

    def update_rating(self):
        self.rating = 0
        post = list(Post.objects.filter(author = self.user).values('rating'))
        for i in post:
            self.rating += i['rating']
        self.rating *= 3
        comments = list(Comment.objects.filter(author=self.user).values('rating'))
        for post in list(Post.objects.filter(author=self.user)):
            comments += Comment.objects.filter(post=post).values('rating')
        for dict in comments:
            for p in dict.values():
                self.rating += p



class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.BooleanField(default=False) #False - новость, true - статья
    create_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default = 0)

    category = models.ManyToManyField(Category, through='PostCategory')
    def like(self):
        self.rating +=1


    def dislike(self):
        self.rating -= 1

    def preview(self):
        return self.text[:124:] + '...'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default = 0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    def comments(self):
        text = ''
        com_list = Comment.objects.filter(post=self.post)
        for c in com_list:
            text += f"[{c.create_time}] {c.author}: <{c.text}> rating: {c.rating}\n"
        return text



