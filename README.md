# We@NITC
The website is up and running. [Check out the website here](http://nandana1anand1tvm.pythonanywhere.com/)

![image](https://github.com/user-attachments/assets/e1586807-d166-4541-bc2b-41b42f3a5526)

## Details
The website was created using html, css(bootstrap framework) and django. 

## Home Page
The posts and calender can be viewed. The posts are also paginated.

## USER Interface
Anyone can view the website and see all posts. However, users need to have accounts and login to write, update and delete posts. They can also like other's posts. Ever user has a profile page.

### 1. Register user
- For registering, user needs to fill a form (implemented using django modelforms).
  
  ![image](https://github.com/user-attachments/assets/b9bb8201-185c-4ad7-8af3-d691ed9967e2)
  
  The email id should be of NITC mail id to ensure that only students of the college can access the website
  
### 2. Login
- After setting the password, the user will be redirected to login page.
  
  ![image](https://github.com/user-attachments/assets/6e0171ac-d1cf-437b-8586-a32c502fb9e5)
  
- Already existing users can simply login directly.
  
### 3. Password Reset
- There is also an option for forgot password where the users can type in the registered email id and reset the password through the mails. If you do not receive any mail, that would imply that the mail id entered is wrong.

## BLOG POSTS
-  Any user can view everyone's posts:
  ![image](https://github.com/user-attachments/assets/e1586807-d166-4541-bc2b-41b42f3a5526)

-  But only registered users can create posts:
  ![image](https://github.com/user-attachments/assets/ad68ca67-c85e-4727-bf3a-6a4f7cc52658)

-  Clicking on a post's title will open up the posts detail view with option to even like a post:
  ![image](https://github.com/user-attachments/assets/32dd7851-741d-40c7-864c-6ce345d1a441)

- Logged in users can also like the posts. 
  ![image](https://github.com/user-attachments/assets/e9901a74-27df-487f-90b1-882ed1c859d2)

- A user who is not logged in cannot like and will be asked to login to do so.
- Also, a user cannot like their own posts.
- Opening one's own posts will open up options to update/ delete the post and the user to choose to do either:
  ![image](https://github.com/user-attachments/assets/1200afe0-b019-4995-a4d2-6de21fa213a9)
  
## USER Profiles
- In the home page, if the user clicks on the username of the author of the posts OR the profile picture, then the profile of the author can be viewed.
  ![image](https://github.com/user-attachments/assets/475cc50e-21e8-4eec-ab8f-a6d67ea564aa)

- While viewing one'e own profile, there will also be an option to edit the profile. The username, about fields and profile picture are set to default if the user did not provide one.
  ![image](https://github.com/user-attachments/assets/7089a0a1-219c-42e1-905b-a9db164d6983)

- While updating profile pictures, the uploaded image can be previewed directly:
  ![image](https://github.com/user-attachments/assets/824b5ce0-5c2f-4c56-abdf-e69acba089ef)

## Calender
- The advanced calender feature helps in giving a quick overview about the posts on the website. 
  ![image](https://github.com/user-attachments/assets/c5477151-b152-4582-9733-4bdd79539b0f)

- Clicking on any date will show the posts on that date
  ![image](https://github.com/user-attachments/assets/f3f43934-582e-49ad-94ec-6e94fa73a909)


# More interesting features and updations coming soon.....
