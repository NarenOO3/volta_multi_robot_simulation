#!/usr/bin/env python3

import rospy
import tf2_ros
import geometry_msgs.msg

def main():
    rospy.init_node('tf_publisher_node')
    broadcaster = tf2_ros.TransformBroadcaster()

    rate = rospy.Rate(10)  # Adjust the rate as needed
    
    num_robots = 4  # Adjust the number of robots as needed

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        for i in range(1, num_robots + 1):
            # Define the transform from /roboti/odom to map (if using localization)
            map_trans = geometry_msgs.msg.TransformStamped()
            map_trans.header.stamp = current_time
            map_trans.header.frame_id = "map"  # Adjust frame_id as needed
            map_trans.child_frame_id = "/robot{}_tf/odom".format(i)
            map_trans.transform.translation.x = 0.0  # Adjust translation values as needed
            map_trans.transform.translation.y = 0.0
            map_trans.transform.translation.z = 0.0
            map_trans.transform.rotation.x = 0.0  # Adjust rotation values as needed
            map_trans.transform.rotation.y = 0.0
            map_trans.transform.rotation.z = 0.0
            map_trans.transform.rotation.w = 1.0

            # Publish the transform
            broadcaster.sendTransform(map_trans)

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
