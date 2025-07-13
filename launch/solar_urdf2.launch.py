from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    urdf_path = os.path.join(
        get_package_share_directory('solar_urdf2'),
        'urdf',
        'solar_urdf2.urdf')
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen'
    )

    node_joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    with open(urdf_path, 'r') as f:
        robot_desc = f.read()

    return LaunchDescription([
        # Relay Joint_states
       # Node(
      #      package='solar_joint_controller',
       #     executable='joint_relay',
      #      name='joint_relay',
       #     output='screen'
      #  ),

        # Pub robot_description TF
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}],
            output='screen'
        ),

        # RViz
        Node(
            package='rviz2',
            executable='rviz2',
            output='screen'
        ),
        node_robot_state_publisher,
        node_joint_state_publisher_gui
    ])

