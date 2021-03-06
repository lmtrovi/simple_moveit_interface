#!/usr/bin/env python

## @package simple_moveit_interface
#  Demo script using the simple_moveit_interface

## @file
#  Demo ROS node

## @author Clemens Schuwerk
#  clemens.schuwerk@tum.de

import sys
import rospy
import moveit_commander
from geometry_msgs.msg import Pose,Point
from sensor_msgs.msg import JointState
from simple_moveit_interface.moveit_interface import moveit_interface, moveit_interface_config
import copy
from math import pi

def shutdown_hook():
  print("Shutting down...")

  print("... DONE")




if __name__ == '__main__':
    try:

        # Init the ROS node
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('demo', anonymous=False)

        cfg = moveit_interface_config()
        moveit_if = moveit_interface(cfg)

        #moveit_if.init_planning_scene()

        moveit_if.move_fixed_pose("home")

        # Testing movements: fixed pose
        # moveit_if.move_fixed_pose("up")
        # moveit_if.move_fixed_pose("home")

        # up/down
        #moveit_if.move_z(0.2)
        #moveit_if.move_z(-0.1)
        #moveit_if.move_fixed_pose("home")

        # Pose
        pose = Pose()
        pose.position.x = 0.452285850112
        pose.position.y = 0.193954170998
        pose.position.z = 0.257895357846
        pose.orientation.x = -0.707667889402
        pose.orientation.y = -0.706531871778
        pose.orientation.z = -0.00210449161745
        pose.orientation.w = 0.00380047190555
        moveit_if.move_pose(pose)

        moveit_if.move_fixed_pose("home", True)

        # Joint state
        #js = JointState()
        #js.position = [0, -pi/3, pi/4, pi/4, pi/2, 0.0]
        #print js.position
        #moveit_if.move_joint_state(js)

        # Relative movements
        #moveit_if.move_z(0.2)
        #moveit_if.move_y(-0.2)
        #moveit_if.move_x(-0.2)

        #moveit_if.rotate_x(0.1)
        #moveit_if.rotate_y(0.1)
        #moveit_if.rotate_z(0.1)

#        # Cartesian path
#        moveit_if.move_fixed_pose("up")
#        pose = Pose()
#        pose.position.x = 0.552285850112
#        pose.position.y = 0.193954170998
#        pose.position.z = 0.357895357846
#        pose.orientation.x = -0.707667889402
#        pose.orientation.y = -0.706531871778
#        pose.orientation.z = -0.00210449161745
#        pose.orientation.w = 0.00380047190555
#        moveit_if.move_cartesian_path_to_pose(pose)


        rospy.on_shutdown(shutdown_hook)

        rospy.spin()


    except rospy.ROSInterruptException:
        pass
