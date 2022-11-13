# Tweepy-workshop
# @Author: [Steeve-Dominique HEUNA MBIAFENG](https://www.linkedin.com/in/steeve-dominique-heuna-mbiafeng-06690516b/)
This project's purpose is to teach how to simply use Tweepy( Twitter API ) and achieve Neo4j Cipher queries with students in a lab and also learn a way to build a project.

## GOAL: 
Given a username that is specified in the config file we should be able to get a list of user he follows that didn't followed him back using a cipher query, and also unfollow them if we have the good rights.
The relationship between the user and his contacts should be avaible in the graph database

## SETUP
**PRE-REQUISITES for Python:**

python 3.11.0 (If you don't have it, download here - [Installation file](https://www.python.org/downloads/release/python-3110/))

### Dependencies installation
To run scripts on your machine, it will be necessary to install python's
 dependency libraries. The file lists the dependencies is on requirements.txt file
 Make sure to be in the folder containing your python.exe file (If you have python in the system variable path don't mind this advise) 
 Execute the following command to setup the requirements:
```
pip install -r requirements.txt
```

**PRE-REQUISITES for Neo4j:**
Neo4j 4.x.x (If you don't have it, download here - [Installation file](https://neo4j.com/download/?ref=get-started-dropdown-cta))

### Setup Neo4j database and learn cipher
If you are not familiar to Neo4j use this [link](https://www.tutorialspoint.com/neo4j/neo4j_environment_setup.htm) to follow a complete tutorial about the installation and how to write Cipher queries
Make sure to start the neo4j database service before running your python scripts

### Configuration
#### Tweeter API credentials
You need first to access to Twitter api to be able to use Tweepy. In order to achieve this, create your account if it is not already done by using this [link](https://developer.twitter.com/en/portal/petition/essential/basic-info).
Once you will achieve the creation you will get 4 keys  that will be needed in the next steps 
#### ![image](https://user-images.githubusercontent.com/73309628/201518578-10d33fc7-d510-4fad-98b7-9ddac72d75a9.png)
These keys will help you setting up your config.py that contains the credentials you need to use Twitter API

```
conf={
    "api_key":"<your api key>",
    "api_secret_key":"<your api secret key>",
    "bearer_token":""<your bearer token>",
    "access_token_key":"<your access token>",
    "access_token_secret":"<your token secret>",
    ...
    }
```

Use the credentials of your neo4j graphbase to complete the database part of the config.py

```
conf={...,
    "url_db":"<url to your Neo4j database >",         eg: "neo4j:7474/browser/"
    "user_db":"<username of the database >",
    "password_db":"<password to access database>",
    "db_name":"<database name>",
    ...
    }
```

Set the username parameter with your twitter account username and if your Twitter API account has Elevated or Academic Access set read_write_permission_acount to True

```
conf={...,
    "user_name":<"your twitter username">,
    "read_write_permission_acount":False
}
```

## CONSUME Project

Once you finished setting up the parameters, you can then run the main.py

