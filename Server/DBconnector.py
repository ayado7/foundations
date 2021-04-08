
import sqlite3
import time
from random import randint


# setup DB connection
db_connection = sqlite3.connect('db/mainDB.db')
db_cursor = db_connection.cursor()

# add new user
def newUser(userName, password):
    db_connection = sqlite3.connect('db/mainDB.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute ('INSERT INTO users (userName, password) VALUES ("{}","{}")'.format(userName, password))
    
    db_connection.commit()
    db_connection.close()

# Authenticate user
def checkUser(userName, password):
    db_connection = sqlite3.connect('db/mainDB.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT userName, password, userId from users WHERE userName = "{}" AND password = "{}"'.format(userName, password))
    result = db_cursor.fetchone()
    db_connection.close()
    return result

# add new post
def newPost(storyContent, userId):
    db_connection = sqlite3.connect('db/mainDB.db')
    db_cursor = db_connection.cursor()
    # We need to generate a random number ((find a way for a serial number)) for each post so we can call it back, while we get the username and Id from the active cookie session
    postId = randint(0,1000000000)
    db_cursor.execute ('INSERT INTO posts (input, userId, postId) VALUES ("{}","{}","{}")'.format(storyContent, userId, postId))
    db_connection.commit()
    
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT * from posts WHERE postId = "{}"'.format(postId))
    newPost = db_cursor.fetchall()
    db_connection.close()
    return newPost

# main page: Get all posts ((FINALIZE))
def get_all_posts():
    db_connection = sqlite3.connect('db/mainDB.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * from posts")
    result = db_curser.fetchall()
    db_connection.close()
    return get_all_posts

# Profile page: Get all posts from one user ((FINALIZE))
def get_all_user_posts():
    db_connection = sqlite3.connect('db/mainDB.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * from posts WHERE userId = {}".format(userId))
    result = db_cursor.fetchall()
    db_connction.close()
    return result


