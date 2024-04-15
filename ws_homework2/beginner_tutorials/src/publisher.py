#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import numpy as np

def publisher():
    pub = rospy.Publisher("public_randint", Float32, queue_size=10)
    rospy.init_node("publisher", anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        seconds = rospy.get_time()
        random_number = np.sin(seconds) * np.random.randn()
        rospy.loginfo(f"{random_number}")
        pub.publish(random_number)
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass