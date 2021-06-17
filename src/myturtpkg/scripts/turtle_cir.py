#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

class turtlesim:
	def __init__(self):
		rospy.init_node('turtlebot_control', anonymous=True)
		self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
		self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.poseCallback)
		self.pose = Pose()
		
				
	def poseCallback(self, data):
    		self.pose.theta = round(data.theta,1)
		rospy.loginfo("theta = %f\n", self.pose.theta)
				
	def move(self):
    		vel_msg = Twist()
		vel_msg.linear.x = 2
        	vel_msg.angular.z = abs(2/2)
		rate = rospy.Rate(10)
		i = 0
		x = 3.10
		while not rospy.is_shutdown():
			self.velocity_publisher.publish(vel_msg)
			rate.sleep()
			if self.pose.theta == x:
				x = -0.0
				i = i + 1
				continue
			elif i == 2:
				break
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		self.velocity_publisher.publish(vel_msg)
		rospy.loginfo("complete")
		rate.sleep()

if __name__ == '__main__':
    try:
	x = turtlesim()
        x.move()

    except rospy.ROSInterruptException:
        pass

#source devel/setup.bash
# cd src/mypg/scripts
#chmod +x turtlebot_circles.py
#rosrun mypg turtlebot_circles.py
