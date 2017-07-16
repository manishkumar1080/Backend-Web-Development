import requests, urllib                                                                                         #This statement is used for importing the requests library
from termcolor import colored                                                                                   #This statement is used for importing the colored module from termcolor library
from graph import generate_words                                                                                #This statement is used for importing the generate_word function from graph file

#This is access token generated from instagram api
APP_ACCESS_TOKEN = ''                                                                                           #In the single quotes the acess token is the entered for running the InstaBot

BASE_URL = 'https://api.instagram.com/v1/'

#This is the function used for fetching self information of the user
def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'Sorry!\n User does not exist!'
    else:
        print 'Status code other than 200 received!'


#This is the function used for fetching instagram user id of the another user
def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


#This is the function used for fetching the information of the another instagram user
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'Sorry!\n User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data available for this user!'
    else:
        print 'Status code other than 200 received!'


#This is the function used for fetching the own insatgram posts of the instagram user
def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


#This is the function used for fetching the instagram posts of another instagram user
def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'Sorry!\n User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Yeah! your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'



#This is the function used for fetching instagram post if of the instagram user
def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "Sorry!\n User does not exist!"
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print "There is'nt any recent post available of the user!"
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()



#This is the function used for  posting a like the instagram posts of the instagram user
def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Yeah!\n Your like was successful!'
    else:
        print 'Sorry!\n Your like was unsuccessful.\n Please Try again!'



#This is the function used for posting a comment on the instagram post of the instagram user
def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment.\n PLease Try again!"



#This is the function used for fetching a list of comments on an instagram post of the instagram user
def get_comment_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    get_a_comment = requests.get(request_url).json()
    print get_a_comment
    if get_a_comment['meta']['code'] == 200:
        x=1
        for temp in get_a_comment['data']:
            print "%d. %s : %s"%(x,temp['from']['username'],temp['text'])
            x=x+1
    else:
        text = colored('Your comment was unsuccessful. Please Try again!', "red")
        print text



#This is the function used for fetching the hashtags of trends and the subtrends occuring on the instagram from a instagram user's posts
def tag_name(insta_username):

    media_id=get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    tag_trends= requests.get(request_url).json()
    print tag_trends

    if tag_trends['meta']['code']==200:
        file = open("wordcloud.txt", "w")
        for item in tag_trends['data']['caption']['text']:
            file.write(item)
        file.close()

    else:
        print 'Status code other than 200 received!'
        exit()




#From here the InstaBot starts and the intro gets displayed in differnet colors from the colored module of the termcolor library
#This is function used for satrting the InstaBot and loading all the options
def start_bot():
    while True:
        print '\n'
        text = colored('Hey There! \nWelcome to InstaBot!', "blue")
        print text
        text = colored('Here We Go', 'green')
        print text

        #From here the all the menu options are displayed in different colors from the colored module of the termcolor library
        text = colored('So here is your Menu:', "yellow")
        print text
        text = colored("For fetching your own details \n Press 1\n", "magenta")
        print text
        text = colored("For fetching details of a user by username\n Press 2\n", "green")
        print text
        text = colored("For fetching your own recent posts\n Press 3\n", "magenta")
        print text
        text = colored("For fetching the recent post of a user by its username\n Press 4\n", "green")
        print text
        text = colored("For liking the recent post of a user\n Press 5\n", "green")
        print text
        text = colored("For fetching a list of comments on the recent post of a user\n Press 6\n", "magenta")
        print text
        text = colored("For making a comment on the recent post of a user\n Press 7\n", "green")
        print text
        text = colored("For fetching trends & subtrends\n Press 8\n", "magenta")
        print text

        #These statements are used for exiting the user from the InstaBot
        text = colored("For Exiting the InstaBot \nPress 0", "red")
        print text


         #From here the user inputs his or her choice whichever option he or she wants to use
        choice = raw_input("Please! Enter you choice: ")
        if choice == "1":
            self_info()
        elif choice == "2":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == "5":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice == "6":
            insta_username = raw_input("Enter the username of the user: ")
            get_comment_list(insta_username)
        elif choice == "7":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)
        elif choice == "8":
            insta_username = raw_input("Enter the username of the user: ")
            tag_name(insta_username)
            generate_words()

        elif choice == "0":
            exit()
        #These statements are used if the a user inputs an invalid option then a special message is displayed to the user
        else:
            text = ("Sorry! \n It's an invalid option", "red")
            print text

#Here the startbot function is lastly called
start_bot()
