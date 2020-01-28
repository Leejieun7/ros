#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

pub = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)
pub1 = Twist()

def gos():
		pub1.linear.x = 0.2
		pub1.angular.z = 0
		pub.publish(pub1)

def turn():
		pub1.linear.x = 0
		pub1.angular.z = 0.6
		pub.publish(pub1)

def stop():
		pub1.linear.x = 0
		pub1.angular.z = 0
		pub.publish(pub1)

def callback(data):
	for num_1 in data.ranges[1:101]:
		if num_1 > 0.02 and num_1 < 0.3:
			gos()

	for num_2 in data.ranges[101:201]:
		if num_2 > 0.02 and num_2 < 0.3:
			turn()

def main():
	rospy.init_node("Sensor_Publisher")
	rospy.Subscriber("/scan", LaserScan, callback)

	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		a = 1

	rate.sleep()

if __name__ == '__main__':
	try :
		main()
	except rospy.ROSInterruptException:
		pass



