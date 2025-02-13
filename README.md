# Snack-Attack
A full-stack projects by the Code Vipers
![Site logo](static/)
## Overview

Snack Attack is a fun and simple game based on the classic "Snake" game.


![Site image](static)

View the live site here: [Snack Attack](https://snackattack-35d58c59e23c.herokuapp.com/)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Agile](#agile)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [AI Implementation and Orchestration](#ai-implementation-and-orchestration)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### User Stories

- Full User Stories in GitHub Projects:
 [GitHub Project board](https://github.com/users/Jo-JPEG/projects/12/)

#### Must-have User Stories:


#### Should-have User stories:
 


#### Could-have User stories

## Agile

For this project we used Agile methodology to prioritize project requirements, tasks, and features.

User stories were separated into 4 catagories:
- Must have: These are the non-negotiable requirements that are essential for the project to be considered successful. Without these features, the project would fail or be deemed incomplete.
- Should have: These are important requirements that are not critical for the project's success but would add significant value. While the project could still function without them, their inclusion would enhance the overall experience.
- Could have: These are desirable requirements that would be nice to have but are not essential. They can be included if time and resources permit, but they are not a priority.
- Won't have (this time): These are requirements that will not be included in the current project scope. They may be considered for future iterations or phases but are not necessary for the current project.

## Design

### Design Rationale:


### Colour Scheme



### Typography

[Google Fonts](https://fonts.google.com/).

The main font, 



### Imagery



### Wireframes

 
## Features

### Main features


#### Profile

Users can see a profile page where they can edit their password or delete their account.

#### Logout

Users can log out of their account easily from the navbar.

### Future Implementations


### Accessibility

Accessibility was a priority at all stages of developing this project.

## Technologies Used

### Languages Used

- HTML was used to create the frontend pages.
- CSS was used to style the frontend site.
- Python and Django were used to build the backend framework.

### Frameworks, Libraries & Programs Used

- GitHub was used to host the repository and for version control.
- Heroku was used as a platform to host the deployed site.

- Bootstrap
- [Google Fonts](https://fonts.google.com/) was used for fonts.
- [Font Awesome](https://fontawesome.com/) was used for icons.


## AI Implementation and Orchestration

### Use Cases and Reflections:

#### Code Creation:


#### Debugging:


#### Performance and UX Optimization:

- AI had an impact on performance..

### Overall Impact:

- We found that...

## Deployment & Local Development

### Deployment

#### Platform:
- The website was deployed to Heroku and can be found [here](https://snackattack-35d58c59e23c.herokuapp.com/).
### Heroku
* Heroku is a cloud platform that lets developers create, deploy, monitor and manage apps.
- You will need a Heroku account to be able to deploy a website to Heroku.

 **High-Level Deployment Steps:** 
1. From the Heroku dashboard, click 'New' > 'Create new app'
2. Choose a unique name, choose the closest region, and press 'Create app'
3. Navigate to 'Settings' and then click 'Reveal Config Vars'
4. Add a key of 'DISABLE_COLLECTSTATIC' with a value of '1'.
5. Add a key of 'DATABASE_URL' - this value will be the URL for your database.
6. Add a key of 'SECRET_KEY' - the value should be a random secret key.
7. In your terminal, enter the following commands to install project requirements:
- `pip3 install gunicorn~=20.1`
- `pip3 install -r requirements.txt`
- `pip3 freeze --local > requirements.txt`
8. Create a file named `env.py` in the root directory, containing the following:
    - import os
    - os.environ["DATABASE_URL"]='Your database URL'
    - os.environ["SECRET_KEY"]="Your secret key"
9. Create a file at the root directory called Procfile. In this file enter: "web: gunicorn my_project.wsgi" (without the quotes)
10. In settings.py, ensure DEBUG is set to `False`.
11. Add ",'.herokuapp.com' " (without the double quotes) to the ALLOWED_HOSTS list in settings.py
12. Add, commit and push your code.
13. On Heroku, click on the 'Deploy' tab.
14. Connect your project to GitHub.
15. Scroll to 'Manual deploy' and click on, 'Deploy Branch'.


#### Verification and Validation:
- Verify the deployed version matches the development version in functionality.
- Ensure accessibility of the deployed application via manual testing and Lighthouse performance checks.
#### Security Measures:
- Sensitive data, such as the SECRET_KEY should be kept in env.py and not publicly shared.
- Always set DEBUG to `FALSE` before deploying, for security.

### Local Development

#### How to Fork

A fork is a new repository that shares code and visibility settings with the original “upstream” repository.
- To fork a GitHub repository:
1. Login to GitHub and navigate to the repository you want to fork.
2. Click the "Fork" button (found above the Settings button).
3. This creates a copy of the original repository in your GitHub account.

#### How to Clone

Cloning this repository will create a local copy on your computer.

- Access the repository: Go to the GitHub repository you want to clone on the GitHub website. 
- Copy the URL: Click on the "Code" button and copy the HTTPS URL provided. 
- Open your terminal: Open a terminal window on your computer. 
- Run the clone command: `git clone <repository-url>` 
- You can also clone a repository using the GitHub Desktop application by selecting the repository and clicking "Clone". 

*Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Run the server: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C`
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`

## Testing


### Manual Testing:

#### Devices and Browsers Tested: 
- The site was tested on Chrome,
- Various devices were used during testing... 
- Keyboard navigation was tested to ensure site can be navigated fully without mouse inputs.
#### Features Tested:
- User account creation, login, password edit, logout and account deletion.

#### Results:
- All critical features work as expected???


## Credits

### Code Used


### Content


###  Media


###  Acknowledgments

- We would like to thank...