#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    # Directories for launch files
    nikiro_gazebo_launch_dir = os.path.join(get_package_share_directory('conveyor_description'), 'launch')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # Launch configurations
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    x_pose = LaunchConfiguration('x_pose', default='0.0')
    y_pose = LaunchConfiguration('y_pose', default='0.0')

    # World file
    world = os.path.join(
        get_package_share_directory('conveyor_description'),
        'worlds',
        'env.world'
    )

    # Gazebo server command
    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    # Gazebo client command
    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    # Create the launch description
    ld = LaunchDescription()

    # Add actions to launch description
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)

    return ld

