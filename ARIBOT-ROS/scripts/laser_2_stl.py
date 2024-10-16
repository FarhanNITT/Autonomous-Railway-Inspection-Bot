#!/usr/bin/env python

import rospy
import numpy as np 
from sensor_msgs.msg import LaserScan
from gazebo_msgs.msg import ModelStates
from tf.transformations import euler_from_quaternion
from sensor_msgs.msg import PointCloud2
from laser_assembler.srv import *


class laser_scanner:
    """
        Class to input and convert laser scan data into stl file

        [x,y,z] --> Current position of the laser scanner
        theta --> Yaw angle of Inspection bot
        phi --> Sampling angles of the ray sensor
        d --> Distance of obstacle data from sensor
    """
    x = 0
    y = 0
    z = 0
    theta = 0

    data = np.array([[0,0,0]])
    samples = 50
    phi = np.reshape(np.linspace(-0.5,0.5,samples),[samples,1])

    def laser_callback(self,data):
        self.laser_data_processing(data.ranges)
        pass

    def pos_callback(self,data):
        index = 2
        self.x = data.pose[index].position.x
        self.y = data.pose[index].position.y
        self.z = data.pose[index].position.z

        x = data.pose[index].orientation.x
        y = data.pose[index].orientation.y
        z = data.pose[index].orientation.z
        w = data.pose[index].orientation.w
        [roll,pitch,yaw] = euler_from_quaternion([x,y,z,w])
        self.theta = yaw

    def __init__(self):
        print("Node Initialized .......")
        rospy.init_node('Laser_2_stl_node',anonymous=False)
        self.laser_sub = rospy.Subscriber('/Aribot/laser/scan',LaserScan,self.laser_callback)
        self.pos_sub   = rospy.Subscriber('/gazebo/model_states', ModelStates,self.pos_callback)
        self.pc_pub = rospy.Publisher("/point_cloud", PointCloud2,queue_size=100)
        self.pc_msg = PointCloud2()
        self.rate = rospy.Rate(0.5)
        while True:
            self.pc_msg.data = self.data.tolist()
            self.pc_pub.publish(self.pc_msg)
            self.rate.sleep()

    def laser_data_processing(self,d):
        d = np.reshape(d,[self.samples,1])
        del_x = (self.x + d*np.sin(self.phi)*np.cos(self.theta))
        del_y = (self.y + d*np.sin(self.phi)*np.sin(self.theta))
        del_z = (self.z - d*np.cos(self.phi))
        del_data = np.hstack([del_x,del_y,del_z])
        self.data = np.vstack([self.data,del_data])



if __name__ == '__main__':
    try:
        ls = laser_scanner()
        #data = np.asarray(ls.data)
        #np.save('rail_bot.npy',data)
        print('Size of data: ',np.shape(ls.data))
        print("Data saved ......")
    except rospy.ROSInterruptException:
        pass