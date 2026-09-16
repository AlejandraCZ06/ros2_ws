import sys
from tutorial_interfaces.srv import Hypotenuse
import rclpy
from rclpy.node import Node

class HypotenuseClient(Node):
    def __init__(self):
        super().__init__('hypotenuse_client')
        self.cli = self.create_client(Hypotenuse, 'calculate_hypotenuse')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando al servicio...')
        self.req = Hypotenuse.Request()

    def send_request(self, a, b):
        self.req.a = float(a)
        self.req.b = float(b)
        return self.cli.call_async(self.req)

def main():
    rclpy.init()
    client = HypotenuseClient()
    future = client.send_request(sys.argv[1], sys.argv[2])
    rclpy.spin_until_future_complete(client, future)
    response = future.result()
    client.get_logger().info(f'Resultado: Hipotenusa = {response.c}')
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
