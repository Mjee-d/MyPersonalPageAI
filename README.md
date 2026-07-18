# Coffee Image Classifier

This project uses a Google Teachable Machine model trained to recognize two distinct classes. The model is deployed and verified using a Python script inside a Google Colab notebook environment.

## Repository Structure
* `model/`: Contains the pre-trained Keras model (`.h5`) and class labels text file.
* `test_images/`: Sample image used to verify the model accuracy.
* `teachable_machine_test.ipynb`: Jupyter notebook containing the inference pipeline code.

## How to Run
1. Open Google Colab and upload the `teachable_machine_test.ipynb` notebook.
2. Upload the files from the `model/` directory into your Colab runtime.
3. Upload a test image to the runtime environment.
4. Execute the cells to see the classification output and confidence scores.

# Real-Time Multi-Color Recognition

A computer vision application built with Python and OpenCV that tracks multiple colors (Blue, Orange, and Red) simultaneously in a live webcam feed using HSV color space thresholding.

## Prerequisites & Environment
This project was developed and tested using the following tools:
* **Environment Manager:** Anaconda
* **IDE:** Visual Studio Code (VS Code)
* **Core Libraries:** OpenCV (`opencv-python`), NumPy

## Installation & Setup
### Set Up Anaconda Environment:
in the Anaconda Environments search for opencv and install it
then open the Anaconda Prompt or terminal and create/activate the environment using:

conda create -n color_track python=3.10
conda activate color_track

### Running the Project in VS Code:
Open Visual Studio Code and select your project folder.

Set your Python interpreter to the newly created color_track environment.

Open your script (color_detection.py) and click the Play button in the top right corner to start the webcam tracking.

### How to Add Another Color to the Tracking System
The project is built dynamically, meaning you don't need to rewrite any loops or logic to track a new color. You only need to add its configuration parameters to the colors_to_track dictionary.

Step 1: Find the HSV Bounds
Every color is defined by its Lower and Upper bounds in the HSV (Hue, Saturation, Value) color space. For example, if you want to add Green, a standard range is:

Lower Bound: [40, 50, 50]

Upper Bound: [80, 255, 255]

Step 2: Choose a Display Color (BGR)
OpenCV uses BGR (Blue, Green, Red) layout instead of RGB. Pick the color you want the overlay box and text label to be.

Example for Green: (0, 255, 0)

Step 3: Update the Dictionary in Your Code
Open color_detection.py and simply add your new color profile directly into the colors_to_track block like this:

```python
colors_to_track = {
    "Blue": { ... },
    "Orange": { ... },
    "Red": { ... },
    
    "Green": {
        "lower": np.array([40, 50, 50]),
        "upper": np.array([80, 255, 255]),
        "bgr_color": (0, 255, 0)
    }
}
