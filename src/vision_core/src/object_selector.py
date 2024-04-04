#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import Int16

global pos_x, pos_y, obj_selection
pos_x = 0
pos_y = 0
obj_selection = 0

#enter Class_ID 45 for bottle 
#program will keep on checking when z is equal to 45 
#if object 45 is there then print its centroid (x,y)

def obj_callback(data):
    global pos_x, pos_y, obj_selection
    pos_x = data.x
    pos_y = data.y
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #print(" ")
    #print(detection.Center[0]) #Centroid X Coordinate
    #print(detection.Center[1]) #Centroid Y Coordinate 
    #print(data.z) #Object_ID 

    #for detection in detections:
        #pos_x = detection.Center[0]
        #pos_y = detection.Center[1]
    #    obj_selection = 45
        
		#if detection.ClassID + 1 == obj_selection:
        #    print(f'{pos_x,pos_y}')

    if data.z  == obj_selection:
        print(f'{pos_x,pos_y}')
		 
def obj_id_callback(data):
    global obj_selection
    obj_selection = data.data

    print(obj_selection)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('object_selector', anonymous=True)

    rospy.Subscriber("object_def", Point, obj_callback)
    rospy.Subscriber("obj_id", Int16, obj_id_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
