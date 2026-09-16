import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('my_robot_launch')

    # Declarar un argumento principal configurable desde la terminal
    mi_arg = DeclareLaunchArgument(
        'input_namespace',
        default_value='robot_jerarquico',
        description='Namespace principal para la jerarquía de launch'
    )

    # Incluir el archivo launch secundario pasando el argumento
    include_subs = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'subs_events.launch.py')
        ),
        launch_arguments={'namespace_arg': LaunchConfiguration('input_namespace')}.items()
    )

    return LaunchDescription([
        mi_arg,
        include_subs
    ])
