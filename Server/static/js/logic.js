//This function takes inputs from the user and stores them in the database then allows the user in.
function register()
{
   //Get user input from the HTML form
   var userName = document.getElementById("email").value;
   var password = document.getElementById ("password").value;
   var checkbox = document.getElementById ("tnc");
   // More conditions should be applied as password length and valid email ID (at a later stage)
   if (userName && password != 0)
   {if (!checkbox.checked) {
      event.preventDefault(); 
      alert("Please agree to the terms and conditions before signing up");
      } else 
            {
   //Put it in the Database
      let xhr = new XMLHttpRequest();
      xhr.responseType = "json";
      xhr.open("POST", "/api/sign-up");
      // define what to do when the response comes back
      xhr.onload = function () {
      // redirect user to the main page
      window.location.href = "/"
         console.log ("response! " + xhr.response);
      };
      console.log ("It's getting sent!");
      //send the request, and when it comes back, run the code above.
      xhr.send("userName="+userName+"&password="+password);
      console.log ("userName="+userName+"&password="+password);}
      // Allow user in!  

   }
}

//This function takes inputs from user and checks them against the DB information, if there is a match the user is allowed in, if not, the user can try again.
function authenticate() 
{
   // Get user input from the HTML form
   var userName = document.getElementById("email").value;
   var password = document.getElementById ("password").value;
   // Take user input to the server
   let xhr = new XMLHttpRequest();
   xhr.open("POST", "/api/sign-in");
   xhr.onload = function () {
      var response = JSON.parse(xhr.response)
      if (response.success){
         window.location.href = "/"
      }
      else {
         alert("Wrong email or password, please try again!")
        }
   }
      // send the request, and when it comes back, run the code above.
      xhr.send("userName="+userName+"&password="+password);

} 

function all_posts() {
   for (let i=0; i< allposts.length; i++) {

   }
}

//This function loads all the content of the mainpage when a user visits the website
function loadMain () {
 // get all posts from the database
   let xhr = new XMLHttpRequest();
   xhr.responseType = "json";
   xhr.open("GET", "/api/posts");
   // define what to do when the response comes back
   xhr.onerror = function (error) {
      console.log("ERROR! ", error)
   }
   xhr.onload = function () {
      // Response will contain the data to render
      if (xhr.response === null) return;
      for (const story of xhr.response.reverse()) {
         var [postId, userId, storyText] = story;
         renderNewPost({ input: storyText, postId });
      }
   }
   xhr.send();
}

//This function loads the content of one story
function loadStory() {
   // get post from database with postId
   let url = window.location.href.split("/")
   let post_id = url[url.length - 1]
   console.log(post_id)
   let xhr = new XMLHttpRequest();
   xhr.responseType = "json";
   xhr.open("GET", "/api/post/" + post_id);
   // define what to do when the response comes back
   xhr.onerror = function (error) {
      console.log("ERROR! ", error)
   }
   xhr.onload = function () {
      // Response will contain the data to render
      if (xhr.response === null) return;
      console.log("THIS IS RESPONSE", xhr.response)

      let postText = xhr.response[0][2]
      document.getElementById('story-content').innerHTML = postText
   }
   xhr.send();
   loadComments()
}

//This function loads the comments of a post
function loadComments() {
   // get post from database with postId
   let url = window.location.href.split("/")
   let post_id = url[url.length - 1]
   console.log(post_id)
   let xhr = new XMLHttpRequest();
   xhr.responseType = "json";
   xhr.open("GET", "/api/comments/" + post_id);
   // define what to do when the response comes back
   xhr.onerror = function (error) {
      console.log("ERROR! ", error)
   }
   xhr.onload = function () {

      document.getElementById('post-comments').innerHTML = ''

      // Response will contain the data to render
      if (xhr.response === null) return;
      let comments = xhr.response

      for (let i = 0; i < comments.length; i++) {
         var comment = document.createElement("div");
         comment.classList.add("comment-box");
         comment.innerHTML = comments[i][3];
         document.getElementById('post-comments').appendChild(comment)
      }

   }
   xhr.send();
}

