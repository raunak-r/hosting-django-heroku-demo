# Setting Up

## Backend-Dependencies
```
Via Anaconda Prompt:
	> virtualenv . (Requires Python 3)
	> .\Scripts\activate

	> Inside Master folder
	> pip install -r requirements.txt
	> Assign Static Folder in settings.py
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
Dashboard > New > Create new app > 

![Heroku New App Page](documentations/images/heroku_start_new_app.png?raw=true "Heroku New App Page")


#### Setting Up Heroku CLI
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
	> 

4. Setup Logs. Logs save lives. Only they can help you see what's wrong.
	> heroku logs -a APPNAME --tail -n 10

5. Create Procfile in your code (Specifically for Django)
	> web: gunicorn PROJECTNAME.wsgi --log-file -
```


#### Connecting Heroku with Git Repo