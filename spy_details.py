from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Manish', 'Mr.', 21, 4.9)

friend_one = Spy('Sarabjeet', 'Mr.', 20, 4.3)
friend_two = Spy('Manila', 'Mrs.', 22, 4.75)
friend_three = Spy('Aliza', 'Dr.', 23, 4.99)


friends = [friend_one, friend_two, friend_three]