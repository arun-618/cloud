# mongo engine

from mongoengine import *

connect("mongo-dev-db")


# Defining documents

class User(Document):
    username = StringField(unique=True, required=True)
    email = EmailField(unique=True)


class BlogPost(DynamicDocument):
    title = StringField()
    content = StringField()


user = User(
    username="arun",
    email="arunaks618@gmail.com"
).save()

user2 = User(
    username="akshay",
    email="akshay007@gmail.com"
).save()

# Dynamic document

BlogPost(
    title="My first post",
    content="Python is robust"
).save()

for user in User.objects:
    print (user.username)
    print (user.email)

for blog in BlogPost.objects:
    print(blog.title)
    print(blog.content)

print("Done")
