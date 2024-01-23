class User:
    name: str
    age: int
    followers: int
    following: int
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following +=1

    

user1 = User("Brayan", 18)
user2 = User("Andres", 25)

print(f"Hello my name is {user1.name} and I am {user1.age} years old")
user1.follow(user2)
print(f"User1 followers: {user1.followers}, following: {user1.following}")
print(f"User2 followers: {user2.followers}, following: {user2.following}")
