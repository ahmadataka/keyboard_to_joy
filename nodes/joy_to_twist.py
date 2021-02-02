#!/usr/bin/env python
import roslib
roslib.load_manifest('keyboard_to_joy')
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class keyboard_joy(object):
  def __init__(self):
    rospy.init_node('joy_to_twist')
    self.key_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    key_sub = rospy.Subscriber('keyboard_msg', Joy, self.get_key)
    rate = rospy.Rate(40.0)
    self.twist_sent = Twist()
    while not rospy.is_shutdown():
    	rate.sleep()

  def get_key(self,msg):
    self.twist_sent.linear.x = msg.axes[1]
    self.twist_sent.angular.z = msg.axes[0]
    self.key_pub.publish(self.twist_sent)

if __name__ == '__main__':
    try:
        keyboard_joy()
    except rospy.ROSInterruptException: pass
