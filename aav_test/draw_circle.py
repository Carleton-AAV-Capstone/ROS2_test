#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
#Dependency for this library must be added in xml file
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):

    def __init__(self):
        #Node name
        super().__init__("draw_cicle")
        #Publisher, with type of message, the topic, queue size
        self.cmd_vel_pub = self.create_publisher(Twist, "test_topic", 10)
        self.timer = self.create_timer(0.5, self.send_velocity_command)
        self.get_logger().info("Draw node started")

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()