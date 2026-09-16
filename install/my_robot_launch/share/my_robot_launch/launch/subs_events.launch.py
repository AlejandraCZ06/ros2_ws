from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Declarar el argumento que se pasará desde el archivo principal
    namespace_arg = DeclareLaunchArgument(
        'namespace_arg',
        default_value='default_namespace',
        description='Namespace recibido para el nodo turtlesim'
    )

    # Configuración del argumento
    ns_config = LaunchConfiguration('namespace_arg')

    # Nodo turtlesim que usa el namespace dinámico
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        namespace=ns_config,
        name='sim'
    )

    # Registro de eventos para mostrar el cambio de parámetros en consola
    print_launch_info = LogInfo(msg=['Iniciando turtlesim con el namespace: ', ns_config])

    return LaunchDescription([
        namespace_arg,
        print_launch_info,
        turtlesim_node
    ])
