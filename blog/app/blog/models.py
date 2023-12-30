from django.db.models import Model, CharField, TextField, DateTimeField, ManyToManyField, ForeignKey, CASCADE

class Category(Model):
    name = CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(Model):
    title = CharField(max_length=30)
    author = CharField(max_length=50)
    content = TextField()
    created_on = DateTimeField(auto_now_add=True)
    last_modified = DateTimeField(auto_now=True)
    categories =  ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

def Comment(Model):
    author = CharField(max_length=30)
    body = CharField(max_length=200)
    created_on = DateTimeField(auto_now_add=True)
    post = ForeignKey("Post", on_delete=CASCADE)

