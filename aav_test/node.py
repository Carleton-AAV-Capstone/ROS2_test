#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

#Create our own node inheriting rclpy node class
class AavNode(Node):
    def __init__(self):
        #Node name is auto_node
        super().__init__("auto_node")
        self.counter = 0
        #Create a callback every second to timer_callback function
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter))
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    #Write main code here

    #Create first node
    node = AavNode()

    #Keep node alive until killed 
    rclpy.spin(node)

    
    #Shutdown ros2 communication
    rclpy.shutdown()


if __name__ == '__main__':
    main()