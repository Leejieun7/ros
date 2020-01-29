#!/usr/bin/env python

import rospy
from topic_simple.msg import sim

class Pub:
	def __init__(self):
		self.numpub = rospy.Publisher("pub_msg",sim,queue_size=10)
		self.a = 1.0
	



def main():
	tur = Pub()
	rospy.init_node("Sensor_Publisher")
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		tur.a += 0.5
		tur.numpub.publish(tur.a)
		rospy.loginfo(sim)
		print(tur.a)

	rate.sleep()

if __name__ == '__main__':
	try :
		main()
	except rospy.ROSInterruptException:
		pass


