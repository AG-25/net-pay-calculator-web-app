# UK Net Pay Calculator Web Application
A single page Python (Flask) web application that takes a UK annual salary as input and then calculates annual income tax, national insurance contributions and take-home pay.

## How the Application Works:
1. A user browses to the website and the homepage is rendered with a calculator, which contains a web form for the user to input an annual salary.
1. When the user submits the web form with a valid salary input (positive number with no symbols), the annual tax payments, 
national insurance contributions and take home pay of the employee are calculated on the server side.
1. The homepage is rendered again with the results of the calculation included below the web form.
<br>

|                   Starting calculator:                  |     Calculator after user submission (£55000):   |
| ------------------------------------------------------- | ------------------------------------------------ |
| <img src="/readme_images/starting_calc.PNG">             |<img src="/readme_images/calc_result.PNG">       |


## Using the Application:
The application has been deployed on Heroku and can be accessed here:  
* https://net-pay-calculator-web-app.herokuapp.com/

## Running the Unittests and Application Locally:
1. Clone the repository:  
    >> git clone `https://github.com/AG-25/net-pay-calculator-web-app`
1. Install Python version 3.8 or a later version. The most recent version of Python can be downloaded from: 
     https://www.python.org/downloads/
1. Install the Python modules listed in "requirements.txt" using pip:
   >> pip install requirements.txt
1. Run the unittests by navigating to the project root and entering the following command in a terminal:  
   >> python -m unittest test_app.py
1. To run the application locally, set a "SECRET_KEY"* environment variable to a random string and then enter the following command in a terminal to start a Flask test server:
   >> flask run  
  
*Note that the "SECRET_KEY" environment variable is used by Flask as a cryptographic key.

## Application Files:
* app.py - The main application module, which configures Flask and includes a view function for the homepage.
* tests.py - Unittests for the calculator function in src/calculator.py.
* requirements.txt - A list of Python modules that are needed to run the application.
* Procfile - A file that defines the web server for Heroku to run the application.
* src/calculator.py - Additional Python source code, which includes the calculator function that takes salary as an input and returns net pay.
* src/forms.py - Includes a definition of the flask-wtf form that is used in the application to take user input.
* templates/index.html - HTML template for the webpage.
* static/css/styles.css - Custom css styles for index.html.
* static/css/index.js - Custom javascript for index.html.

## Supporting Libraries:
* Flask (backend): https://flask.palletsprojects.com/en/1.1.x/quickstart/  
* Bootstrap (frontend): https://getbootstrap.com/  

