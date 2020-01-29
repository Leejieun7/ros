cmake_minimum_required(VERSION 2.8.3)
project(topic_simple)
# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  rospy
  message_generation
  std_msgs
)
 add_message_files(
   FILES
   sim.msg
 )

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES topic_simple
  CATKIN_DEPENDS rospy std_msgs
#  DEPENDS system_lib
)

