# PG-Mountain-Water
Graphics programming project using OpenGL and ModernGL to create a water and mountain environment.
## 1. Setup and Initialization (main.py)
- Initialize Pygame and create an OpenGL context with ModernGL.
- Load vertex and fragment shaders from GLSL files.
- Define vertex data for a full-screen quad.
- Create and bind vertex buffer and vertex array objects.
- Set up camera attributes including position, front direction, and movement speed.
## 2. Rendering (main.py)
- Clear the context and render the vertex array.
- Update shader uniforms with the current time and camera position.
- Handle keyboard and mouse inputs to move the camera.
- Implement mouse movement to adjust camera orientation.
## 3. Shaders (vertex.glsl)
- Vertex shader transforms vertex positions from 2D to 4D space.
## 4. Shaders (fragment.glsl)
- Fragment shader performs ray marching to render terrain and water.
- Uses noise functions and fractal Brownian motion (FBM) to generate terrain features.
- Computes lighting, shadows, and ambient occlusion.
- Mixes sky and terrain colors based on the ray-marched distance.

## Prerequisites
Make sure you have Python 3.7+ and pip installed on your system.

## Instructions to Clone and Run the Project Locally

### Step 1: Clone the Repository
https://github.com/horby17/PG-Mountain-Water.git

### Step 2: Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Step 3: Install Dependencies
pip install -r requirements.txt

### Step 4: Run the Project
python main.py

## Project Structure
main.py: Main file that initializes the graphical environment and contains the rendering logic.
programs/vertex.glsl: Vertex shader used to transform vertices.
programs/fragment.glsl: Fragment shader used to calculate pixel colors.

## If you want to see more about the topic, please enter in the link description
https://vimeo.com/977333500?share=copy
