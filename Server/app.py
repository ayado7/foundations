
from flask import Flask, jsonify, send_file, redirect, request, make_response
from flask_login import current_user, login_user
from flask_cors import CORS 

app = Flask (__name__)
import DBconnector

CORS(app, resources={r"/api/*": {"origins": ["http://34.107.19.83/" , "http://3.75.158.163" , "http://3.125.183.140" , "http://35.157.117.28" ]}})

@app.route('/')
def main():
    if 'authenticated_user' not in request.cookies:
        return redirect("/sign-in", code=302)
    return send_file("static/html/index.html",conditional=True)

@app.route('/sign-up')
def signUp():
    return send_file("static/html/sign-up.html")

@app.route('/sign-in')
def signIn():
    return send_file("static/html/sign-in.html")

#@app.route('/index')
#def index():
    #return send_file("static/html/index.html")

@app.route('/profile')
def profile():
    if 'authenticated_user' not in request.cookies:
        return redirect("/sign-in", code=302)
    return send_file("static/html/profile.html")

@app.route('/post/<postId>')
def post(postId):
    if 'authenticated_user' not in request.cookies:
        return redirect("/sign-in", code=302)
    return send_file("static/html/post.html")

@app.route('/api/signup', methods= ['POST'])
def signup(): 
    app.logger.debug("request is:", request, "data is", request.data)
    data = str(request.data) 
    args = data.split("&") 
    username = args[0].split("=")[1]
    password = args[1].split("=")[1]
    pw = password[0:-1] 
    DBconnector.newUser (username, pw)

    response = make_response("it worked!")
    return response
    #return redirect ("/index",conditional=True)

    
@app.route('/api/signin', methods= ['POST'])
def api_signin():
    data = str(request.data) 
    args = data.split("&") 
    username = args[0].split("=")[1]
    password = args[1].split("=")[1]
    pw = password[0:-1] 
    user = DBconnector.checkUser (username, pw)

    if user == None:
        return make_response("failed")

    resp = jsonify(success=True)
    resp.set_cookie("authenticated_user", str(user[2]), 60 * 60 * 24 * 30)
    return resp
       

@app.route('/api/posts',  methods=['GET'])
def api_all_posts():
    if 'authenticated_user' not in request.cookies:
        response = make_response ("Not authenticated", 401)
        return response
    database_posts = DBconnector.get_all_posts()
    posts = []
    for database_post in database_posts:
        posts.append(database_post)
    
    return jsonify(posts)

@app.route('/api/post/<postId>')
def post_content(postId):
    if 'authenticated_user' not in request.cookies:
        return redirect("/sign-in", code=302)
    post_text = DBconnector.get_post_id(postId)
    return jsonify(post_text)


@app.route('/api/post/create', methods=['POST'])
def create_post():
    # If Else statements here instead of client
    if 'authenticated_user' not in request.cookies:
        response = make_response ("Not authenticated", 401)
        return response
    else:
        userId = request.cookies.get('authenticated_user')
        app.logger.debug("request is:", request, "data is", request.form.to_dict())
        arg = str (request.data)
        userStory = arg[2:-1]
        newPost = DBconnector.newPost (userStory, userId)
        app.logger.debug("data is", userStory)
        response = jsonify(newPost=newPost[0])
        return response 

@app.route('/api/post/delete/<postId>', methods=['DELETE'])
def delete_post(postId):
    if 'authenticated_user' not in request.cookies:
        response = make_response ("Not authenticated", 401)
        return response
    else:
        app.logger.debug("request is:", request, "data is", request.form.to_dict(), "post ID is", postId)
        app.logger.debug(postId)
        DBconnector.deletePost(postId)
        return redirect("/profile", code=200)

@app.route('/api/comments/create/<postId>', methods=['POST'])
def create_comment(postId):
    # If Else statements here instead of client
    if 'authenticated_user' not in request.cookies:
        response = make_response ("Not authenticated", 401)
        return response
    else:
        userId = request.cookies.get('authenticated_user')
        app.logger.debug("request is:", request, "data is", request.form.to_dict())
        arg = str (request.data)
        commentInput = arg[2:-1]
        newComment = DBconnector.newComment (commentInput, postId, userId)
        return newComment

@app.route('/api/comments/<postId>')
def get_post_comments(postId):
    if 'authenticated_user' not in request.cookies:
        return redirect("/sign-in", code=302)
    post_comments = DBconnector.get_comments(postId)
    return jsonify(post_comments)


@app.route('/api/profile')
def get_profile():
    if 'authenticated_user' not in request.cookies:
        return redirect("/sign-in", code=302)
    else:
        userId = request.cookies.get('authenticated_user')
        profile_posts = DBconnector.get_profile(userId)
        return jsonify(profile_posts)

if __name__ == "__main__":
    app.run(debug=True)
