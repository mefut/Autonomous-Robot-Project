 #!/usr/bin/env python3

#This script sets the robot's initial pose in a navigation system.

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped #PoseWithCovarianceStamped: Message type for defining the robot's initial pose along with its covariance.
from nav_msgs.msg import Odometry #Odometry: Message type for retrieving the robot's current pose from the /odom topic.

# Node initialization
rospy.init_node('init_pose')
pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 1)

# Construct message
init_msg = PoseWithCovarianceStamped()
init_msg.header.frame_id = "map"

# Get initial pose from Gazebo
odom_msg = rospy.wait_for_message('/odom', Odometry)
init_msg.pose.pose.position.x = odom_msg.pose.pose.position.x
init_msg.pose.pose.position.y = odom_msg.pose.pose.position.y
init_msg.pose.pose.orientation.x = odom_msg.pose.pose.orientation.x
init_msg.pose.pose.orientation.y = odom_msg.pose.pose.orientation.y
init_msg.pose.pose.orientation.z = odom_msg.pose.pose.orientation.z
init_msg.pose.pose.orientation.w = odom_msg.pose.pose.orientation.w

# Delay
rospy.sleep(1)

# Publish message
rospy.loginfo("setting initial pose")
pub.publish(init_msg)
rospy.loginfo("initial pose is set")
