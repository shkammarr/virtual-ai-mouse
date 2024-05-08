# AI Virtual Mouse 
This project enables users to control their computer mouse using hand gestures captured by their webcam. The system detects hand movements and finger gestures in real-time, translating them into corresponding mouse actions such as left-click, right-click, double-click, and scrolling up/down.

## How it Works
![](https://github.com/shkammarr/virtual-ai-mouse/blob/main/virtual-mouse.gif)

## Requirements
You must have Python version 3.9+ installed on your device. Following Modules need to be installed for proper working of the project :

- OpenCV
- NumPy
- Mouse
- cvzone (Custom Hand Tracking Module)

## OpenCV

OpenCV (Open Source Computer Vision Library) is a powerful open-source computer vision and machine learning software library. It provides a wide range of functionalities for image and video analysis, including object detection, facial recognition, feature detection, and more.

Installation of this module :
```bash
  pip install opencv-python
```

## NumPy

NumPy is a fundamental package for scientific computing with Python. It provides support for multidimensional arrays, matrices, and mathematical functions to operate on these arrays efficiently.In this project, NumPy is used for numerical operations, particularly for interpolating hand positions and performing calculations related to image processing.

Installation of this module :
```bash
  pip install numpy
```

## Mouse 

Mouse is a Python library that provides cross-platform functions for controlling the mouse cursor on a computer. It allows you to simulate mouse clicks, movements, scrolling, and other interactions programmatically. 

Installation of this module :
```bash
  pip install mouse
```

## Install all dependencies at once 

```bash
 pip install opencv-python numpy mouse
 ```

## How to Use
Once you are done installing all dependencies you can run the program & can operate mouse with following actions : 

- **Index Finger**: Controls the mouse cursor.
- **Index + Middle Finger** (distance between them becomes 2 cm): Left-click.
- **Index + Middle + Ring Finger** (distance between them becomes 2 cm): Right-click.
- **Thumb + Index + Middle Finger**: Scroll up.
- **All Fingers Slightly Closed**: Scroll down.
## Note
- This project supports single-hand control at a time (either left hand or right hand).
- You need to adjust the screen size in the code(depending upon the size of your screen for optimum performance)
- To know the exact size of your screen run scrn_size.py file
- Use a well-lit environment and ensure that your hand is clearly visible to the camera for optimal performance.
- Please note that **speed and efficiency of this project may vary depending on factors such as hardware configuration and input data size.**
  
## 🔗 Links

<div align="left">
  <a href="https://www.linkedin.com/in/shkammar/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="linkedin logo"  />
  </a>
  <a href="https://t.me/Insaane_xd" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Telegram&logo=telegram&label=&color=2CA5E0&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="telegram logo"  /> <br>
  </a>
  <a href="https://discordapp.com/users/707265337133105183" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Discord&logo=discord&label=&color=7289DA&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="discord logo"  />
  </a>
  <a href="mailto:ammar.info19@gmail.com" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="gmail logo"  />
  </a>
</div>



