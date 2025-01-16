<p align="center">
  <img src="images/itu-eef-white.png" width="600" title="İTÜ Kontrol ve Otomasyon Mühendisliği">
</p>

# KON-414E Final Project
This repository contains ROS Packages about Final Project of the **KON414E** *"Principles of Robot Autonomy"* Course 
given at **Istanbul Technical University** in the fall term of 2024/2025.
<br>

## Objective: 3D Mapping of the Environment
### Robot
AgileX HUNTER 2.0

### Sensors
<ol>
    <li>3D LIDAR</li>
        <ul>
            <li>360° horizontal and 30° vertical FOV</li>
            <li>0.5° horizontal and vertical resolution</li>
            <li>20m range</li>
            <li>10Hz refresh rate</li>
        </ul>
    <li>RTK-GPS</li>
        <ul>
            <li>+/-2cm precision</li>
        </ul>
</ol>

### Project Description
<ol>
  <li>Point Cloud Map generation for the Gazebo environment (Clearpath Robotics Inspection World) using 
RTAB Mapping</li>
  <li> Odometry source will be RTK-GPS + Wheel odometry of the vehicle (fusing withrobot_localization package)</li>
  <li>Converting point cloud map into octomaps with different resolutions and evaluate resolution effects on 
environment representation</li>
  <li>Check map resolution effect on autonomous navigation/li>
</ol>

## Installation
<ol>
    <li>Clone the repository to your workspace's src directory.</li>
    <li>Go to parent directory.</li>
    <li>Build workspace.</li>
</ol>

```
cd your_workspace/src
git clone "repository link"
cd ..
catkin_make
```