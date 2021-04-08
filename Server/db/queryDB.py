import sqlite3
db_connection = sqlite3.connect('mainDB.db')


#Get user info from user (sign up page)
db_new_user = db.connection.cursor()
db_new_user.execute("INSERT INTO users VALUES ()") 

db_new_user.close()


#Get post content from user (sign up page)
db_new_user = db.connection.cursor()
db_new_user.execute("INSERT INTO posts VALUES ()") 

db_new_user.close()

# Get all posts from DB (Main page)
db_posts = db_connection.cursor()
db_posts.execute("SELECT * FROM posts")
list_posts = db_posts.fetchall()

print("list_posts contents:")
print(list_posts)

#
db_users = db_connection.cursor()
db_users.execute("SELECT * FROM users")
list_users = db_users.fetchall()

print("list_users contents:")
print(list_users)

# Get all posts from a specfic user (Profile page)
db_comments = db_connection.cursor()
db_comments.execute("SELECT * FROM posts Where userId = {}").format(userId)
list_comments = db_users.fetchall()

print("list_comments contents:")
print(list_comments)


