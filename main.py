from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime

Status_Message = ["Once a spy always a spy.", 'You are not just a freaking agent you are more than that you are a spy.', 'Spy are always super cool']

print "Hey There! \nThis is SpyChat \nSo, Let's get started"

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)


def add_status():
    updated_status_message = None

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print "You don't have any status message currently \n"

    default = raw_input("Do you wanna select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you wanna set? ")

        if len(new_status_message) > 0:
            Status_Message.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in Status_Message:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(Status_Message) >= message_selection:
            updated_status_message = Status_Message[message_selection - 1]

    else:
        print 'The option you chose is invalid! \nPress either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print "You currently don't have a status update"

    return updated_status_message


def add_friend():
    new_friend = Spy('', '', 0, 0.0)

    new_friend.name = raw_input("What's your friend's name: ")
    new_friend.salutation = raw_input("What are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("What's their age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("What's thier spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Yeah! Friend Added'
    else:
        print "Sorry! \nIt's an invalid entry. \nWe can't add spy with such details which were provided by you on SpyChat"

    return len(friends)


def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name,
                                                                friend.age,
                                                                friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():
    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text, False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


def read_chat_history():
    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        print "Authentication complete. \nWelcome " + spy.name + "\n of age: " \
              + str(spy.age) + "\nwith rating of: " + str(spy.rating) + " Proud to have you on SpyChat"

        show_menu = True

        while show_menu:
            menu_choices = "What do you wanna do? \n 1. Add a status update \n 2. Add a friend \n 3. Select a friend \n 4. Send a secret message to friends \n 5. Read a secret message from friends \n 6. Read Chats from a friends \n 7. Close the SpyChat \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    index = select_a_friend()
                    print index
                elif menu_choice == 4:
                    send_message()
                elif menu_choice == 5:
                    read_message()
                elif menu_choice == 6:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry! you are not of the proper age to be a spy'


if existing == "Y":
    start_chat(spy)
else:

    spy = Spy('', '', 0, 0.0)

    spy.name = raw_input("Welcome to spy chat, \nYou must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("What should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please enter a valid spy name'