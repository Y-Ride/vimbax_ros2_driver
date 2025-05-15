# Copyright (c) 2024 Allied Vision Technologies GmbH. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the Allied Vision Technologies GmbH nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os


def generate_launch_description():
    # Get directory where this launch file is located
    this_dir = os.path.dirname(os.path.realpath(__file__))
    default_settings_path = os.path.join(this_dir, '..', 'config', 'settings', 'stereo_ptp_auto_bayerRG8.xml')

    settings_file_arg = DeclareLaunchArgument(
        'settings_file_path',
        default_value=default_settings_path,
        description='Path to the camera settings XML file'
    )

    settings_file_path = LaunchConfiguration('settings_file_path')

    return LaunchDescription([
        SetEnvironmentVariable('RCUTILS_COLORIZED_OUTPUT', '1'),
        settings_file_arg,

        Node(
            package='vimbax_camera',
            namespace='camera_fr',
            executable='vimbax_camera_node',
            name='front_right',
            parameters=[{
                # "camera_id": "00:0f:31:00:0e:2f"
                # "camera_id": "00:0F-31-00-0E-2F"
                "camera_id": "192.168.68.60",
                # "camera_id": "DEV_000F31000E2F"
                "settings_file": settings_file_path,
            }]
        ),

        # Node(
        #     package='vimbax_camera',
        #     namespace='camera_fl',
        #     executable='vimbax_camera_node',
        #     name='front_left',
        #     parameters=[{
        #         # "camera_id": "00:0f:31:00:0e:2f"
        #         # "camera_id": "00:0F-31-00-0E-2F"
        #         "camera_id": "192.168.68.61"
        #         # "camera_id": "DEV_000F31000E2F"
        #     }]
        # )
    ])
