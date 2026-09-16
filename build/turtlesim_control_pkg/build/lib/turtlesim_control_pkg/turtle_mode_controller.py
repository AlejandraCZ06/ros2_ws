import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Trigger

class TurtleModeController(Node):
    def __init__(self):
        super().__init__('turtle_mode_controller')
        
        # Publicador a la tortuga
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # Suscriptor a la posición
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_cb, 10)
        
        # Servicios para cambiar y consultar modo
        self.srv_get_mode = self.create_service(Trigger, '/get_mode', self.get_mode_cb)
        self.srv_set_manual = self.create_service(Trigger, '/set_mode_manual', self.set_manual_cb)
        self.srv_set_circles_cw = self.create_service(Trigger, '/set_mode_circles_cw', self.set_circles_cw_cb)
        self.srv_set_circles_ccw = self.create_service(Trigger, '/set_mode_circles_ccw', self.set_circles_ccw_cb)
        self.srv_set_trajectory = self.create_service(Trigger, '/set_mode_trajectory', self.set_trajectory_cb)
        
        # Estado actual: MANUAL, CIRCLES_CW, CIRCLES_CCW, TRAJECTORY
        self.current_mode = "MANUAL"
        self.current_pose = None
        
        # Trayectoria autónoma: 3 puntos (x, y)
        self.waypoints = [(2.0, 2.0), (8.0, 2.0), (5.5, 8.5)]
        self.target_idx = 0
        
        # Bucle de control a 10 Hz
        self.timer = self.create_timer(0.1, self.control_loop)
        self.get_logger().info("Nodo Controlador de Modos iniciado en modo MANUAL.")

    def pose_cb(self, msg):
        self.current_pose = msg

    def set_manual_cb(self, request, response):
        self.current_mode = "MANUAL"
        response.success = True
        response.message = "Modo cambiado a: MANUAL"
        self.get_logger().info(response.message)
        return response

    def set_circles_cw_cb(self, request, response):
        self.current_mode = "CIRCLES_CW"
        response.success = True
        response.message = "Modo cambiado a: CIRCLES_CW (Horario)"
        self.get_logger().info(response.message)
        return response

    def set_circles_ccw_cb(self, request, response):
        self.current_mode = "CIRCLES_CCW"
        response.success = True
        response.message = "Modo cambiado a: CIRCLES_CCW (Anti-Horario)"
        self.get_logger().info(response.message)
        return response

    def set_trajectory_cb(self, request, response):
        self.current_mode = "TRAJECTORY"
        self.target_idx = 0
        response.success = True
        response.message = "Modo cambiado a: TRAJECTORY (3 Puntos)"
        self.get_logger().info(response.message)
        return response

    def get_mode_cb(self, request, response):
        response.success = True
        response.message = f"Modo activo actual: {self.current_mode}"
        return response

    def control_loop(self):
        cmd = Twist()
        
        if self.current_mode == "MANUAL":
            return

        elif self.current_mode == "CIRCLES_CW":
            cmd.linear.x = 2.0
            cmd.angular.z = -1.5
            self.cmd_pub.publish(cmd)

        elif self.current_mode == "CIRCLES_CCW":
            cmd.linear.x = 2.0
            cmd.angular.z = 1.5
            self.cmd_pub.publish(cmd)

        elif self.current_mode == "TRAJECTORY":
            if self.current_pose is None:
                return

            if self.target_idx < len(self.waypoints):
                gx, gy = self.waypoints[self.target_idx]
                dx = gx - self.current_pose.x
                dy = gy - self.current_pose.y
                dist = math.hypot(dx, dy)

                if dist < 0.2:
                    self.get_logger().info(f"Punto {self.target_idx + 1} alcanzado ({gx}, {gy}).")
                    self.target_idx += 1
                    if self.target_idx >= len(self.waypoints):
                        self.get_logger().info("Trayectoria completada. Pasando a modo MANUAL.")
                        self.current_mode = "MANUAL"
                        self.cmd_pub.publish(Twist())
                        return

                target_angle = math.atan2(dy, dx)
                angle_diff = math.atan2(math.sin(target_angle - self.current_pose.theta),
                                        math.cos(target_angle - self.current_pose.theta))

                cmd.linear.x = min(1.5, 1.0 * dist)
                cmd.angular.z = 2.5 * angle_diff
                self.cmd_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleModeController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
