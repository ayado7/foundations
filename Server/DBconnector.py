
import psycopg2
from psycopg2 import sql
import time
from random import randint
from datetime import datetime


# setup DB connection
def create_connection():
    try: 
        return psycopg2.connect(
            dbname="postgres",
            user="postgres.bqkalputmhzdcauhpzza",
            password="ziPKGpyswsvCIExB",
            host="aws-0-eu-central-1.pooler.supabase.com",
            port="5432"
        )
    
    except psycopg2.Error as error:
        print("Error in connecting to PostgreSQL database")
        raise error
    
# add new user
def newUser(userName, password):
    db_connection = create_connection()
    db_cursor = db_connection.cursor()
    query = sql.SQL('INSERT INTO users (userName, password) VALUES (%s, %s)')
    db_cursor.execute(query, (userName, password))
    db_connection.commit()
    db_connection.close()

# Authenticate user
def checkUser(userName, password):
    db_connection = create_connection()
    db_cursor = db_connection.cursor()
    query = sql.SQL('SELECT userName, password, userId from users WHERE userName = %s AND password = %s')
    db_cursor.execute(query, (userName, password))
    result = db_cursor.fetchone()
    db_connection.close()
    return result

# add new post
def newPost(storyContent, userId):
    db_connection = create_connection()
    db_cursor = db_connection.cursor()
    # We need to generate a random number ((find a way for a serial number)) for each post so we can call it back, while we get the username and Id from the active cookie session
    postId = randint(0,1000000000)
    createdAt = datetime.now()
    query = sql.SQL('INSERT INTO posts (input, userId, postId, createdAt) VALUES (%s, %s, %s, %s)')
    db_cursor.execute(query, (storyContent, userId, postId, createdAt))
    db_connection.commit()
    query = sql.SQL('SELECT * from posts WHERE postId = %s')
    db_cursor.execute(query, (postId,))
    newPost = db_cursor.fetchall()
    db_connection.close()
    return newPost

def deletePost(postId):
    db_connection = create_connection()
    db_cursor = db_connection.cursor()
    query = sql.SQL('DELETE FROM comments WHERE postId = %s')
    db_cursor.execute(query, (postId,))
    query = sql.SQL('DELETE FROM posts WHERE postId = %s')
    db_cursor.execute(query, (postId,))
    db_connection.commit()
    db_connection.close()
    return True

# main page: Get all posts
def get_all_posts():
    db_connection = create_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * from posts ORDER BY createdAt DESC")
    result = db_cursor.fetchall()
    db_connection.close()
    return result

# post page: get post text from post id
def get_post_id(postId):
    db_connection = create_connection()
    db_cursor = db_connection.cursor()
    query = sql.SQL('SELECT * from posts WHERE postId = %s')
    db_cursor.execute(query, (postId,))
    result = db_cursor.fetchall()
    db_connection.close()
    return result


# Profile page: Get all posts from one user
def get_all_user_posts(userId):
    db_connection = create_connection()
    db_cursor = db_connection.cursor()
    query = sql.SQL("SELECT * from posts WHERE userId = %s")
    db_cursor.execute(query, (userId,))
    result = db_cursor.fetchall()
    db_connection.close()
    return result


# add new comment to post
def newComment(commentContent, postId, userId):
    db_connection = create_connection()
    db_cursor = db_connection.cursor()
    # We need to generate a random number ((find a way for a serial number)) for each post so we can call it back, while we get the username and Id from the active cookie session
    commentId = randint(0,1000000000)
    createdAt = datetime.now()
    query = sql.SQL('INSERT INTO comments (commentinput, postid, userid, commentid, createdat) VALUES (%s, %s, %s, %s, %s)')
    db_cursor.execute(query, (commentContent, postId, userId, commentId, createdAt))
    db_connection.commit()
    
    query = sql.SQL('SELECT * from comments WHERE commentid = %s')
    db_cursor.execute(query, ( commentId, ))
    newComment = db_cursor.fetchall()
    db_connection.close()
    return newComment

def get_comments(postId):
    db_connection = create_connection()
    db_cursor = db_connection.cursor()
    query = sql.SQL('SELECT * from comments WHERE postId = %s')
    db_cursor.execute(query, (postId,))
    result = db_cursor.fetchall()
    db_connection.close()
    return result

def get_profile(userId):
    db_connection = create_connection()
    db_cursor = db_connection.cursor()
    query = sql.SQL('SELECT * from posts WHERE userId = %s')
    db_cursor.execute(query, (userId))
    result = db_cursor.fetchall()
    db_connection.close()
    return result