#!/usr/bin/env python

import rospy
import scipy
import numpy as np 
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2

def pc_defect_callback(data):
    data = point_cloud2.read_points(data,field_names = ("x", "y", "z"))
    print(list(data))


rospy.init_node('pc_defect_detect_node')
rate = rospy.Rate(10)

sub = rospy.Subscriber('/laser_point_cloud', PointCloud2, pc_defect_callback)
rospy.spin()