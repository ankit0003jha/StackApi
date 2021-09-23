# StackApi
 Using stackoverflow api we have to scrap question and represent it  in a proper format using all search fields and parameters.


## How to run this application on your system.

1) First clone this project.
2) Make a virtual enviroment on your system.
3) Take requirements.txt file which i provided in the uppermost dir in this respository.
4) Then run: pip install -r requirements.txt in your shell.
5) Go to terminal and run python manage.py make migrations and python manage.py migrate.
6) Go to manage.py file dir and run python manage.py runserver.
7) Want to access django admin panel createsuper and login into it.

## What this application do?

1) We have used stackoverflow api to scrab questions and other owner information.
2) We have made a search area for each field and parameters present in the api.
3) We have used django pagination to list the items. (we have set some default value you can also change it while searching the query)
4) We have used Redis-cache system for Page/Data. (Application should only call StackOverflowAPI if we didn't pull data already for same query param)
5) We have used django throttling for Search limit per min(5) and per day(100) for each session.
6) This is the simple explaination about this application. Clone it and run it on your system and enjoy the application.

## You have to download Redis server for windows to run redis-caching system.
