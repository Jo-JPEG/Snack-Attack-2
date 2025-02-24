# GameBox
A full-stack project by the Code Vipers
![Site logo](static/snake/images/gamebox.png)
## Overview

GameBox is a site that has browser-based games. It can be easily expanded to introduce new games using the Django database.

![Site image](static)

View the live site here: [GameBox](https://snackattack-35d58c59e23c.herokuapp.com/)


## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [GitHub Project board](https://github.com/users/Jo-JPEG/projects/12/)
- **Wireframes:**
  - GameBox games. 
  ![GameBox Display Page](static/snake/images/readme/GameBoxDesign.pngpng)
  - SnackAttack game.
  ![SnackAttack Display Page](static/snake/images/readme/SnackAttackDesign.png)
  - TicTacToe game.
  ![TicTacToe Display Page](static/snake/images/readme/TicTacToeDesign%20.png.png)
- **Design Rationale:**
- **Colour Theme:** 
  - The colour theme was created on [Colour Theme](https://coolors.co/086788-f0c808-fff1d0-8a8a8a-dd1c1a-5be02f-000000-ffffff)
  - Cerulean #086788 for the score boxes 
  - Jonquil #F0C808 used for the arrow keys on the snake screen 
  - Papaya Whip #FFF1D0 for the game board background
  - Battleship Gray #8A8A8A for the headder and footer to allow for logo colour contrast
  - Rojo #DD1C1A for the o's in tic tac toe, snake tounge and snakes food. As well as being intergrated into all. logos.
  - SGBUS Green #5BE02F for X's in tic tac toe and the snake. As well as being intergrated into all logos.
  - Black #000000 for the main background colour.
  - White #FFFFFF for some of the text and footer icons. 
- **Fonts:**
  - The fonts were chosen using Google Fonts and thses are:
  - Rubik Dirt [Link to the font Rubik Dirt](https://fonts.google.com/specimen/Rubik+Dirt) This was used to match the font that was used in the logos.
  - Roboto Flex [Link to the font Robot Flex](https://fonts.google.com/specimen/Roboto+Flex) This was used in all other text. It is simple and easy to read.
- **Design:**
  - The basis of this design started from the game SnackAttack with the idea of a green snake and a red tongue.
  That was the basis for the colour scheem. Other colours were then chosen that allow high colour contrasts. 
  Throughout all three pages there are the same colours implimented to show a uniformed branded design. The 
  layout was to be simple on the landing page showing the game box logo and the two logos for the two games. 
  Then once clicking on a game image you will be taken to the game where instructions are displayed and sign in or register opions are avalible. This is so then you can have your scores stored and recorded for each game and then always be able to view your gaming progress. You can also view other players scores in the view of a leader board. 
  - On screens smaller than a desktop the menu bar will change into a bars icon with a dropdown menu to make sure the logo and menu remain a decent sze to read and be eye catching. 
  - For the snake design due to the game being controlled using arrow keys the design had to involve arrow buttons for tablets and mobiles so the snake can still be controlled. 
  - The footer has the git hub profiles linked of all contributers to this project as well as a copyright. 
- **Accessability:**
  - The three pages and two games have been designed to have:
  - Contasting colour to help those who are visually impared. 
  - Easy readable text, instructions and images to make the site easy to navigate.
  - The use of sound effects to narrate the game.
- **Reasoning For Any Final Changes:**
  - The deployed site does differ from the design in places due to time give for the producrt to be completed. Hopefully with more time given these would be corrected. However the whole site is responsive. 

## Key Features
- **Homepage:** The homepage lists all available games with links and images hosted on Cloudinary. This enables easy future expansion of the games catalogue. 
- **Snack Attack:** Snack Attack is a snake-type game were the user directs a snake character to collect food. The user's score is recorded and high scores are added to the leaderboard.  
- **Inclusivity Notes:** 
  - The site makes use of a high-contrast colour scheme, allowing users with visual imparements to easily read text.

## Deployment
- **Heroku:**
- **High-Level Deployment Steps:** 
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
- **Verification and Validation:**
  - We verified that the deployed version matched the development version in functionality.
  - We checked accessibility of the deployed application via manual testing and Lighthouse performance checks.
- **Security Measures:**
  - Sensitive data, such as the SECRET_KEY should be kept in env.py and not publicly shared.
  - Always set DEBUG to `FALSE` before deploying, for security.

## AI Implementation and Orchestration

### Use Cases and Reflections:
AI was used during the project development to generate code, and debug issues as they arose.

  - **Code Creation:** 
    - Reflection: Strategic use of AI allowed for rapid prototyping, with minor adjustments for alignment with project goals. 
    - Examples: Reverse prompts for alternative code solutions and question-answer prompts for resolving specific challenges.
  - **Debugging:** 
    - Reflection: Key interventions included resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.
  - **Performance and UX Optimization:** 
    - Reflection: Minimal manual adjustments were needed to apply AI-driven improvements, which enhanced application speed and user experience for all users.
  - **Automated Unit Testing: (If undertaken)**
    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

## Testing Summary
- **Manual Testing:**
  - **Devices and Browsers Tested:** [List devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers or keyboard-only navigation.]
  - **Features Tested:** [Summarise features tested manually, e.g., CRUD operations, navigation.]
  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]
- **Automated Testing: (If undertaken)**
  - Tools Used: [Mention any testing frameworks or tools, e.g., Django TestCase.]
  - Features Covered: [Briefly list features covered by automated tests.]
  - Adjustments Made: [Describe any manual corrections to AI-generated test cases, particularly for accessibility.]

## Future Enhancements
- In the future we would make all the features on the sites fully responsive to screen szes. Finish to fit the final designs. 
- Consider enhancements to improve accessibility further, such as voice input capabilities or additional language support.

[imageLink]: static/snake/images/readme/SnackAttackDesign.png