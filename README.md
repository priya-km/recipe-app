# Recipe Rack

<p>Recipe Rack is a project built using the Python-based Django framework. It has been deployed on Heroku. RR allows its users to view a recipe wiki, upload their own recipes, and search recipes.<br>
<br>
<h2>Video Demo</h2>


https://github.com/priya-km/recipe-app/assets/118628757/a02a3c36-f3f5-44fc-99f7-67afd713fa99

## [Live Demo](https://github.com/priya-km?tab=repositories "RR Live Demo")
### Live Demo Login: (case sensitive)
Username: demo <br>
Password: DemoUser
<br>
<p>*Please note that when trying out the demo hosted on Heroku, you may not see the images of recipes. This is due to Heroku's ephemeral filesystem, which resets every time the dyno restarts. As a result, uploaded images are not persisted across dyno restarts. I hope to implement an external storage solution in the near future.</p>
<br>
<p>Demo users are not authorized to access the Django admin panel and are for user demonstration purposes only.</p>

## Local Demo Installation
#### Requirements:
- Python 3.11.6
<br>
Note: Run these commands in the terminal from the desired root directory

1. Clone the repo
   ```sh
   git clone https://github.com/priya-km/recipe-app.git
   ```
2. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Migrate the database
   ```sh
   python manage.py migrate
   ```
3. Run the local server
   ```sh
   python manage.py runserver
   ```
<h2>Key Features</h2>
● Allow for user authentication, login, and logout.<br>
● Let users search for recipes according to ingredients.<br>
● Automatically rate each recipe by difficulty level.<br>
● Receive user input and handle errors appropriately.<br>
● Display more details on each recipe if the user asks for that.<br>
● Add user recipes to an SQLite database.<br>
● Include a Django Admin dashboard for working with database entries.<br>
● Show statistics and visualizations based on trends and data analysis<br>
<br>

## Tech-Stack:
● Python<br>
● Django<br>
● Heroku<br>
● HTML/CSS<br>


<h2>Links</h2>

[Portfolio](https://priya-km.github.io/portfolio "Portfolio")
<br>
[My Repositories](https://github.com/priya-km?tab=repositories "My Repositories")<br>
[LinkedIn](https://www.linkedin.com/in/priyamaharban/ "LinkedIn")<br>
[Email Me](mailto:priyakmaharban@gmail.com?subject=Hi% "Hi!")
