import instaloader
from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('home.html')  # This will serve your HTML file

# Example of handling form submission (POST request)
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')

    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    # Log in using the submitted Instagram username and password
    try:
        L.login(username, password)  # Use the submitted username and password

        # Load the user's profile
        profile = instaloader.Profile.from_username(L.context, username)

        # Get the followers and following lists
        followers = set(follower.username for follower in profile.get_followers())
        following = set(followee.username for followee in profile.get_followees())

        # Find users you follow but who don't follow you back
        not_following_back = following - followers  # Set difference

        # Prepare a response
        not_following_back_list = "\n".join(not_following_back)
        return render_template('result.html', not_following_back=not_following_back)
    
    except Exception as e:
        return f"An error occurred: {str(e)}"  # Handle login errors

if __name__ == '__main__':
    app.run(debug=True)