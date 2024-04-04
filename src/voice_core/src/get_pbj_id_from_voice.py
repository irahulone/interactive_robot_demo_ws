#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Int16

def talker():
    pub = rospy.Publisher('obj_id', Int16, queue_size=10)
    rospy.init_node('fake_obj_id_pub', anonymous=True)
    rate = rospy.Rate(4)
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        obj_id = 76
        pub.publish(obj_id)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
