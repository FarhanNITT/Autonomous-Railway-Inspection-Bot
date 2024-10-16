#!/usr/bin/env python

import rospy
import tf
from gazebo_msgs.msg import ModelStates


class tf_broadcast:

    def tf_callback(self,data):
        index = 2
        #print(data.pose[index])
        position = (data.pose[2].position.x,data.pose[2].position.y,data.pose[2].position.z)
        orientation = (data.pose[2].orientation.x,data.pose[2].orientation.y,data.pose[2].orientation.z,data.pose[2].orientation.w)
        self.tf_b.sendTransform(position,orientation,rospy.Time.now(),'base_link','world')

    def __init__(self):
        rospy.init_node('tf_broadcast')
        print("Node Initialized.........")
        self.tf_sub = rospy.Subscriber('/gazebo/model_states', ModelStates,self.tf_callback)
        self.tf_b = tf.TransformBroadcaster()
        rospy.spin()


if __name__ == '__main__':
    try:
        tf_bc = tf_broadcast()
    except rospy.ROSInterruptException():
        pass