//This function loads the posts of a user
function loadProfile() {
   let xhr = new XMLHttpRequest();
   xhr.responseType = "json";
   xhr.open("GET", "/api/profile");
   // define what to do when the response comes back
   xhr.onerror = function (error) {
      console.log("ERROR! ", error)
   }
   xhr.onload = function () {
      // Response will contain the data to render
      if (xhr.response === null) return;
      console.log("THIS IS PROFILE RESPONSE", xhr.response)

      for (const story of xhr.response) {
         var [postId, userId, storyText] = story;
         renderNewPost({ input: storyText, postId });
      }
   }
   xhr.send();
}


//Get input from User
function newPost() {
   // get data from UI
   var payLoad = document.getElementById("story-content").value;
   if (payLoad != 0) {
      let xhr = new XMLHttpRequest();
      xhr.responseType = "json";
      xhr.open("POST", "/api/post/create");
      // define what to do when the response comes back
      xhr.onerror = function (error) {
         console.log("ERROR! ", error)
      }
      xhr.onload = function () {
         // Response will contain the data to render
         if (xhr.response === null) return;
         var [postId, userId, input] = xhr.response.newPost;
         renderNewPost({ input, postId });
         console.log("Saved!")
      }
      xhr.send(payLoad);
      console.log ("story="+payLoad);
   }
}

function deletePost() {
   let url = window.location.href.split("/")
   let post_id = url[url.length - 1]
   let xhr = new XMLHttpRequest();
   xhr.responseType = "json";
   xhr.open("DELETE", "/api/post/delete/" + post_id);
   // define what to do when the response comes back
   xhr.onerror = function (error) {
      console.log("ERROR! ", error)
   }
   xhr.onload = function () {
      // Response will contain the data to render
      if (xhr.response === null) return;
      loadComments()
   }
   xhr.send();
}


//copy change new
function newComment() {
   var payLoad = document.getElementById("comment-content").value;
   let url = window.location.href.split("/")
   let post_id = url[url.length - 1]
   if (payLoad != 0) {
      let xhr = new XMLHttpRequest();
      xhr.responseType = "json";
      xhr.open("POST", "/api/comments/create/" + post_id);
      // define what to do when the response comes back
      xhr.onerror = function (error) {
         console.log("ERROR! ", error)
      }
      xhr.onload = function () {
         // Response will contain the data to render
         if (xhr.response === null) return;
         loadComments()
      }
      xhr.send(payLoad);
      console.log("story=" + payLoad);
   }
}

//This function should alternate between showing and hiding the moderator pop-up upon click ((FINALIZE))
function displayHide () {
   var x = document.getElementById ("invisible");
   if (x.style.display === "none") {
      x.style.display = "block";
   } else {
      x.style.display = "none";
   }
}

//This function creates the contents of the div that holds the new post to render
function createNewPost (postId, input) {
   var post = document.createElement("div");
   post.classList.add ("post");
   var story = document.createElement("div");
   story.classList.add ("story");
   story.textContent = input;
   var like = document.createElement("div");
   like.classList.add ("like");
   like.textContent = "like";
   var comment = document.createElement("a");
   comment.classList.add ("comment");
   comment.textContent = "comment";
   comment.href = `/post/${postId}`;
   post.appendChild(story);
   post.appendChild(like);
   post.appendChild(comment);
   return post;
}


//This function renders a new post on the HTML when the user submits a story
function renderNewPost(payload){
   var { postId, input } = payload;
   var newPost = createNewPost(postId, input);
   document.getElementById("posts").prepend(newPost);
}

// This function takes userId and returns all posts made by the same user to the profile page.
function userPosts () 
{
   if(userId == 1) return allPosts (userId == 1);
   if(userId == 2) return allPosts (userId == 2);

   console.log("user id " + userId + " not found" );
   return null;
}


// This function takes postId and returns it with its properties to the post page.
function postPage (postId) 
{
   for (let index = 0; index < allPosts.length; index++) 
   {
      if(allPosts[index].postId == postId)  
      {
          return allPosts[index]
      }
   }
}
