
from flask import Flask, jsonify, send_file, request, make_response
from flask_login import current_user, login_user
from flask_cors import CORS 

app = Flask (__name__)
import DBconnector

CORS(app, resources={r"/api/*": {"origins": "http://34.107.19.83/"}})

@app.route('/')
def main():
    return send_file("static\html\index.html",conditional=True)

@app.route('/sign-up')
def signUp():
    return send_file("static\html\sign-up.html")

@app.route('/sign-in')
def signIn():
    return send_file("static\html\sign-in.html")

#@app.route('/index')
#def index():
    #return send_file("static\html\index.html")

@app.route('/profile')
def profile():
    return send_file("static\html\profile.html")

@app.route('/post')
def post():
    return send_file("static\html\post.html")

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
    resp.set_cookie("authenticated_user", str(user[2]))
    return resp
       

@app.route('/api/main',  methods=['GET'])
def api_all_posts():

    database_posts = DBconnector.get_all_posts()
    for database_post in database_posts:
        post = convertPost(database_post)
        posts.append(post)

    
    return jsonify(posts)


@app.route ('/api/posts', methods=['POST'])
def create_post():
    if 'authenticated_user' not in request.cookies:
        response = make_response ("Not authenticated", 401)
        return response
    else:
        userId = request.cookies.get('authenticated_user')
        # If Else statements here instead of client
        app.logger.debug("request is:", request, "data is", request.form.to_dict())
        arg = str (request.data)
        userStory = arg[2:-1]
        newPost = DBconnector.newPost (userStory, userId)
        app.logger.debug("data is", userStory)
        response = jsonify(newPost=newPost[0])
        return response 




if __name__ == "__main__":
    app.run(debug=True)
