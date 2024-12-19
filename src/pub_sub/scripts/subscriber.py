#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

def callback(msg):
	print(msg)

#Node + subscriber initialization
rospy.init_node("subscriber")
rospy.subscriber("topic", Int64, callback)
rospy.spin()
