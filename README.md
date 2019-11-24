# Setting Up

## Backend-Dependencies
```
Via Anaconda Prompt:
	> virtualenv . (Requires Python 3)
	> .\Scripts\activate

	> Inside Master folder -> cd ./master/
	> pip install -r requirements.txt
	
	> Assign Static Folder in settings.py
		STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

	> python backend\manage.py runserver

```

## Frontend-Dependencies
```
1. THE PROJECT ECOSYSTEM (npm, bower)
	<!-- Install Node Js -->
	> https://nodejs.org/en/download/

	<!-- Check version using  -->
	> node -v
	v10.16.3

2. JS Framework (Angular)
	> npm install -g @angular/cli
	> > ng --version (TO VERIFY)

3. SETUP DEPENDENCY MANAGERS FOR PROJECT
	> cd frontend
	> npm install (from package.json)

	<!-- INFO  -->
	* npm install will install all dependencies mention in package.json

4. RUNNING THE FRONTEND
	> Open a new terminal
	> cd speech-recognizer\Master\frontend>
	> npm start

<!-- Other Commands -->
ng generate component dashboard
```	

## Setting it up for Cloud Deployment

#### Git Repository Setup
To host your code, keep track of changes. Be the VCS
Setup a git repository. Commit your code there. Make sure that everything is working on your local. To read about setting up a new repository see link.

https://help.github.com/en/github/getting-started-with-github/create-a-repo


#### Heroku Account Creation
To create, maintain and deploy your git repo to a server.
Create an account for free. No need to add credit cards or anything.
https://www.heroku.com/


#### Create a new App corresponding to the website.
Dashboard > New > Create new app

![Heroku New App Page](documentations/images/heroku_start_new_app.png?raw=true "Heroku New App Page")


#### Setting Up Heroku CLI and a few support files
```
1. https://devcenter.heroku.com/articles/heroku-cli#verifying-your-installation

	Download it.
	Verify it.
		> heroku --version


2. Login
	> heroku login -i


3. Install Some Basic Required Plugins
	> heroku plugins:install heroku-builds
	> heroku plugins:install heroku-repo


4.a. Setup Logs on Heroku. Logs save lives. Only they can help you see what's going wrong.
	> heroku logs -a APPNAME --tail -n 10

4.b. Setup Logs on your backend side.
	> See LOGGING in settings.py
	
	> Add the following in your views.py wherever necessary.
		import logging
		logger = logging.getLogger(__name__)
		logger.info('Inside Home Page')


5. Create Procfile in your code (to start containers)

	> web: gunicorn PROJECTNAME.wsgi --log-file -
	(If the manage.py and project is in the same folders)
	
	OR

	> web: sh -c 'cd ./backend/ && exec gunicorn --preload tryHosting.wsgi --log-file -'
	Procfile should be at repo level.
	Manage.py can be inside a folder named 'backend'
	frontend files in a folder named 'frontend'


6. Add 'app_name.herokuapp.com' in Allowed_Hosts in settings.py. ex. below
	ALLOWED_HOSTS = [
	    'try-hosting.herokuapp.com',
	    'localhost',
	]

```


#### Connecting Heroku with Git Repo
Shown below is the dashboard once you're in your app.
![Dashboard](documentations/images/dashboard.png?raw=true "Dashboard")

Select Deploy Tab.
No need to choose any pipelines for now.
1. Under Deployment Method. Connect Github
2. Choose repository to be connected.
3. Enable Automatic Deploys

4. If this is the first time, under the 'Manual Deploy' Tab, select Deploy Branch. It will deploy on its own the next time commits are going to be made.

You can see the build logs either in terminal or under the Activity Tab.


#### Deployment Successfull
If everything has gone right, then you should see the below in your logs.

![Successfull](documentations/images/build_success.png?raw=true "Successfull")