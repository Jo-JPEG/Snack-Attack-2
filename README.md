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
  (static/snake/images/readme/Game Box Page Design.png)
  - SnackAttack game.
  (static/snake/images/readme/Snack Attack Page Design.png)
  -TicTacToe game.
  (static/snake/images/readme/TicTacToe Page Design.png)

  [Attach or link to accessible wireframes used in the design process, ensuring high colour contrast and alt text for visual elements.]
  - The basis of this design started from the game SnackAttack with the idea of a green snake and a red tongue.
  That was the basis for the colour scheem. Other colours were then chosen that allow high colour contrasts. 
  Throughout all three pages there are the same colours implimented to show a uniformed branded design. The 
  layout was to be simple on the landing page showing the game box logo and the two logos for the two games. 
  Then once clicking on a game image you will be taken to the game where instructions are displayed and sign in or register opions are avalible. This is so then you can have your scores stored and recorded for each game and then always be able to view your gaming progress. You can also view other players scores in the view of a leader board. 
   [Explain the rationale behind the layout and design choices, focusing on usability and accessibility for all users, including those using assistive technologies.]
- **Design Rationale:**
  - [Explain key design decisions, such as layout, colour scheme, typography, and how accessibility guidelines (e.g., WCAG) were integrated.]
  - [Highlight any considerations made for users with disabilities, such as screen reader support.]
- **Reasoning For Any Final Changes:**
  - [Summarise significant changes made to the design during development and the reasons behind them.]
  - [Reflect on how these changes enhance inclusivity and accessibility.]

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
- [List potential improvements or additional features for future development.]
- Consider enhancements to improve accessibility further, such as voice input capabilities or additional language support.