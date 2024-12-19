#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64  # Correct message type

# Node + Topic initialization
rospy.init_node("publisher_node")
pub = rospy.Publisher("/onur", Int64, queue_size=1)
pub2 = rospy.Publisher("/sam", Int64, queue_size=1)

# Looping
while not rospy.is_shutdown():
    pub.publish(1)
    pub2.publish(2)
    rospy.sleep(1)
 
