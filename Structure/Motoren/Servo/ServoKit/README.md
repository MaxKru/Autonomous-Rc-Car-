# ServoKit
Install the Adafruit ServoKit Circuit Python library on the NVIDIA Jetson Nano Developer Kit

Here are some convenience scripts to get servo motors working with the NVIDIA Jetson Nano Developer Kit using a PCA9685 breakout board over I2C.

<h3>installServoKit.sh</h3>
installServoKit.sh first sets the permissions for i2c and gpio so that they can be accessed in user space by the current user. Next, pip is installed. Finally, the adafruit-circuitpython-servokit library (along with its supporting libaries) are installed. To run the script:<br>

<blockquote>$ ./installServoKit.sh</blockquote>

