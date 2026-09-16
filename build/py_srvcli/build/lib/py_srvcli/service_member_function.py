import math
from tutorial_interfaces.srv import Hypotenuse
import rclpy
from rclpy.node import Node

class HypotenuseService(Node):
    def __init__(self):
        super().__init__('hypotenuse_service')
        self.srv = self.create_service(Hypotenuse, 'calculate_hypotenuse', self.calculate_callback)

    def calculate_callback(self, request, response):
        response.c = math.sqrt(request.a**2 + request.b**2)
        self.get_logger().info(f'Peticion recibida: a={request.a}, b={request.b} -> Hipotenusa={response.c}')
        return response

def main():
    rclpy.init()
    node = HypotenuseService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

