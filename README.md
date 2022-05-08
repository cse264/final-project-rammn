# Final Project

## Due Last day of Class
## First report due April 11th 2022

Maximillian Machado, Nicole ElChaar, Alexander Carr, Rachael Bucci, Michael DeMasi

### Our Application - https://rammn.herokuapp.com/

#### Name

* Boredle

#### Members & Roles

* Frontend: Rachael Bucci, Alex Carr, Mike Demasi
* Backend: Max Machado
* Database: Nicole ElChaar

#### Functionality

* Must have user accounts and different user roles (like user/Admin, free/paid, etc)
    * Options will be guest, normal user, and admin
    * Guest will be able to access the website and click the button to generate a random response
    * Normal users will be able to choose their region or topic of interest to generate a response
    * Admins will be have access to a dashboard with user and search statistics, such as number of users, searches done by logged in users and guest users

* Must use a database (you choose)
    * PostgreSQL, which will save user information and search statistics over time.

* Must have interactive UI (of any kind)
    * Users will have access to a search tab and a profile tab
    * The search tab finds posts and subreddits curated to the user’s interests
    * Profile tab allows a user to customize their interests or link a reddit account to import interests

* Must use a library or framework not discussed/used in class
    * Backend is built using Python Flask
    * Frontend is built using Vue.js

* Must use an outside REST API in some way (Outside as in external, like the Reddit API, etc)
    * Will select a post to show the user using the Reddit/Twitter API
    * Will obtain user interests from their Reddit/Twitter account if linked

* Must deploy your application in some publicly accessible way (Heroku, Digital Ocean, AWS, etc)
    * Deployed using Heroku

#### Use Case

* Guest
    * Only has access to home page, can click the Boredle button to generate trending reddit posts

* User
    * User can link reddit account to the application using the login button in the top right
    * Can view a profile in order to see recent searches, reddit profile information, and interests

* Admin
    * A user can become and admin by hitting the button in the top right (only for grader testing purposes)
    * Can view the dashboard, which has statistic information about the website like search history and top searches

#### Technical Design

* Backend is developed using Python Flask
    * Routes are handled using flask blueprints
    * Authentication will use OAuth through a user's reddit account
    * Database will be hosted on Heroku and all database transactions will be handled on the backend

* Frontend is developed using VueJS
    * A template from CoreUI was used for many of the design elements
