import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/alejandra/ros2_ws/install/turtlesim_control_pkg'
