# ARIBOT
Autonomous Railway Inspection Robot built as a part of Ministry of Education's Innovation cell, Government of India.
Project Report and Results can be found here [ARIBOT](https://sites.google.com/view/farhanseliyarobotics/experience/aribot?authuser=0)

## Abstract

Regular maintenance and inspection are crucial for the effective and safe usage of railways as a mode of transportation. Any form of cracks or defects in railway tracks can lead to track failures causing catastrophic damage. In India, most railway track inspections are conducted manually by railroad track inspectors. It is practically difficult to manually look for defects along long stretches of railway tracks, making it inaccurate due to human errors. Deploying an autonomous robot that can check the railway lines for defects will reduce human effort and error.

We propose a prototype that is a fully autonomous 4-wheeled robot, flexible in usage and installation, capable of detecting railway defects by performing various tests such as ultrasonic Nondestructive Test (NDT) for internal crack detection in rails and a 3D-laser profiling system for surface cracks, gauge length, and ballast profile inspection. The robot is also equipped with a machine vision system (camera) for anomaly detection in fasters and sleepers. Once inspection mode is turned on, our proposed system will autonomously inspect the track for defects, mainly in 4 profiles: Ballast, Rails, Sleepers, and Fasteners, checking for deviation from a standard profile by implementing the aforementioned methods.

The bot is equipped with modules like GPS, odometer, and IMU sensors to locate and know the robot's position and status respectively at any given time. All the inspection data, including ongoing data capture and defect location details, are constantly being sent and updated to a user-friendly web server. These details can be accessed by Inspection personnel for robot activity monitoring, such as distance traveled, battery charge with rough inspection duration estimate, the temperature of on-board modules, and mainly, Inspection result analysis such as live camera feed from a camera installed, laser profile of track, and other inspection data. If any defect or anomaly is detected, the nearby base station is alerted in the webserver mentioned, and the Spatio-temporal coordinates, that is, time and location of defect and type of defect, are shared.

## Framework and Simulation Version

● Simulation and Test integration: *ROS, Gazebo11*

● Design Analysis: *SolidWorks 2022, Ansys*

● Point Cloud Processing: *MATLAB 2021*

● Fault Detection: *Pandas, Tensor Flow, OpenCV2*

● Communication: *NGINX, GSM*

## Packages Required (*for launch)*

```bash
pip3 install scikit-image
pip3 install opencv-contrib-python
pip3 install python3-numpy
pip3 install libboost-python-dev
```

## **Build and Launch instructions**

*ARIBOT_ROS package only*

```bash
cd ~/<your_ws>/src
git clone <repo URL>
cd ~/<your_ws>
catkin_make
Roslaunch aribot gazebo.launch
```
