import psycopg2
db_connection = psycopg2.connect('mainDB.db')


#Get user info from user (sign up page)
db_new_user = db_connection.cursor()
db_new_user.execute("INSERT INTO users DEFAULT VALUES") 
db_connection.commit()
db_new_user.close()

#Get post content from user (sign up page)
db_new_post = db_connection.cursor()
db_new_post.execute("INSERT INTO posts DEFAULT VALUES") 
db_connection.commit()
db_new_post.close()

# Get all posts from DB (Main page)
db_posts = db_connection.cursor()
db_posts.execute("SELECT * FROM posts")
list_posts = db_posts.fetchall()

print("list_posts contents:")
print(list_posts)

# Get all posts from a specfic user (Profile page)
#db_comments = db_connection.cursor()
#db_comments.execute("SELECT * FROM posts Where userId = {}").format(userId)
#list_comments = db_users.fetchall()

print("list_user_posts contents:")
print(list_user_posts)

# Close database connection
db_connection.close()
