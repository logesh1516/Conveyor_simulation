# Conveyor_simulation
**Custom Conveyor simulation for ROS2 humble**

This project is a simulation of a conveyor belt system, designed for use in robotic automation, industrial applications, and research purposes. The model includes features such as conveyor motion, sensors for object detection, and integration with ROS 2 and Gazebo classic.

**OVERVIEW**

This project is an improved version of the conveyor model developed by the IFRA (Intelligent Flexible Robotics and Assembly) Group, part of the Centre for Robotics and Assembly at Cranfield University. It integrates a realistic conveyor simulation into Gazebo and ROS 2 environments, supporting various research and industrial applications.

**FEATURES**

Realistic Conveyor Motion: Simulates belt movement for transporting objects.
Sensor Integration: Includes IR sensors for object detection.
ROS 2 Support: Compatible with ROS 2 for easy integration with robotic systems.
Gazebo Integration: Fully functional in Gazebo for visualization and testing.
Interactive Object Spawner: Use the summoner.py script to spawn objects dynamically.

**INSTALLATION**
```sh
cd ~/colcon_ws/src
git clone https://github.com/logesh1516/Conveyor_simulation.git
cd ~/colcon_ws
colcon build
```
**SIMULATION**

**Basic simulation**

```sh
cd ~/colcon_ws
source install/setup.bash
ros2 launch conveyor_description conveyor_model.launch.py 
```
Spawning Objects over the Conveyor

a) Single object

```sh
cd ~/colcon_ws
source install/setup.bash
ros2 run ros2_conveyorbelt SpawnObject.py --package "conveyor_description" --urdf "redcube.urdf" --name "redcube" --x -0.2 --y 0 --z 1
(or)
ros2 run ros2_conveyorbelt SpawnObject.py --package "conveyor_description" --urdf "bluecube.urdf" --name "bluecube" --x -0.2 --y 0 --z 1
(or)
ros2 run ros2_conveyorbelt SpawnObject.py --package "conveyor_description" --urdf "greencube.urdf" --name "greencube" --x -0.2 --y 0 --z 1
```
through this command only red,green and bluecubes can be spawned.

b) Multiple Object

I have created a python script to spawn multiple objects over the conveyor.

Each object can be spawned only once.

```sh
cd ~/colcon_ws/src/Conveyor_simulation/ros2_conveyorbelt/python
source install/setup.bash
python3 summoner.py
```
**Simulation of the conveyor**

a) Manual power input

Activate the ConveyorBelt with the desired speed -> Value = (0,100]:

```sh
cd ~/colcon_ws
source install/setup.bash
ros2 service call /CONVEYORPOWER conveyorbelt_msgs/srv/ConveyorBeltControl "{power: --}"

```
b) Conveyor Automation using Ir sensors

Two IR sensors are placed in the start and end position of the conveyor for the automation depending on the presence of the object.

```sh
cd ~/colcon_ws
source install/setup.bash
ros2 run conveyor_automation conveyor_automation_node
```

**REFERENCE**

- (https://github.com/IFRA-Cranfield/IFRA_ConveyorBelt.git): My repo is based on this Repo and i took reference from it.

  
- [usnistgov/ARIAC](https://github.com/usnistgov/ARIAC): Reference of how a ConveyorBelt can be simulated with a ROS2 Plugin has been taken from the "ariac2023" branch of this repository, and adapted for the IFRA ROS2 Robot Simulation in Gazebo.


- [rokokoo/gconveyor-demo](https://github.com/rokokoo/conveyor_demo): The CAD file (mesh) of the ConveyorBelt used in our demo has been taken from this repository.



