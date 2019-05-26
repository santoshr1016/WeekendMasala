from operator import attrgetter


class User:
    def __init__(self, idd):
        self.user_id = idd

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(11), User(9), User(1), User(99), User(5)]
print(users)

# attrgetter() is often a tad bit faster
print(sorted(users, key=attrgetter('user_id')))

print(sorted(users, key=lambda u: u.user_id))