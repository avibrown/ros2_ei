#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import RPi.GPIO as GPIO



class Trigger(Node):
    def __init__(self):
        super().__init__("trigger")

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.publisher_ = self.create_publisher(Bool, "trigger_stream", 15)
        self.timer_ = self.create_timer(0.05, self.read_trigger)
        self.get_logger().info("Trigger stream opened.")

    def read_trigger(self):
        msg = Bool()
        msg.data = bool(GPIO.input(40))
        self.publisher_.publish(msg)

 
def main(args=None):
    rclpy.init(args=args)
    node = Trigger()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
