#The bellow code samples contain a lot of different code found in Chapter 4. 
# While the majority of the code is written in python, there are other YAML, JSON and Java files that are included 
# to showcase the operation of these basic tests and data in entirety.


#The first code is a JSON data structure written in Python syntax. 
# It represents a list of dictionaries, where each dictionary contains information about a user's login attempt. 
# Each dictionary has three key-value pairs: username, password, and expectedOutcome.

#username: This key holds the username of the user attempting to log in. 
# For example, the first dictionary specifies "user1" as the username, while the second specifies "user2".
#password: This key contains the password provided by the user during the login attempt. 
# In the first dictionary, the password is "pass123", and in the second, it is "wrongpass".
#expectedOutcome: This key indicates the anticipated result of the login attempt. 
# It is either "success" or "failure". For instance, the first dictionary expects the login to succeed, while the second expects it to fail.

#This structure is likely used for testing or simulating login functionality in an application. 
# By providing a set of predefined inputs (username and password) and their corresponding expected outcomes, 
# developers can validate whether the login system behaves as intended. 
# For example, they can check if the system correctly authenticates valid credentials and rejects invalid ones.



[
  {
    "username": "user1",
    "password": "pass123",
    "expectedOutcome": "success"
  },
  {
    "username": "user2",
    "password": "wrongpass",
    "expectedOutcome": "failure"
  }
]


#The active selection is a Java class named LoginTest that uses JUnit's parameterized testing feature to test login functionality. 
# The @RunWith(Parameterized.class) annotation specifies that this test class will use the Parameterized runner, 
# which allows the same test logic to be executed multiple times with different sets of input data.

#Parameterized Data Setup: The data() method, annotated with @Parameterized.Parameters, provides the test data as a collection of object arrays. 
# Each array represents a set of inputs and the expected outcome for a single test case. 
# For example, the first test case uses "user1" as the username, "pass123" as the password, and expects a "success" outcome. 
# The second test case uses "user2", "wrongpass", and expects a "failure" outcome. 
# This setup allows the test to iterate over multiple scenarios without duplicating code.

#Instance Variables: The class defines three private instance variables: username, password, and expectedOutcome. 
# These variables store the input data and expected result for each test case.

#Constructor: The constructor LoginTest(String username, String password, String expectedOutcome) 
# initializes the instance variables with the data provided for each test case. 
# JUnit's Parameterized runner automatically calls this constructor for each set of inputs defined in the data() method.

#Test Method: The testLogin() method, annotated with @Test, contains the logic for testing the login functionality. 
# Although the actual test logic is not implemented in the provided code, 
# it would typically involve using the username and password to simulate a login attempt and then comparing the result to the expectedOutcome.

#This structure is ideal for testing multiple input-output scenarios in a concise and maintainable way. 
# It ensures that the login functionality is validated against both valid and invalid credentials, helping to identify edge cases and potential bugs.

@RunWith(Parameterized.class)
public class LoginTest {
    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][] {
            { "user1", "pass123", "success" },
            { "user2", "wrongpass", "failure" }
        });
    }

    private String username;
    private String password;
    private String expectedOutcome;

    public LoginTest(String username, String password, String expectedOutcome) {
        this.username = username;
        this.password = password;
        this.expectedOutcome = expectedOutcome;
    }

    @Test
    public void testLogin() {
        // Test logic using username, password, and expectedOutcome
    }
}



#YAML Configuration: The first part of the selection is written in YAML format. It defines three environments: development, staging, and production. Each environment specifies:

#url: The base URL for the environment.
#browser: The browser to be used for testing or automation in that environment.
#apiEndpoint: The API endpoint specific to the environment.
#credentials: A nested structure containing username and password for authentication.
#For example, the development environment uses the URL https://dev.example.com, the browser chrome, and the API endpoint https://dev.api.example.com. 
# It also includes credentials with the username devUser and password devPass.

#JSON Configuration: The second part of the selection represents the same data in JSON format:

#

#YAML Configuration
development:
  url: "https://dev.example.com"
  browser: "chrome"
  apiEndpoint: "https://dev.api.example.com"
  credentials:
    username: "devUser"
    password: "devPass"

