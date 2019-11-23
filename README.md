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

#### Heroku Account Creation
```
https://www.heroku.com/

Create an account for free. No need to add credit cards or anything.
```

#### Create a new App corresponding to the website.
```
Dashboard > New > Create new app > 
```
![Heroku New App Page](relative/documentations/images/heroku_start_new_app.png?raw=true "Heroku New App Page")

