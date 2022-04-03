#livefeedapp

##Table of conten
* [About the project](#about-the-project)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)

##About the project

  This is a live feed chat made with django the .
It include login and authentification and moderation.

##Technologies

* Python3
  * Django4
  * HTML
  * CSS
  * JAVA SCRIPT

##Features

  * Post Message
  * Read Message
  * Login And Registration
  * Report A Message For User
  * Moderator Can See Reported Message
  * Moderator Can Hidde Reported Message
  * Moderator Can Unhidde A message

##Setup

  This app is made with raw django to run it localy you just need to have django at least version 4 , before you run the project create a superuser :

  ```shell
    $cd livefeedapp/
    $source bin/activate
    $cd src/livefeedapp
    $python3 manage.py createsuperuser
    $python3 manage.py makemigrations
    $python3 manage.py runserver
  ```