staging:
  url: "https://staging.example.com"
  browser: "firefox"
  apiEndpoint: "https://staging.api.example.com"
  credentials:
    username: "stageUser"
    password: "stagePass"

production:
  url: "https://www.example.com"
  browser: "chrome"
    apiEndpoint: "https://api.example.com"
    credentials:
        username: "prodUser"
        password: "prodPass"

#JSON Configuration
{
    "development": {
        "url": "https://dev.example.com",
        "browser": "chrome",
        "apiEndpoint": "https://dev.api.example.com"
    },
    "staging": {
        "url": "https://staging.example.com",
        "browser": "firefox",
        "apiEndpoint": "https://staging.api.example.com"
    },
    "production": {
        "url": "https://www.example.com",
        "browser": "chrome",
        "apiEndpoint": "https://api.example.com"
    }
}


#The active selection demonstrates a Python script that dynamically loads environment-specific configurations and credentials 
# for use in an application. It also includes examples of how environment variables are set in PowerShell and configuration details
# in property file formats.

#Python Script:

#The script begins by importing the os and json modules. 
# The json module is used to load a configuration file (config.json), which contains environment-specific settings such as API endpoints.
#The os.getenv() function retrieves environment variables. 
# The ENV variable determines the current environment (e.g., development, staging, or production), defaulting to development if not explicitly set.
#Based on the environment, the script retrieves credentials (USERNAME and PASSWORD) from environment variables. 
# These are dynamically constructed using the environment name (e.g., DEVELOPMENT_USERNAME for the development environment).
#The script prints the current environment, the API endpoint for that environment, and the username. 
# It explicitly warns against printing passwords in production for security reasons.
#Environment Variable Configuration:

#The PowerShell commands demonstrate how to set environment variables for different environments. 
# For example, DEVELOPMENT_USERNAME and DEVELOPMENT_PASSWORD are set for the development environment, 
# while similar variables are set for staging and production.
#Property Files:

#The property files and INI-style configuration sections provide static representations of environment-specific settings. 
# These include the url, browser, apiEndpoint, username, and password for each environment (development and staging are shown). 
# These files could be used as an alternative to or in conjunction with the JSON configuration file.
#This setup is useful for managing multiple environments in a project, such as development, staging, and production. 
# It ensures that environment-specific details like API endpoints and credentials are isolated and can be 
# dynamically loaded based on the current environment. 
# However, care must be taken to secure sensitive information like passwords, especially in production.


import os
import json

# Load JSON config
with open("config.json") as config_file:
    config = json.load(config_file)

# Retrieve environment-specific credentials
env = os.getenv("ENV", "development")  # Default to development if ENV is not set
username = os.getenv(f"{env.upper()}_USERNAME")
password = os.getenv(f"{env.upper()}_PASSWORD")

# Use credentials securely in your application
print(f"Running tests in {env} environment")
print(f"Using API: {config[env]['apiEndpoint']}")
print(f"Username: {username}")  # Do NOT print passwords in production

These environment variables are then configured as follows in PowerShell:
$env:DEVELOPMENT_USERNAME="devUser"
$env:DEVELOPMENT_PASSWORD="devPass"
$env:STAGING_USERNAME="stageUser"
$env:STAGING_PASSWORD="stagePass"
$env:PRODUCTION_USERNAME="prodUser"
$env:PRODUCTION_PASSWORD="prodPass"


#property files
url=https://dev.example.com
browser=chrome
apiEndpoint=https://dev.api.example.com
username=devUser
password=devPass


[development]
url = https://dev.example.com
browser = chrome
apiEndpoint = https://dev.api.example.com
username = devUser
password = devPass

[staging]
url = https://staging.example.com
browser = firefox
apiEndpoint = https://staging.api.example.com
username = stageUser
password = stagePass

url = os.getenv('URL')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


#The below code contains a mix of functions designed for automating browser interactions and making API calls. 
# Here's a breakdown of the functionality:

#login Function:
#This function simulates a user login process in a web application. It performs the following steps:

