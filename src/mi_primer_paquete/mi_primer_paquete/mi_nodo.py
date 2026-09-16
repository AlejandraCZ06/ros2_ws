import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ControlTurtlesim(Node):
    def __init__(self):
        super().__init__('nodo_control_tortuga')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.mover_tortuga)

    def mover_tortuga(self):
        msg = Twist()
        msg.linear.x = 1.5
        msg.angular.z = 1.0
        self.publisher_.publish(msg)
        self.get_logger().info('Publicando comando de movimiento...')

def main(args=None):
    rclpy.init(args=args)
    nodo = ControlTurtlesim()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
