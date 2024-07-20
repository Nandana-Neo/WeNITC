# We@NITC
The website is up and running. [Check out the website here](http://nandana1anand1tvm.pythonanywhere.com/)
![image](https://github.com/user-attachments/assets/84b9b6a8-17d4-4f98-bd28-9bab5fab4f31)


## Details
The website was created using html, css(bootstrap framework) and django. 

## Home Page
The posts and calender can be viewed. The posts are also paginated.

## USER Interface
Anyone can view the website and see all posts. However, users need to have accounts and login to write, update and delete posts. They can also like other's posts. Ever user has a profile page.

### 1. Register user
- For registering, user needs to fill a form (implemented using django modelforms).
  
  ![image](https://github.com/user-attachments/assets/0ee97826-8507-4b75-853a-2a08e4839f66)

  
  The email id should be of NITC mail id to ensure that only students of the college can access the website
  
### 2. Login
- After setting the password, the user will be redirected to login page.
  
  ![image](https://github.com/user-attachments/assets/34ec261c-6ca9-4361-a228-979256d4e53a)

  
- Already existing users can simply login directly.
  
### 3. Password Reset
- There is also an option for forgot password where the users can type in the registered email id and reset the password through the mails. If you do not receive any mail, that would imply that the mail id entered is wrong.

## BLOG POSTS
-  Any user can view everyone's posts:
  ![image](https://github.com/user-attachments/assets/e012e665-fef3-4977-a4e7-35c3632a54e7)

-  But only registered users can create posts:
  ![image](https://github.com/user-attachments/assets/1f792bdb-3679-4698-862c-e1792833fd37)

-  Clicking on a post's title will open up the posts detail view with option to even like a post:
  ![image](https://github.com/user-attachments/assets/acb419a0-0f0c-4c61-bb8b-627097638a4a)

- Logged in users can also like the posts. 
  ![image](https://github.com/user-attachments/assets/9809c440-0000-4bf1-a639-38a4c0bb420e)

- A user who is not logged in cannot like and will be asked to login to do so.
- Also, a user cannot like their own posts.
- Opening one's own posts will open up options to update/ delete the post and the user can choose to do either:
  ![image](https://github.com/user-attachments/assets/689bb3d5-b588-423e-916c-d816cf7652a6)

  
## USER Profiles
- In the home page, if the user clicks on the username of the author of the posts OR the profile picture, then the profile of the author can be viewed.
  ![image](https://github.com/user-attachments/assets/6fa0c765-6ce3-41c0-b547-abbb905f2e6b)

- While viewing one'e own profile, there will also be an option to edit the profile. The username, about fields and profile picture are set to default if the user did not provide one.
  ![image](https://github.com/user-attachments/assets/53d016c3-0952-4b3e-a9a9-4d470b7f0f27)

- While updating profile pictures, the uploaded image can be previewed directly:
  ![image](https://github.com/user-attachments/assets/55b2b096-fd0a-4a30-b504-96aad65efb01)


## Calender
- The advanced calender feature helps in giving a quick overview about the posts on the website. 
  ![image](https://github.com/user-attachments/assets/8b5c8d8c-c480-4856-956c-c5f2773d1135)

- Clicking on any date will show the posts on that date
  ![image](https://github.com/user-attachments/assets/534ba493-f41d-4814-9d00-b10fe7fa4f32)



# More interesting features and updations coming soon.....
