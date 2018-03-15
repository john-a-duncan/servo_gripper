#!/usr/bin/env python

import rospy
import numpy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import UInt16

open_angle = 20
close_angle = 109

def callback(data):
	pinch = "Pinch strength is %s" % data.data
	rospy.loginfo(pinch)
	
	desired_angle = int(open_angle + (close_angle-open_angle)*(data.data))
	desired = "Desired angle is %s" % desired_angle
	rospy.loginfo(desired)
	
	pub = rospy.Publisher('servo', UInt16, queue_size=10)
	pub.publish(desired_angle)

def listener_talker():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    #pub = rospy.Publisher('servo', std_msgs.msg.UInt16, queue_size=10)
    #pub = rospy.Publisher('servo', String, queue_size=10)
    
    rospy.init_node('servo_gripper_node', anonymous=True)
    rospy.Subscriber("leap_motion_output/right_hand/pinch_strength", Float32, callback)
    
    #rate = rospy.Rate(10) # 10hz

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    
    #while not rospy.is_shutdown():
    #	pub_str = "hello world %s" % data
    #	rospy.loginfo(pub_str)
    #	pub.publish(pub_str)
    #	rate.sleep()
    
    
if __name__ == '__main__':
	
    try:
        listener_talker()
    except rospy.ROSInterruptException:
        pass