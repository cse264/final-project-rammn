# Frontend Manual

## Requirements:

- npm
- ...

## Run server:

Depending on development, there are two deploy options: local and heroku. **When in development**, use the "Local Deploy" to test features. **When in production/Heroku deployment**, use the "Heroku Deploy" to push stable/running version of the frontend to the backend.

### Local Deploy:
1. Type `npm run serve`.
2. Click [here](http://localhost:8080/).

(Note: localhost is available only on the computer running the Vue.js instance. If you want to test the app on other computers connected to the same network then use the provided "Network" link provided to you when the command in step 1 is executed. This link may not work depending on network settings)

Once your app is running, feel free to develop in real time. The reactive nature of Vue.js will update code as you save the files, so there is no need to redeploy after each save.

### Heroku Deploy:
1. Ensure code is stable using the "Local Deploy" version.
2. Stage, commit, and push code to your current remote working branch.
3. Checkout/move to the master/main branch.
4. Merge code from the previous branch (the one used for the most-up-to-date development) into the master/main branch.
5. Type `npm run build`.
6. Move to the "backend" folder and execute the "deploy_heroku" script.
7. (Option 1) If the changes seemed to work well on the Heroku, **do not** forget to push the new web/frontend code to the master branch. (finished)
7. (Option 2) If the changes did not seem to work on the Heroku, **revert the changes to master** by using the git reset functionality. The consequence of this will be that the master/main branch will continue to have the "bad" code, but only in the "web" folder. The "backend" folder will continue to have the stable frontend code. For correctness, you should roll back the master branch by one commit. However, this last step is not as important as just keeping the backend clean.


(Note: the final step of the list above is critical to avoid merge and uncommited file problems)

The process above can be described as the following: first, the code is validated as being ready for remote deployment; second, the code is saved to the remote branch respective to the current developer (I assume you are working in a branch independent of the master/main remote branch); third, the code in the remote working branch is ready to be added to the most stable version of the code-base (master/main) and so we add it; forth, we run a build script that copies files from the *compiled* Vue.js app into the backend's web resource folders (this moves files around the project base from "web" into "backend"); fifth, we move to the "backend" folder to prepare deployment of the Python Flask application and run a script that handles the configuration and deployment of the app; sixth, if the Heroku deployed version of the code-base is satisfactory then commit the new code in the backend (the copied files after building the Vue.js frontend in step 5) to the master/main branch. Alternatively, if the deployed version of the Vue.js app is not to satisfaction, then preform a git reset in the master/main branch. Again, if the last step is not finished, then you will run into difficultly switching branches or commiting code to the main/master branch in the future.

## Installation Instructions:

1. 

## Run tests:

1. 

## Environment Configuration:

(Note to developers: the backend should have a config file that both web and backend will have access to. However, this has not been figured out yet.)

## TODO:

- 