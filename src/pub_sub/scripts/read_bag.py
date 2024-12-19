#!/usr/bin/env python3

import rospy
import rosbag       

rospy.init_node("read_bag")
bag = rosbag.Bag("/home/onur/catkin_ws/src/pub_sub/bag/test.bag")

for topic, msg,t in bag.read_messages(topics = ["/onur", "/sam"]):
	if topic == "/onur":
		print("Onur's data is: ")
		print(msg.data)
		print("and it was recorded at:")
		print(t)
		
	if topic == "/sam":
		print("Sam's data is: ")
		print(msg.data)
		print("and it was recorded at:")
		print(t)
		
		
