from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='scanner', default_value='scanner',
            description='Namespace for sample topics'
        ),
        
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=['0', '0', '0', '1.57', '-1.57', '0.0', 'camera_depth_optical_frame', 'map']
        ),
        # Node(
        #     package='pointcloud_to_laserscan', executable='dummy_pointcloud_publisher',
        #     remappings=[('cloud', [LaunchConfiguration(variable_name='scanner'), '/cloud'])],
        #     parameters=[{'cloud_frame_id': 'cloud', 'cloud_extent': 15.0, 'cloud_size': 50000}],
        #     name='cloud_publisher'
        # ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     name='static_transform_publisher',
        #     arguments=['0', '0', '0', '0', '0', '0', '1', 'map', 'cloud']
        # ),
        # Node(
        #     package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
        #     remappings=[('cloud_in', [LaunchConfiguration(variable_name='scanner'), '/cloud']),
        #                 ('scan', [LaunchConfiguration(variable_name='scanner'), '/scan'])],
        #     parameters=[{
        #         'target_frame': 'cloud',
        #         'transform_tolerance': 0.01,
        #         'min_height': 0.0,
        #         'max_height': 10.0,
        #         'angle_min': -1.57,  # -M_PI/2
        #         'angle_max': 1.57,  # M_PI/2
        #         'angle_increment': 0.0087,  # M_PI/360.0
        #         'scan_time': 0.3333,
        #         'range_min': 0.45,
        #         'range_max': 5.0,
        #         'use_inf': True,
        #         'inf_epsilon': 1.0
        #     }],
        #     name='pointcloud_to_laserscan'
        # )
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('cloud_in', '/camera/depth/color/points'),
                        ('scan', '/scan_pointcloud')],
            parameters=[{
                'target_frame': 'map',
                'transform_tolerance': 0.010,
                'min_height': 0.1,
                'max_height': 2.0,
                'angle_min': -1.57,  # -M_PI/2
                'angle_max': 1.57,  # M_PI/2
                'angle_increment': 0.008,  # M_PI/360.0
                'scan_time': 0.333,
                'range_min': 0.45,
                'range_max': 10.0,
                'use_inf': True,
                'inf_epsilon': 100.0
            }],
            name='pointcloud_to_laserscan'
        )
        
    ])
