## Flask Application Design for Navigating and Exploring the Mandelbrot Ensemble

### HTML Files

**index.html**

- Main HTML page for the application.
- Contains the interactive UI elements for navigating and exploring the Mandelbrot ensemble.
- Includes controls for zooming, panning, and adjusting the rendering parameters.

**info.html**

- Provides additional information about the Mandelbrot ensemble and its mathematical properties.
- Can include interactive visualizations or explanations to enhance understanding.

### Routes

**@app.route('/')**

- Main route that loads the `index.html` page.
- This is the initial page of the application.

**@app.route('/set-params', methods=['POST'])**

- Route for handling requests to set the rendering parameters for the Mandelbrot ensemble.
- Parses the request body to update the values for parameters such as the zoom level, pan position, and color scheme.

**@app.route('/get-image', methods=['GET'])**

- Route for generating the Mandelbrot image based on the current rendering parameters.
- Generates a high-resolution image using NumPy and matplotlib.
- Returns the image data as a response.

**@app.route('/info')**

- Route for loading the `info.html` page.
- Provides access to additional information about the Mandelbrot ensemble.