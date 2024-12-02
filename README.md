# Conveyor_simulation
**Custom Conveyor simulation for ROS2 humble**

This project is a simulation of a conveyor belt system, designed for use in robotic automation, industrial applications, and research purposes. The model includes features such as conveyor motion, sensors for object detection, and integration with ROS 2 and Gazebo classic.

**Overview**

This project is an improved version of the conveyor model developed by the IFRA (Intelligent Flexible Robotics and Assembly) Group, part of the Centre for Robotics and Assembly at Cranfield University. It integrates a realistic conveyor simulation into Gazebo and ROS 2 environments, supporting various research and industrial applications.

**Features**

Realistic Conveyor Motion: Simulates belt movement for transporting objects.
Sensor Integration: Includes IR sensors for object detection.
ROS 2 Support: Compatible with ROS 2 for easy integration with robotic systems.
Gazebo Integration: Fully functional in Gazebo for visualization and testing.
Interactive Object Spawner: Use the summoner.py script to spawn objects dynamically.

**Installation**
```sh
cd ~/colcon_ws/src
git clone https://github.com/IFRA-Cranfield/IFRA_ConveyorBelt.git
cd ~/dev_ws
colcon build
```


