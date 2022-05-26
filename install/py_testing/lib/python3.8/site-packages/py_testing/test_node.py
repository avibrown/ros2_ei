#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 
 
class TestNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("py_test_node") # MODIFY NAME
        self.get_logger().info("ROS2 testing...")
 
def main(args=None):
    rclpy.init(args=args)
    node = TestNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
