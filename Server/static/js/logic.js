//This function takes inputs from the user and stores them in the database then allows the user in.
function register(){
   //Get user input from the HTML form
   var userName = document.getElementById("email").value;
   var password = document.getElementById ("password").value;
   // More conditions should be applied as password length and valid email ID (at a later stage)
   if (userName && password != 0)
   {
   //Put it in the Database
      let xhr = new XMLHttpRequest();
      xhr.responseType = "json";
      xhr.open("POST", "http://127.0.0.1:5000/api/signup");
      // define what to do when the response comes back
      xhr.onload = function () {
      // redirect user to the main page
      window.location.href = "/"
         console.log ("response! " + xhr.response)
      }
      console.log ("It's getting sent!")
      //send the request, and when it comes back, run the code above.
      xhr.send("userName="+userName+"&password="+password);
      console.log ("userName="+userName+"&password="+password);
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
   xhr.open("POST", "http://127.0.0.1:5000/api/signin");
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

  /* This function isn't used anymore for security of user information
  for (let i=0; i< allUsers.length; i++)
   {
   var outcome = " ";
   
   //Find a safer way than sending all info over the inetersnet! 
      if (userName==allUsers[i].userName && password==allUsers[i].password)
      { 
         document.getElementById ("sign-in");
         console.log (userName+ "is here!");
         window.user = allUsers[i];
         //Allow user in! (only if the feilds are filled correctly)
         outcome += window.location.href = "\index.html"
         break
      } else
      { 
         outcome += alert("Wrong password, please try again");
         console.log ("wrong password");
         window.location.reload ();
         break
      }
   }
   return outcome;
*/
} 

function all_posts() {
   for (let i=0; i< allposts.length; i++) {

   }
}

//This function loads all the content of the mainpage when a user visits the website
function loadMain () {
 // get all posts from the database
   var all_posts = document.getRootNode("story-content").value;
   let xhr = new XMLHttpRequest();
   xhr.responseType = "json";
   xhr.open("POST", "http://127.0.0.1:5000/api/posts");
   // define what to do when the response comes back
   xhr.onerror = function (error) {
      console.log("ERROR! ", error)
   }
   xhr.onload = function () {
      // Response will contain the data to render
      if (xhr.response === null) return;
      var [input, postId, userId] = xhr.response.get_all_posts;
      renderNewPost({ input, postId });
      console.log("Saved!")
   }
   xhr.send(all_posts);
   console.log ("story="+all_posts);
}

//Get input from User
function newPost() {
   // get data from UI
   var payLoad = document.getElementById("story-content").value;
   if (payLoad != 0) {
      let xhr = new XMLHttpRequest();
      xhr.responseType = "json";
      xhr.open("POST", "http://127.0.0.1:5000/api/posts");
      // define what to do when the response comes back
      xhr.onerror = function (error) {
         console.log("ERROR! ", error)
      }
      xhr.onload = function () {
         // Response will contain the data to render
         if (xhr.response === null) return;
         var [input, postId, userId] = xhr.response.newPost;
         renderNewPost({ input, postId });
         console.log("Saved!")
      }
      xhr.send(payLoad);
      console.log ("story="+payLoad);
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
   var share = document.createElement("div");
   share.classList.add ("share");
   share.textContent = "share";
   var like = document.createElement("div");
   like.classList.add ("like");
   like.textContent = "like";
   var comment = document.createElement("a");
   comment.classList.add ("comment");
   comment.textContent = "comment";
   comment.href = "/post";
   post.appendChild(story);
   post.appendChild(share);
   post.appendChild(like);
   post.appendChild(comment);
   return post;
}

//This function renders a new post on the HTML when the user submits a story
function renderNewPost(payload){
   var { postId, input } = payload;
   var newPost = createNewPost(postId, input);
   document.getElementById("posts").prepend(newPost); //why is it appending instead?
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
