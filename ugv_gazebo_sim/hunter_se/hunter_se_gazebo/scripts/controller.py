#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import pygame

# Initialize pygame and joystick
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Initialize ROS node
rospy.init_node('gamepad_steering', anonymous=True)
cmd_vel_pub = rospy.Publisher('/ackermann_steering_controller/cmd_vel', Twist, queue_size=10)

# Set the rate of publishing messages
rate = rospy.Rate(10)  # 10 Hz

def get_gamepad_input():
    pygame.event.pump()
    
    # Get the axis values (left/right, up/down for steering and throttle)
    x_axis = -joystick.get_axis(0)  # Left stick horizontal for steering
    y_axis = -joystick.get_axis(1)  # Left stick vertical for throttle
    
    # Get button inputs (use buttons for actions like forward, reverse, etc.)
    button_a = joystick.get_button(0)  # Button A for action
    
    # Process the inputs to control the robot's speed and steering
    steering_angle = x_axis  # Mapping steering input
    throttle = y_axis  # Mapping throttle input
    
    # Debug messages
    rospy.loginfo("Gamepad Input: Steering: %f, Throttle: %f", steering_angle, throttle)
    rospy.logdebug("Button A pressed: %d", button_a)
    
    # Create a Twist message
    twist_msg = Twist()
    twist_msg.linear.x = throttle  # Forward/backward motion
    twist_msg.angular.z = steering_angle  # Turning (steering)
    
    return twist_msg

# Main loop
while not rospy.is_shutdown():
    twist_msg = get_gamepad_input()
    
    # Publish the twist message to cmd_vel
    cmd_vel_pub.publish(twist_msg)
    
    # Log the published message
    rospy.loginfo("Published Twist Message: Linear.x: %f, Angular.z: %f", twist_msg.linear.x, twist_msg.angular.z)
    
    rate.sleep()