#Navigates to the login page (though the navigate_to_login_page function is not defined in the provided code).
#Enters the provided username and password into the respective input fields using the enter_text function.
#Submits the login form by clicking the login button using the click_button function.
#The function is reusable and can be called with different credentials, 
# as shown in the examples login("user1", "pass123") and login("admin", "adminpass").
#enter_text and click_button Functions:
#These helper functions abstract common browser interactions:

#enter_text locates an input field by its field_id and enters the specified text using Selenium's send_keys method.
#click_button locates a button by its button_id and simulates a click using Selenium's click method.
#Both functions rely on a driver object, which is assumed to be a Selenium WebDriver instance, though it is not explicitly defined in the code.
#navigate_to_page Function:
#This function navigates the browser to a specified URL using the WebDriver's get method. 
# It is a utility function that can be used to load any page during test automation.

#api_call Function:
#This function provides a way to make HTTP requests using the requests library. It supports both GET and POST methods:

#For GET requests, it sends the request to the specified endpoint with optional headers.
#For POST requests, it sends the request with optional data (as JSON) and headers.
#The function returns the response object, which can be used to inspect the status code, response body, etc.
#This code is likely part of a test automation framework, combining browser-based UI testing (using Selenium) 
# with API testing (using the requests library). 
# However, the code assumes the existence of a driver object and a navigate_to_login_page function, 
# which are not defined in the provided snippet. 
# These would need to be implemented or imported for the code to function correctly. 
# Additionally, the login function could be enhanced by adding error handling to manage scenarios where elements are not found or login fails.



def login(username, password):
    # Navigate to login page
    navigate_to_login_page()
    # Enter credentials
    enter_text("username_field", username)
    enter_text("password_field", password)
    # Submit login form
    click_button("login_button")

#This function can be called in different test cases with different credentials:
login("user1", "pass123")
login("admin", "adminpass")

def navigate_to_page(url):
    driver.get(url)

def enter_text(field_id, text):
    driver.find_element_by_id(field_id).send_keys(text)

def click_button(button_id):
    driver.find_element_by_id(button_id).click()



import requests

def api_call(method, endpoint, data=None, headers=None):
    if method == "GET":
        response = requests.get(endpoint, headers=headers)
    elif method == "POST":
        response = requests.post(endpoint, json=data, headers=headers)
    return response


#The below code contains a mix of database interaction and web form automation functionality. Here's a detailed explanation of each part:

#Database Connection (db_connect):
#The db_connect function establishes a connection to a PostgreSQL database using the psycopg2 library. 
# It connects to a database named testdb hosted on localhost at port 5432, using the credentials user and password. 
# The function returns the connection object (conn), which can be used to interact with the database. 
# This function is a reusable utility for establishing database connections.

#Executing Database Queries (execute_query):
#The execute_query function is designed to execute a SQL query and retrieve results. It:

#Calls db_connect to establish a database connection.
#Creates a cursor object using conn.cursor(), which is used to execute the query.
#Executes the provided query using cursor.execute(query).
#Fetches all results from the query using cursor.fetchall().
#Closes the database connection to release resources.
#Returns the query results to the caller.
#This function is useful for retrieving data from the database but does not handle queries that modify data (e.g., INSERT, UPDATE, DELETE). 
# Additionally, it lacks error handling, which could lead to unhandled exceptions if the query fails.
#Filling a Web Form (fill_form):
#The fill_form function automates the process of populating a web form. 
# It takes a dictionary (fields) where the keys represent the IDs of form fields, and the values represent the text to be entered. 
# For each key-value pair, it uses Selenium's find_element_by_id method to locate the input field by its ID 
# and enters the corresponding value using send_keys. 
# This function is useful for automating repetitive form-filling tasks in web applications.

#Submitting a Web Form (submit_form):
#The submit_form function automates the process of submitting a web form. 
# It takes the ID of the submit button (button_id) as an argument, locates the button using Selenium's find_element_by_id, 
# and clicks it using the click method. This function is typically used after the form fields have been populated using fill_form.

import psycopg2

def db_connect():
    conn = psycopg2.connect(database="testdb", user="user", password="password", host="localhost", port="5432")
    return conn

def execute_query(query):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def fill_form(fields):
    for field, value in fields.items():
        driver.find_element_by_id(field).send_keys(value)

