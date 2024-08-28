from flask import Flask, request, jsonify
import unittest

# Create a new Flask web application
app = Flask(__name__)

# Define a route for the GET request on the /hello path
@app.route('/hello', methods=['GET'])
def hello_world():
    # Get the 'name' query parameter from the URL, default to 'World' if not provided
    name = request.args.get('name', 'World')
    
    # Create a response dictionary with a greeting message
    response = {
        'message': f'Hello, {name}!'
    }
    
    # Return the response as JSON with an HTTP status code of 200 (OK)
    return jsonify(response), 200

# Define a route for the POST request on the /greet path
@app.route('/greet', methods=['POST'])
def greet():
    # Get the JSON body of the request
    data = request.json
    # Extract the 'name' field from the JSON, default to 'World' if not provided
    name = data.get('name', 'World')
    
    # Create a response dictionary with a greeting message
    response = {
        'message': f'Greetings, {name}!'
    }
    
    # Return the response as JSON with an HTTP status code of 201 (Created)
    return jsonify(response), 201

# Below is the test case for the Flask application using the unittest module
class FlaskTestCase(unittest.TestCase):

    # Method to set up the test environment
    def setUp(self):
        # Set up a test client for the Flask application
        self.app = app.test_client()
        self.app.testing = True

    # Test the GET request to /hello
    def test_hello_world(self):
        # Send a GET request to /hello with a 'name' query parameter
        response = self.app.get('/hello?name=Olivia')
        # Parse the JSON response
        data = response.get_json()
        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the message in the response is as expected
        self.assertEqual(data['message'], 'Hello, Olivia!')

    # Test the POST request to /greet
    def test_greet(self):
        # Send a POST request to /greet with a JSON body containing 'name'
        response = self.app.post('/greet', json={'name': 'Olivia'})
        # Parse the JSON response
        data = response.get_json()
        # Check if the status code is 201 (Created)
        self.assertEqual(response.status_code, 201)
        # Check if the message in the response is as expected
        self.assertEqual(data['message'], 'Greetings, Olivia!')

# Entry point for running the Flask app or the tests
if __name__ == '__main__':
    # If this script is executed, run the Flask development server
    # or if tests are being run, execute the tests
    import sys
    if 'test' in sys.argv:
        # Run the unit tests if 'test' is in the command line arguments
        unittest.main()
    else:
        # Otherwise, run the Flask app normally
        app.run(debug=True)

#to run the tests run the following command line : "python -m unittest main.py"
