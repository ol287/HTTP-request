from flask import Flask, request, jsonify
import requests
import threading

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

# Function to start the Flask app in a separate thread
def run_flask_app():
    app.run(debug=True, use_reloader=False)

# Function to make requests to the Flask app
def make_requests():
    # Make a GET request to the /hello endpoint
    response_get = requests.get('http://127.0.0.1:5000/hello?name=Olivia')
    print('GET /hello Response:', response_get.json())

    # Make a POST request to the /greet endpoint
    response_post = requests.post('http://127.0.0.1:5000/greet', json={'name': 'Olivia'})
    print('POST /greet Response:', response_post.json())

if __name__ == '__main__':
    # Start the Flask app in a new thread
    threading.Thread(target=run_flask_app).start()

    # Make sure the Flask app has time to start up before sending requests
    import time
    time.sleep(2)

    # Make the requests to the Flask app
    make_requests()