def submit_form(button_id):
    driver.find_element_by_id(button_id).click()


#The below code conitnues the functionality above and contains utility functions for verifying API responses, 
# fetching database data, retrying API calls, and asserting the visibility of web elements. 
# Here's a detailed explanation of each function:

#verify_api_response:
#This function validates the response from an API call. It:

#Asserts that the status_code of the response matches the expected_status_code.
#Optionally, if expected_data is provided, it asserts that the JSON content of the response matches the expected data.
#This function is useful for ensuring that API responses meet expected criteria during testing or validation.
#fetch_data:
#This function retrieves data from a database by executing a SQL query. It:

#Calls the execute_query function (provided in the relevant implementations) to execute the query and fetch results.
#Optionally, if expected_columns is provided, it asserts that the number of columns in the first row 
#of the results matches the length of expected_columns.
#This function is helpful for validating database query results, ensuring that the structure of the data aligns with expectations.
#api_call_with_retry:
#This function performs an API call with a retry mechanism. It:

#Attempts the API call (using the api_call function) up to a specified number of retries (retries, default is 3).
#If the response has a status code of 200 (success), it returns the response.
#If an exception occurs during the API call, it prints an error message with the attempt number and continues retrying.
#If all retries fail, it raises an exception indicating that the API call failed after multiple attempts.
#This function is useful for handling transient issues in API calls, such as network instability or temporary server errors.
#assert_element_visible:
#This function checks whether a web element is visible on the page. It:

#Locates the element by its element_id using Selenium's find_element_by_id method.
#Asserts that the element is displayed using the is_displayed method. If the element is not visible, 
# it raises an assertion error with a descriptive message.
#This function is commonly used in UI testing to ensure that specific elements are visible to the user.
O

def verify_api_response(response, expected_status_code, expected_data=None):
    assert response.status_code == expected_status_code
    if expected_data:
        assert response.json() == expected_data



def fetch_data(query, expected_columns=None):
    results = execute_query(query)
    if expected_columns:
        assert len(results[0]) == len(expected_columns)
    return results



