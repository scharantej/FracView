
# Import necessary libraries
from flask import Flask, render_template, request, send_file
import numpy as np
import matplotlib.pyplot as plt

# Create a Flask application
app = Flask(__name__)

# Main route for the application
@app.route('/')
def index():
    # Render the index.html page
    return render_template('index.html')

# Route for handling requests to set the rendering parameters
@app.route('/set-params', methods=['POST'])
def set_params():
    # Parse the request body to get the rendering parameters
    params = request.get_json()

    # Update the global variables with the new parameters
    global zoom_level
    global pan_position
    global color_scheme

    zoom_level = params['zoom_level']
    pan_position = params['pan_position']
    color_scheme = params['color_scheme']

    # Return a success message
    return {'success': True}

# Route for generating the Mandelbrot image
@app.route('/get-image', methods=['GET'])
def get_image():
    # Generate the Mandelbrot image based on the current rendering parameters
    image = generate_mandelbrot(zoom_level, pan_position, color_scheme)

    # Return the image data as a response
    return send_file(image, mimetype='image/png')

# Route for loading the information page
@app.route('/info')
def info():
    # Render the info.html page
    return render_template('info.html')

# Main driver function
if __name__ == '__main__':
    # Set the initial rendering parameters
    zoom_level = 2
    pan_position = np.array([0, 0])
    color_scheme = 'viridis'

    # Start the Flask application
    app.run(debug=True)
