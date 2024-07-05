# PG-Mountain-Water
Graphics programming project using OpenGL and ModernGL to create a water and mountain environment.

## Prerequisites
Make sure you have Python 3.7+ and pip installed on your system.

## Instructions to Clone and Run the Project Locally

### Step 1: Clone the Repository
git@github.com:horby17/PG-Mountain-Water.git

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
