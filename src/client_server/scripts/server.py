#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool, SetBoolResponse

def callback(req_msg):
    # Create response message
    response = SetBoolResponse()

    if req_msg.data:
        response.success = True  # Correct spelling of 'success'
        response.message = "The device was enabled"
    else:
        response.success = True  # Correct spelling of 'success'
        response.message = "The device was disabled"
        
    return response  # Service callbacks must return a response

# Node setup
rospy.init_node("server")
rospy.Service("test_service", SetBool, callback)
rospy.spin()