def api_call_with_retry(method, endpoint, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            response = api_call(method, endpoint)
            if response.status_code == 200:
                return response
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
        attempt += 1
    raise Exception("API call failed after multiple retries")


def assert_element_visible(element_id):
    element = driver.find_element_by_id(element_id)
    assert element.is_displayed(), f”Element {element_id} is not visible”


#The below code defines a LoginPage class and a test_login_success function, 
# which together implement a basic structure for automating the login process of a web application using Selenium.

#LoginPage Class:
#This class encapsulates the behavior and elements of a login page, following the Page Object Model (POM) design pattern. 
# POM is a popular design pattern in test automation that promotes maintainability and reusability 
# by separating page-specific logic from test scripts.

#Constructor (__init__):
#The constructor initializes the LoginPage object with a Selenium WebDriver instance (driver). 
# It locates and stores references to the username field, password field, and login button using their respective HTML element IDs
#  (username, password, and login). 
# These references are stored as instance variables (self.username_field, self.password_field, and self.login_button) for reuse in other methods.

#enter_username Method:
#This method takes a username as input and enters it into the username field using the send_keys method. 
# It abstracts the interaction with the username input field, making the code more readable and reusable.

#enter_password Method:
#Similar to enter_username, this method takes a password as input and enters it into the password field. 
# It encapsulates the interaction with the password input field.

#click_login Method:
#This method simulates a click on the login button. It abstracts the button click operation, making it easier to reuse in different test scenarios.

#test_login_success Function:
#This function represents a test case for verifying a successful login. It:

#Creates an instance of the LoginPage class, passing the Selenium WebDriver instance (driver) to interact with the login page.
#Calls the enter_username and enter_password methods to input the credentials ("user" and "password").
#Calls the click_login method to submit the login form.
#Additional assertions can be added after the login action to verify that the login was successful 
# (e.g., checking for a redirect to a dashboard page or the presence of a specific element).

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element_by_id("username")
        self.password_field = driver.find_element_by_id("password")
        self.login_button = driver.find_element_by_id("login")

    def enter_username(self, username):
        self.username_field.send_keys(username)

    def enter_password(self, password):
        self.password_field.send_keys(password)

    def click_login(self):
        self.login_button.click()



def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("user")
    login_page.enter_password("password")
    login_page.click_login()
    # Further assertions can be added here


#The below code demonstrates a streamlined approach to implementing and testing login functionality using the Page Object Model (POM) design pattern. 
# It includes two classes, DashboardPage and LoginPage, and a simplified test case for verifying successful login.

#DashboardPage Class:
#This class represents the dashboard page that users are redirected to after logging in. 
# It encapsulates the behavior and elements specific to the dashboard:

#Constructor (__init__): The constructor initializes the DashboardPage object with a Selenium WebDriver instance (driver) 
# and locates the logout button using its HTML element ID (logout). This allows the class to interact with the logout button.
#click_logout Method: This method simulates a click on the logout button, enabling the user to log out of the application. 
# It abstracts the logout functionality, making it reusable in tests.
#LoginPage Class:
#This class models the login page and provides methods for interacting with its elements:

#login Method: This method combines the steps for logging in—entering the username, entering the password, 
# and clicking the login button—into a single reusable method. It calls the enter_username, enter_password, 
# and click_login methods (assumed to be defined elsewhere in the class). This abstraction simplifies test scripts by reducing repetitive code.
#Simplified Test Case:
#The test case test_login_success demonstrates how the LoginPage class can be used to test the login functionality:

#It creates an instance of the LoginPage class, passing the Selenium WebDriver instance (driver) to interact with the login page.
#It calls the login method with a username ("user") and password ("password") to perform the login operation.
#Additional assertions can be added after the login step to verify that the user has successfully logged in 
# (e.g., checking for a redirect to the dashboard or the presence of user-specific elements).

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_button = driver.find_element_by_id("logout")

    def click_logout(self):
        self.logout_button.click()



class LoginPage:
    # Existing methods...

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

The corresponding test can be simplified:
def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.login("user", "password")
    # Further assertions


class LoginPage:
    # Existing methods...

    def navigate_to_dashboard(self):
        self.click_login()
        return DashboardPage(self.driver)



def test_user_flow(driver):
    login_page = LoginPage(driver)
    dashboard_page = login_page.login("user", "password")
    assert dashboard_page.is_displayed()
    dashboard_page.click_logout()


class DashboardPage:
    # Existing methods...

    def verify_user_logged_in(self, username):
        welcome_message = self.driver.find_element_by_id("welcome_message").text
        assert username in welcome_message, f"Expected username '{username}' not found."

#This allows for more compact tests:
def test_login_success(driver):
    login_page = LoginPage(driver)
    dashboard_page = login_page.login("user", "password")
    dashboard_page.verify_user_logged_in("user")


#The below code defines two utility functions, setup_user_session and teardown_user_session, 
# which are designed to manage the setup and cleanup of a user session in a web application. 
# These functions are essential for ensuring that tests begin with a consistent application state and leave no residual state after execution.

#setup_user_session Function:
#This function is responsible for creating a user session by logging into the application. 
# It navigates the browser to the login page (https://example.com/login) using the Selenium WebDriver's get method. 
# Then, it creates an instance of the LoginPage class, which encapsulates the login page's behavior. 
# The login method of the LoginPage class is called with predefined credentials ("user" and "password") to authenticate the user. 
# This function ensures that any test requiring a logged-in user can reuse this setup logic, promoting consistency and reducing code duplication.

#teardown_user_session Function:
#This function handles the cleanup of the user session by logging the user out of the application. 
# It creates an instance of the DashboardPage class, which represents the dashboard page displayed after a successful login. 
# The click_logout method of the DashboardPage class is called to simulate a logout action. 
# This ensures that the application state is reset after a test, preventing interference with subsequent tests.

def setup_user_session(driver):
    # Code to create a user session
    driver.get("https://example.com/login")
    login_page = LoginPage(driver)
    login_page.login("user", "password")

def teardown_user_session(driver):
    # Code to log out and clean up the user session
    dashboard_page = DashboardPage(driver)
    dashboard_page.click_logout()


#The below code demonstrates a set of test functions designed to validate various user-related functionalities in a web application. 
# These tests follow a structured approach, incorporating setup, teardown, and reusable preconditions to ensure modularity and maintainability.

#test_user_profile_update Function:
#This test verifies the functionality of updating a user's profile. 
# It begins by setting up a user session using the setup_user_session function, which logs the user into the application. 
# Within a try-finally block, the test interacts with the ProfilePage object to update the user's profile details (e.g., name and email). 
# The assert statement ensures that the profile update was successful by calling the verify_update_success method. 
# Finally, the teardown_user_session function is called in the finally block to log the user out and clean up the session, 
# ensuring the application state is reset regardless of test success or failure.

#create_test_user Function:
#This function is a reusable precondition for creating a test user in the application. 
# It interacts with the AdminPage object to add a new user with predefined credentials ("testuser", "password", and "testuser@example.com"). 
# This function is designed to be used across multiple test cases that require a test user to exist before execution.

#test_user_login Function:
#This test validates the login functionality of the application. 
# It begins by calling the create_test_user function to ensure a test user exists. 
# The actual login logic is not shown in the active selection, 
# but the function is structured to continue with additional test steps after the user is created. 
# This modular approach ensures that the test user setup is consistent and reusable.

#cleanup_test_user Function:
#This function is responsible for cleaning up the test user after a test has run. 
# It interacts with the AdminPage object to delete the user with the username "testuser". 
# This ensures that the application state is reset, preventing interference with subsequent tests.

#test_user_deletion Function:
#This test verifies the functionality of deleting a user. It begins by creating a test user using the create_test_user function. 
# Within a try-finally block, the test interacts with the UserPage object to delete the user 
# and asserts that the deletion was successful by calling the verify_user_deleted method. 
# The cleanup_test_user function is called in the finally block to ensure the test user is removed, even if the test fails.


def test_user_profile_update(driver):
    setup_user_session(driver)  # Setup
    try:
        # Test actions for updating user profile
        profile_page = ProfilePage(driver)
        profile_page.update_profile("New Name", "newemail@example.com")
        assert profile_page.verify_update_success()
    finally:
        teardown_user_session(driver)  # Teardown


def create_test_user(driver):
    # Code to create a test user in the application
    admin_page = AdminPage(driver)
    admin_page.add_user("testuser", "password", "testuser@example.com")

#This precondition can be reused in multiple test cases:
def test_user_login(driver):
    create_test_user(driver)
    # Continue with test logic



def cleanup_test_user(driver):
    # Code to delete the test user after the test runs
    admin_page = AdminPage(driver)
    admin_page.delete_user("testuser")


def test_user_deletion(driver):
    create_test_user(driver)
    try:
        # Test logic for user deletion
        user_page = UserPage(driver)
        user_page.delete_user("testuser")
        assert user_page.verify_user_deleted("testuser")
    finally:
        cleanup_test_user(driver)


#The below code demonstrates a well-structured approach to writing reusable and maintainable test cases using pytest. 
# It includes the use of fixtures, custom assertions, and modular test logic to validate user-related functionalities in a web application.

#user_session Fixture:
#The user_session fixture is a reusable setup and teardown mechanism for managing a user session during tests. 
# It uses the setup_user_session function to log the user into the application before the test runs. 
# The yield statement acts as a placeholder where the test logic executes. 
# After the test completes, the teardown_user_session function is called to log the user out and clean up the session. 
# This ensures that each test starts with a consistent state and leaves no residual state, improving test reliability and maintainability.

#test_user_profile_update Test Case:
#This test case leverages the user_session fixture to ensure the user is logged in before the test begins. 
# It interacts with the ProfilePage object to update the user's profile details (e.g., name and email). 
# The assert statement verifies that the profile update was successful by calling the verify_update_success method. 
# By using the fixture, the test avoids duplicating session management logic, making it more concise and easier to maintain.

#assert_user_logged_in Custom Assertion:
#This custom assertion verifies that a user is successfully logged in by checking the presence of the username 
# in the welcome message displayed on the page. 
# It uses Selenium's find_element_by_id method to locate the welcome message element and asserts that the username is part of the text. 
# If the assertion fails, it provides a clear error message, making debugging easier. 
# This assertion is reusable across multiple test cases, as demonstrated in the test_login_success test.

#test_login_success Test Case:
#This test case validates the login functionality by ensuring that the user is logged in after the login logic executes. 
# It uses the assert_user_logged_in custom assertion to check for the presence of the username in the welcome message. 
# This modular approach allows the test to focus on the specific functionality being tested while reusing shared logic for verification.

#assert_user_profile_updated Custom Assertion:
#This custom assertion verifies that a user's profile has been updated correctly. 
# It interacts with the ProfilePage object to retrieve the updated email and compares it with the expected email. 
# Additionally, it calls the assert_user_logged_in assertion to ensure the user is still logged in. 
# This layered approach to assertions improves test clarity and ensures comprehensive validation of the profile update functionality.

import pytest

@pytest.fixture
def user_session(driver):
    setup_user_session(driver)  # Setup
    yield  # Test runs here
    teardown_user_session(driver)  # Teardown

#The test case can then leverage this fixture:
def test_user_profile_update(user_session, driver):
    profile_page = ProfilePage(driver)
    profile_page.update_profile("New Name", "newemail@example.com")
    assert profile_page.verify_update_success()



def assert_user_logged_in(driver, username):
    """Custom assertion to verify that the user is logged in."""
    welcome_message = driver.find_element_by_id("welcome_message").text
    assert username in welcome_message, f"Expected username '{username}' not found in '{welcome_message}'"

#This custom assertion can then be reused in multiple test cases:
def test_login_success(driver):
    # Assume successful login logic here
    assert_user_logged_in(driver, "testuser")


def assert_user_profile_updated(driver, username, expected_email):
    """Custom assertion to verify that the user profile has been updated correctly."""
    profile_page = ProfilePage(driver)
    actual_email = profile_page.get_email()
    assert actual_email == expected_email, f"Expected email '{expected_email}', but got '{actual_email}'"
    assert_user_logged_in(driver, username)

#The active selection defines a CustomAssertions class that encapsulates reusable assertion methods 
# for verifying web elements during automated testing. 
# These methods are static, meaning they can be called directly on the class without requiring an instance. 
# Additionally, the selection includes a test_profile_update function that demonstrates how these assertions can be used in a test case.

#CustomAssertions Class:
#This class provides two static methods for common assertions:

#assert_element_visible: This method checks whether a specific element, identified by its element_id, is visible on the page. 
# It uses Selenium's find_element_by_id method to locate the element and then calls the is_displayed method to verify its visibility. 
# If the element is not visible, the assertion fails with a descriptive error message, making it easier to debug.

#assert_text_in_element: This method verifies that a specific text is present within an element identified by its element_id. 
# It retrieves the element's text using Selenium and checks if the expected_text is a substring of the element's text. 
# If the text is not found, the assertion fails with a clear error message, specifying both the expected text and the element's ID.

#These methods encapsulate common validation logic, improving code reusability and readability. 
# By centralizing assertions in a dedicated class, the code becomes easier to maintain and extend.

#test_profile_update Function:
#This function simulates a test case for updating a user profile. 
# While the actual logic for updating the profile is assumed to be implemented elsewhere, 
# the function focuses on verifying the outcome of the operation. 
# It uses the CustomAssertions methods to perform two checks:

#It ensures that a success message element (with ID "success_message") is visible on the page.
#It verifies that the success message contains the text "Profile updated successfully."
#These assertions validate both the presence and correctness of the success message, 
#ensuring that the profile update operation behaves as expected.

class CustomAssertions:
    @staticmethod
    def assert_element_visible(driver, element_id):
        """Asserts that a specific element is visible on the page."""
        element = driver.find_element_by_id(element_id)
        assert element.is_displayed(), f"Element with ID '{element_id}' is not visible."

    @staticmethod
    def assert_text_in_element(driver, element_id, expected_text):
        """Asserts that a specific text is present in an element."""
        element = driver.find_element_by_id(element_id)
        assert expected_text in element.text, f"Expected text '{expected_text}' not found in element with ID '{element_id}'."


def test_profile_update(driver):
    # Assume logic for updating profile here
    CustomAssertions.assert_element_visible(driver, "success_message")
    CustomAssertions.assert_text_in_element(driver, "success_message", "Profile updated successfully.")


#The below code demonstrates a combination of reusable assertion methods and a test case for verifying user login functionality in a web application. 
# It highlights the use of static methods for common assertions and a structured approach to managing test setup and teardown.

#AssertionLibrary Class:
#The AssertionLibrary class provides two static methods for reusable assertions:

#assert_element_present: This method verifies that a specific web element, 
# identified by a locator (e.g., a tuple like ("id", "element_id")), is present on the page. 
# It uses Selenium's find_element method to locate the element and asserts that the element is not None. 
# If the element is missing, the assertion fails with a descriptive error message, making it easier to debug.

#assert_status_code: This method checks whether an HTTP response's status code matches the expected value. 
# It compares the response.status_code with the expected_status and raises an assertion error with a clear message if they do not match. 
# This is particularly useful for testing API responses.

#These static methods encapsulate common validation logic, making them reusable across multiple test cases and improving code maintainability.

#test_assert_user_logged_in Function:
#This test case validates the functionality of the assert_user_logged_in custom assertion, 
# which checks whether a user is successfully logged in. 
# The test follows a structured approach:

#Setup: The setup_user_session function is called to log the user into the application. 
# This function navigates to the login page and performs the login operation using the LoginPage object.

#Test Execution: The assert_user_logged_in function is called to verify that the user (with username "testuser") is logged in. 
# This function checks the welcome message on the page to ensure it contains the username.

#Teardown: The teardown_user_session function is called in a finally block to ensure that the user session is cleaned up, 
# even if the test fails. This function logs the user out using the DashboardPage object.

class AssertionLibrary:
    @staticmethod
    def assert_element_present(driver, locator):
        element = driver.find_element(*locator)
        assert element is not None, f"Element {locator} should be present."

    @staticmethod
    def assert_status_code(response, expected_status):
        assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code}."

