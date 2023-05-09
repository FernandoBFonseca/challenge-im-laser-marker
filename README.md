# challenge-im-laser-marker
A laser pointer using a robot arm for modern construction sites . Project for the Imagine&Make Challenge at Centrale Lille (kind of a 1 week hackathon)

The challenge consisted in thinking of some application using robotic arms in the construction 4.0 scenario, my group thought of doing a laser pointer to help the site works to do services in walls (e.g do a hole or drill a outlet).

To do this, we used the Niryo Ned 2 Robot and RoboDK (with the python interface), the code have a setup process where the operator point to the four cornes of the wall, so we can calculate the relative position between the robot and the wall. After that, the robot points to the services at the wall (loaded in a .csv file) until the list of points has ended.

