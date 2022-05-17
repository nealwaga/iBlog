# iBlog
iBlog is a web application that allows users to create blogs. The users will be able to submit their  blogs and other users will vote on them and leave comments to give their feedback.


## Author
> Neal Waga


## Installations

The following command installs all the application requirements
>``pip freeze -r requirements.txt``

## Setup
Run 
``https://github.com/nealwaga/iBlog.git``

or download the zip file from github.

After extracting the files, 

1. Navigate to the project folder
>`` cd name_of_folder`` 

2. Creating a virtual environment
>``virtualenv virtual.``

3. Activating the virtual environment
>``source virtual/bin/activate.``

4. Running the application
>``python3 manage.py server``

5. Running tests

 > ``python3 manage.py test.``

## Technologies used
* Python3
* Flask
* Javascript
* HTML5
* CSS3
* Bootstrap4

## User Stories
* As a user, I would like to see the blogs other people have posted.
* As a user, I would like to vote on the blog they liked and give it a downvote or upvote.
* As a user, I would like to be signed in for me to leave a comment
* As a user, I would like to receive a welcoming email once I sign up.
* As a user, I would like to view the blogs I have created in my profile page.
* As a user, I would like to comment on the different blogs and leave feedback.
* As a user, I would like to submit a blog.
* As a user, I would like to view the different categories. 

## BDD(Behaviour Driven Development)
>Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg johndoe``|
| Password  | Account password, ``eg parseword``|

>Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg johndoe``|
| Email  | User email, ``eg morty@testmail.com``|
| Password  | Account password, ``eg parseword``|
| Confirm Password  | Account password, ``eg parseword``|

> Blogs inputs

| Inputs | Description  |
|---|---|
|  Heading | Blog eg; ``Sports``  |
|  Blog text| The actual blog body|
| Comment| A comment on the Blog|


## [License](https://github.com/nealwaga/iBlog/master/LICENSE)
> MIT License &copy; 2022 Neal Waga 

## Collaborate
To collaborate, reach me on [waganeal@gmail.com]()