def test_assert_user_logged_in(driver):
    # Setup a user session
    setup_user_session(driver)
    try:
        # Test the custom assertion
        assert_user_logged_in(driver, "testuser")
    finally:
        teardown_user_session(driver)


#The below codecontains two functions, login_user and verify_user_profile, which are part of a test automation script. 
# These functions are designed to interact with a web application using Selenium and validate specific behaviors. 
# Additionally, there is a JSON structure at the end, which appears to define test data for a user.

#login_user Function:
#This function automates the process of logging a user into the application. 
# It takes three parameters: driver (the Selenium WebDriver instance), username, and password. 
# The function creates an instance of the LoginPage class, which encapsulates the login page's elements and actions. 
# It then performs the following steps:

#Calls enter_username to input the provided username into the username field.
#Calls enter_password to input the provided password into the password field.
#Calls click_login to submit the login form.
#This function abstracts the login process, making it reusable across multiple test cases. 
# By delegating the actual interactions to the LoginPage class, it adheres to the Page Object Model (POM) design pattern, 
# which improves maintainability and readability.

#verify_user_profile Function:
#This function verifies that the email address displayed on a user's profile matches the expected value. 
# It takes three parameters: driver, username, and expected_email. The function performs the following steps:

#Creates an instance of the ProfilePage class, which represents the user's profile page.
#Retrieves the actual email address displayed on the profile page by calling get_email.
#Asserts that the actual_email matches the expected_email. 
# If the assertion fails, it raises an error with a descriptive message, including the username and the mismatched email values.
#This function is useful for validating that the user's profile information is correctly displayed after login or other operations.

#Test Data:
#The JSON structure at the end defines a list of users, with each user represented as a dictionary containing a username and password. 
# In this case, there is one user with the username "testuser" and the password "password123". 
# This data can be used to parameterize test cases, allowing the same test logic to be executed for different users.


def login_user(driver, username, password):
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()


def verify_user_profile(driver, username, expected_email):
    profile_page = ProfilePage(driver)
    actual_email = profile_page.get_email()
    assert actual_email == expected_email, f"Expected {expected_email}, got {actual_email} for user {username}."

{
    "users": [
        { "username": "testuser", "password": "password123" }
    ]
}
