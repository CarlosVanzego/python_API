from flask import Flask, request, jsonify
# Create an instance of the Flask class
app = Flask(__name__)

#  GET route to retrieve user data on the user_id @app.route
@app.route("/hello-world")
def get_user():
    # Sample user data to retrun as a JSON response
    user_data = "Hello World"


    #  Check if an 'extra' query parameter is provided in the request
    # extra = request.args.get("extra")
    # if extra:
    #     # Add extra data if provided 
    #     user_data["extra"] = extra 
    # Return the user_data dictionary as a JSON response with a 200 OK status code when successful    
    return (user_data), 200    


# POST route to create a new user
@app.route("/create-user", methods=["POST"])
def create_user():
    # Extract JSON data from the request body
    data = request.get_json()
    # Return the received data as a JSON response with a 201 Created status when successful
    return jsonify(data), 201

# Run the application if this file is executed directly 
if __name__ == "__main__":
    # Start the Flask development with the debug mode enabled 
    app.run(debug=True)

