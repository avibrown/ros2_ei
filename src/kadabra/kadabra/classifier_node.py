import os
import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32MultiArray
from edge_impulse_linux.runner import ImpulseRunner


class ClassificationNode(Node):
    def __init__(self):
        super().__init__("classifier")
        self.publisher_ = self.create_publisher(
            String, "classification_stream", 15)
        self.timer_ = self.create_timer(0.1, self.classify)

        self.classifier = Classifier('modelfile.eim')

        self.subscriber_ = self.create_subscription(Float32MultiArray, "mpu6050_stream", self.callback_fill_buffer, 15)
        self.buffer = []

        self.get_logger().info("Classification stream opened.")

    def classify(self):
        msg = String()
        if len(self.buffer) == 588:
            msg.data = self.classifier.classify(self.buffer)
            self.publisher_.publish(msg)
            self.buffer = []

    def callback_fill_buffer(self, msg):
        self.get_logger().info(f"Buffer length: {len(self.buffer)}")
        if len(self.buffer) < 588:
            for val in msg.data:
                self.buffer.append(val)


class Classifier:
    def __init__(self, model_path):
        self.runner = None
        self.model_path = model_path

    def signal_handler(self, sig, frame):
        if (self.runner):
            self.runner.stop()
        sys.exit(0)

    def help(self):
        print(f'{self.model_path}')

    def classify(self, features):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        modelfile = os.path.join(dir_path, self.model_path)

        self.runner = ImpulseRunner(modelfile)
        try:
            self.runner.init()
            res = self.runner.classify(features)
            return max(res["result"]["classification"], key=res["result"]["classification"].get)

        finally:
            if (self.runner):
                self.runner.stop()


def main(args=None):
    rclpy.init(args=args)
    node = ClassificationNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
