#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
#Depedency for turtlesim library is already there
from turtlesim.msg import Pose

class SubTurtlePosNode(Node):
    def __init__(self):
        super().__init__("Turtle_sub")
        #Subscribption needs a callback to when a message is received
        self.pose_subscriber = self.create_subscription(Pose,"/turtle1/pose", self.pose_callback, 10)
        self.get_logger().info("Sub node started")

    def pose_callback(self, msg: Pose):
        self.get_logger().info(str(msg))


def main(args=None):
    rclpy.init(args=args)
    node = SubTurtlePosNode()
    rclpy.spin(node)
    rclpy.shutdown()