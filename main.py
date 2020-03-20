# mongo engine

from mongoengine import *

connect("mongo-dev-db")


# Defining documents

class User(Document):
    username = StringField(unique=True, required=True)
    email = EmailField(unique=True)

    def json(self):
        user_dict = {
            "username": self.username,
            "email": self.email
        }
        return json.dumps(user_dict)


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

print("Done")