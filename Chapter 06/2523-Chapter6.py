#This code implements a simple testing framework in Python, consisting of two main classes: TestCase and TestRunner. 
#It also includes sample test functions and demonstrates how to use the framework to execute and report test results.

#TestCase Class:
#The TestCase class represents an individual test case. It encapsulates the following:

#Attributes:

#name: A string representing the name of the test case.
#test_function: A callable function that contains the test logic.
#passed: A boolean indicating whether the test passed or failed (default is False).
#error_message: A string to store the error message if the test fails (default is None).
#Methods:

#run: Executes the test_function inside a try block. If the function runs successfully, the test is marked as passed (passed = True). 
# If an exception occurs, the test is marked as failed (passed = False), and the exception message is stored in error_message.
#This class provides a clean abstraction for managing individual test cases, including their execution and result tracking.

#TestRunner Class:
#The TestRunner class manages the execution of multiple test cases and reports their results. It includes:

#Attributes:

#test_cases: A list to store TestCase instances.
#results: A list to store tuples of test cases and their execution durations.
#Methods:

#add_test_case: Adds a TestCase instance to the test_cases list.
#run_tests: Iterates through all test cases, measures their execution time using time.time(), runs each test case, and stores the results (including duration) in the results list.
#report_results: Prints a summary of the test results. For each test case, it displays whether the test passed or failed, the execution duration, and any error message if applicable.
#This class provides a structured way to manage and execute multiple test cases, ensuring that results are reported clearly.

#Sample Test Functions:
#Three sample test functions are defined to demonstrate the framework:

#test_success: A simple test that passes (1 + 1 == 2).
#test_failure: A test that fails (1 + 1 == 3).
#test_exception: A test that raises an intentional exception (ValueError).
#These functions showcase different outcomes (success, failure, and exception) that the framework can handle.

#Usage Example:
#Instances of TestCase are created for each sample test function, with descriptive names.
#A TestRunner instance is instantiated.
#The test cases are added to the runner using add_test_case.#The tests are executed using run_tests.
#The results are reported using report_results.


import os
import time

class TestCase:
    def __init__(self, name, test_function):
        self.name = name
        self.test_function = test_function
        self.passed = False
        self.error_message = None

    def run(self):
        try:
            self.test_function()
            self.passed = True
        except Exception as e:
            self.error_message = str(e)
            self.passed = False

class TestRunner:
    def __init__(self):
        self.test_cases = []
        self.results = []

    def add_test_case(self, test_case):
        self.test_cases.append(test_case)

    def run_tests(self):
        for test_case in self.test_cases:
            start_time = time.time() //tracks execution time of test
            test_case.run()
            duration = time.time() - start_time
            self.results.append((test_case, duration))

    def report_results(self):
        print("\nTest Results:")
        for test_case, duration in self.results: //test will only pass if doesn’t exceed specific benchmark
            if test_case.passed:
                print(f"✓ {test_case.name} - Passed (Duration: {duration:.4f}s)")
            else:
                print(f"✗ {test_case.name} - Failed (Duration: {duration:.4f}s) - Error: {test_case.error_message}")



# Sample test functions
def test_success():
    assert 1 + 1 == 2

def test_failure():
    assert 1 + 1 == 3

def test_exception():
    raise ValueError("This is an intentional error.")

# Create instances of TestCase
test1 = TestCase("Test Success", test_success)
test2 = TestCase("Test Failure", test_failure)
test3 = TestCase("Test Exception", test_exception)


# Instantiate the test runner
runner = TestRunner()

# Add test cases to the runner
runner.add_test_case(test1)
runner.add_test_case(test2)
runner.add_test_case(test3)

# Run the tests
runner.run_tests()

# Report the results
runner.report_results()
