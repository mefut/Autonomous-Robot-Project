#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool, SetBoolRequest

#node setup
rospy.init_node("client")

#define client and wait for the service
client = rospy.ServiceProxy("test_service", SetBool)
client.wait_for_service()

#create the response message
# Server active mi ya da server var mı diye kontrol etmem gerekiyor
request = SetBoolRequest()
request.data = True

#recieve the response and store it
response = client(request)

#Visualize
print(response)
