#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
class turtle:
	def __init__(self):
		rospy.init_node('control_turtle', anonymous = True)
		self.vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 1)
		self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.posecallback)
		self.position = Pose()
		self.rate = rospy.Rate(10)

	def posecallback(self, pose_data):
		self.position.theta = round(pose_data.theta,2)


	def moveturtle(self):
		cmd_vel = Twist()
		cmd_vel.linear.x = 2.0
		cmd_vel.angular.z = 1.0
		while not rospy.is_shutdown():
			rospy.loginfo("pose .x = %f", self.position.theta)
			self.vel_pub.publish(cmd_vel)
			#if self.position.theta < 10.0:
			#break

			
if __name__ == '__main__':
    try:
	x = turtle()        
	x.moveturtle()
    except rospy.ROSInterruptException:
        pass
	

