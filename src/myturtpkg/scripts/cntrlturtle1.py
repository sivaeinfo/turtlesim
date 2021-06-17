#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
position = Pose()
def posecallback(pose_data):

		position.x = round(pose_data.x,2)
		rospy.loginfo("position in x axis %f ", position.x)
def moveturtle():
		rospy.init_node('control_turtle', anonymous = True)
		vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 1)
		pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, posecallback)
		cmd_vel = Twist()
		rate = rospy.Rate(10)
		cmd_vel.linear.x = 1.0
		while position.x < 10.5:
			vel_pub.publish(cmd_vel)
			rate.sleep()
		cmd_vel.linear.x = 0.0
		vel_pub.publish(cmd_vel)
			
if __name__ == '__main__':
    try:
	moveturtle()
    except rospy.ROSInterruptException:
        pass
	

