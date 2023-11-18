from peewee import SqliteDatabase, Model, CharField, IntegerField
import os
os.remove("users3.db")
db = SqliteDatabase("users3.db")


class User(Model):
    username = CharField(unique=True)
    age = IntegerField()

    class Meta:
        database = db


class Pet(Model):
    petname = CharField(unique=True)
    petbreed = CharField()

    class Meta:
        database = db


db.connect()

db.create_tables([User, Pet])

new_user = User(username="john", age=30)
new_user.save()
new_user = User(username="andy", age=22)
new_user.save()
new_user = User(username="fred", age=45)
new_user.save()
new_pet = Pet(petname="Ben", petbreed="Retriever")
new_pet.save()
all_users = User.select()
for user in all_users:
    print(f"Username: {user.username}, Age: {user.age}")

user_to_update = User.get(username="john")
user_to_update.age = 35
user_to_update.save()

user_to_delete = User.get(username="john")
user_to_delete.delete_instance()


db.close()
