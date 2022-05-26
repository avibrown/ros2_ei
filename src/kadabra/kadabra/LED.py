#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import RPi.GPIO as GPIO
 
class LED(Node):
    def __init__(self):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(37, GPIO.OUT)

        super().__init__("LED")
        self.subscriber_ = self.create_subscription(Bool, "trigger_stream", self.callback_toggle_LED, 15)
        self.get_logger().info("LED toggler opened.")

    def callback_toggle_LED(self, msg):
        GPIO.output(37, msg.data)
 
 
def main(args=None):
    rclpy.init(args=args)
    node = LED()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()