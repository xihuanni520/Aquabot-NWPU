# Aquabot-NWPU
本项目结合人工智能与仿生学技术，设计一款具备自主导航、实时缺陷识别和高机动性的水下机器人，旨在降低检测成本、提升效率，并为水下装备智能化提供新范式。本项目通过“仿生结构+AI边缘计算+模块化能源”三位一体设计，推动水下检测从“人力密集型”向“智能无人化”转型，契合《“十四五”海洋经济发展规划》中“深海装备自主化”的战略目标。

依赖环境：
Ubuntu 18.04 + ROS Melodic
Python 3.6+, PyTorch 1.10+, OpenCV 4.5+

# 安装ROS Melodic  
sudo apt-get install ros-melodic-desktop-full  

# 安装PyTorch & TensorFlow  
pip3 install torch==1.10.0+cu113 torchvision==0.11.1+cu113 -f https://download.pytorch.org/whl/torch_stable.html  
pip3 install tensorflow==2.6.0  

# 克隆并编译代码（需自行创建仓库）  
mkdir -p ~/catkin_ws/src  
cd ~/catkin_ws/src  
git clone https://github.com/your_username/Underwater-Inspector.git  
cd ..  
catkin_make  


# 启动Gazebo水下环境  
roslaunch aquabot_gazebo underwater_world.launch  

# 运行视觉检测  
python3 defect_detection.py --source camera  

# 启动自主导航  
rosrun aquabot_navigation ddpg_navigation_node  



import matplotlib.pyplot as plt  
plt.bar(["传统ROV", "本作品"], [500, 350], color=["red", "green"])  
plt.ylabel("能耗 (W)")  
plt.savefig("power_consumption.png")  
