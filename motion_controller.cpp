// aquabot_control/src/motion_controller.cpp
#include <ros/ros.h>
#include <geometry_msgs/Twist.h>

void controlCallback(const sensor_msgs::Imu::ConstPtr& imu_msg) {
    // 基于IMU数据调整姿态
    geometry_msgs::Twist cmd_vel;
    cmd_vel.angular.z = PID(imu_msg->angular_velocity.z);
    pub.publish(cmd_vel);
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "motion_controller");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("imu/data", 10, controlCallback);
    ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("cmd_vel", 10);
    ros::spin();
    return 0;
}