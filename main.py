from config import conf
from functions import *

username=conf["user_name"]
permission_to_write=conf["read_write_permission_acount"]

#Create Database with relationships of the user
set_relations_db(username=username)

#Return a list of the users that you follow but didn't followed you back (those you want to unfollow)
users_to_unfollow=users_to_unfollow_in_db(username=username)

#Display name and username of the users to unfollow
display_users_to_unfollow(users_to_unfollow)

#Unfollow those accounts
if(permission_to_write):
    unfollow_users(users_to_unfollow)
