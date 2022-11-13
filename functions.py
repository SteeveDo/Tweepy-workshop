import tweepy
from neo4j import GraphDatabase
from config import conf

consumer_key=conf["api_key"]
consumer_secret=conf["api_secret_key"]
access_token_key=conf["access_token_key"]
access_token_secret=conf["access_token_secret"]
bearer_token=conf["bearer_token"]

url=conf["url_db"]
user=conf["user_db"]
password=conf["password_db"]
driver = GraphDatabase.driver(url, auth=(user, password))
username=conf["user_name"]
database=conf["db_name"]

session=driver.session(database=database)


#Create Twitter Client
def create_client():
    client=tweepy.Client(
    bearer_token,consumer_key, consumer_secret, access_token_key, access_token_secret
    )
    return client

client=create_client()
    
#Fetch user we will use to make the unfollow/follow request
def get_user_by_username(username,client=client):
    user=client.get_user(username=username)
    #id_user=user.data["id"]
    return user.data

#Fetch users followed by the user
def get_following_accounts(id_user,client=client):
    users_following=client.get_users_following(id=id_user)

    return users_following.data

#Fetch users that follows the user
def get_followers_accounts(id_user,client=client):
    users_that_follows=client.get_users_followers(id=id_user)
    
    return users_that_follows.data

def execute_query(query,session=session):
    result=session.run(query)

    return result

#Create data nodes
def create_node(user,session=session):
    username=user["username"]
    id_twitter=user["id"]
    name=user["name"]
    
    query="MERGE (node:personne {" + "id_twitter:" + f"'{id_twitter}'," +"username: "+f"'{username}',"+"name:"+f"'{name}'"+"})"
    try:
        execute_query(query,session)
        return({
            "message":f"Noeud créé pour le user {username}",
            "status":1
                })
    except:
        return({
            "message":"Erreur de création du noeud",
            "status":0
            })
def following_relations(user_1,user_2,session=session):

    for user in [user_1,user_2]:
        username=user["username"]
        id_twitter=user["id"]
        name=user["name"]
        #check if node exists
        create_node(user,session=session)

    #create relation
    query=f"""MATCH (a:personne), (b:personne) 
        WHERE a.id_twitter = '{user_1["id"]}' AND b.id_twitter = '{user_2["id"]}'
        MERGE (a)-[: follows]->(b)
            """
    execute_query(query)

#Set data base
def set_relations_db(username,client=client,session=session):
    user=get_user_by_username(username=username)
    create_node(user)

    users_following=get_following_accounts(id_user=user["id"],client=client)
    users_followers=get_followers_accounts(id_user=user["id"],client=client)
    print("Database being created...")
    for u in users_following:
        following_relations(user,u)
        
    for u in users_followers:
        following_relations(u,user)
    print("Database created!")

def users_to_unfollow_in_db(username,session=session):
    user=get_user_by_username(username)
    key="{id_twitter: '"+str(user['id'])+"'}"

    query=f"""
            MATCH(n:personne)<-[r:follows]-(m:personne {key})
            WHERE NOT (n)-[:follows]->(m)
            RETURN n
    """
    result=execute_query(query)
    users_to_unfollow=[]
    for r in result:
        users_to_unfollow.append(r.data()["n"])
    return users_to_unfollow

def display_users_to_unfollow(users_to_unfollow):
    for user in users_to_unfollow:
        print(f" Name: {user['name']}\t Username: {user['username']}\n")
        
def unfollow_users(users_to_unfollow,client=client,session=session):
    
    for user in users_to_unfollow:
        client.unfollow_user(user["id"]) #If you have Read-write account you will be able to unfollow/follow
    print("Successfully unfollowed those who didn't followed you back")
