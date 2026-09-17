import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory("dif_bot_description")
    
    # 1. Archivo del mundo
    world_file = LaunchConfiguration("world", default=os.path.join(pkg_share, "worlds", "my_world.sdf"))
    
    # 2. Descripción del robot (Xacro)
    robot_xacro = os.path.join(pkg_share, "urdf", "robot_gz.urdf.xacro")
    robot_description = Command(["xacro ", robot_xacro])
    
    # 3. Robot State Publisher (usa tiempo de simulación)
    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{
            "robot_description": ParameterValue(robot_description, value_type=str),
            "use_sim_time": True
        }]
    )
    
    # 4. Lanzar Gazebo Sim
    gz_sim_share = get_package_share_directory("ros_gz_sim")
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(gz_sim_share, "launch", "gz_sim.launch.py")),
        launch_arguments={"gz_args": world_file}.items()
    )
    
    # 5. Hacer spawn del robot en Gazebo
    spawn = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-topic", "/robot_description",
            "-name", "dif_bot",
            "-z", "0.2" # Elevar 20cm para evitar colisión inicial con el suelo
        ],
        output="screen"
    )
    
    # 6. ROS-GZ Bridge
    # Sintaxis: /ROS_TOPIC@ROS_MSG_TYPE[DIRECCION]GZ_MSG_TYPE
    # [ = Gazebo a ROS, ] = ROS a Gazebo, @ = Bidireccional
    bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        parameters=[{"use_sim_time": True}],
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock",
            "/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist",
            "/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry",
            "/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model",
            "/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V",
            "/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan",
            "/imu@sensor_msgs/msg/Imu[gz.msgs.IMU"
        ],
        output="screen"
    )

    return LaunchDescription([
        DeclareLaunchArgument("world", default_value=world_file, description="World SDF file"),
        rsp,
        gz_sim,
        TimerAction(period=3.0, actions=[spawn]), # Delay de 3s para que Gazebo cargue antes del spawn
        bridge
    ])
