#!/usr/bin/env python

import rospy
from laser_assembler.srv import AssembleScans2
from sensor_msgs.msg import PointCloud2

rospy.init_node('Laser_to_pc_node')
rospy.wait_for_service('assemble_scans2')
assemble_scans = rospy.ServiceProxy('assemble_scans2',AssembleScans2)
pub = rospy.Publisher('/laser_point_cloud', PointCloud2, queue_size=1)

while not rospy.is_shutdown():
    try:
        resp = assemble_scans(rospy.Time(0,0),rospy.get_rostime())
        pub.publish(resp.cloud)

    except rospy.ROSSerializationException():
        print("Operation failed.....")
