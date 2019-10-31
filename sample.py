import Leap, sys, time, thread
from time import sleep
import pandas as pd
import numpy as np

def convertS2F(matrix):
    matrix = matrix[0]
    matrix = matrix.split(', ')
    matrix = [float(matrix[0][1:]),float(matrix[1][0:]),float(matrix[2][0:-1])]
    return matrix

def convert(matrix):
    matrix = matrix.split(', ')
    matrix = [float(matrix[0][1:]),float(matrix[1][0:]),float(matrix[2][0:-1])]
    return matrix

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']

    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print("Connected")

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print("Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):

        # Get the most recent frame and report some basic information
        frame = controller.frame()

        print("Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers)))

        # Get hands
        middle_result = []
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            print("  %s, id %d, position: %s" % (handType, hand.id, hand.palm_position))

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            # print("  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (direction.pitch * Leap.RAD_TO_DEG,normal.roll * Leap.RAD_TO_DEG,direction.yaw * Leap.RAD_TO_DEG))
            PYR = []
            PYR.append(direction.pitch * Leap.RAD_TO_DEG)
            PYR.append(normal.roll * Leap.RAD_TO_DEG)
            PYR.append(direction.yaw * Leap.RAD_TO_DEG)




            # Get arm bone
            arm = hand.arm
            C = []
            # print( "  wrist position: %s" % (arm.wrist_position))
            C.append(str(arm.wrist_position))
            C = convertS2F(C)


            middle_result = np.hstack((PYR,C))


            # df = pd.DataFrame([middle_result], columns=['pitch','roll','yaw','wrist_position_x','wrist_position_y','wrist_position_z'])
            # df.to_csv('./result.csv')

            # Get fingers
            middle_result_2 = []
            vector_list = []
            middle_result_3 = []
            for finger in hand.fingers:


                B = []

                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)

                    B.append(str(bone.prev_joint))
                    B.append(str(bone.next_joint))
                    B.append(str(bone.direction))

                list_1 = convert(B[0])
                list_2 = convert(B[-2])
                list_3 = convert(B[-1])
                middle_result_2.append(list_1)
                middle_result_2.append(list_2)
                middle_result_3.append(list_3)

            for i in range(0,9,2):

                vector = (((middle_result_2[i][0] - middle_result_2[i+1][0]) ** 2) + ((middle_result_2[i][1] - middle_result_2[i+1][1]) ** 2) + ((middle_result_2[i][2] - middle_result_2[i+1][2]) ** 2))
                vector = vector ** 0.5
                vector_list.append(vector)

            result = np.hstack((middle_result,vector_list))
            # df = pd.DataFrame([result], columns=['pitch','roll','yaw','wrist_position_x','wrist_position_y','wrist_position_z','1','2','3','4','5'])
            # df.to_csv('./result.csv')
            direction_list = []
            for i in range(0,5):
                for j in range(0,3):
                    direction_list.append(middle_result_3[i][j])
            result = np.hstack((result,direction_list))
            label = ['N3']
            result = np.hstack((result,label))
            print(result)

            df = pd.read_csv('./resultN.csv')
            new_df = pd.DataFrame([result], columns=['pitch','roll','yaw','wrist_position_x','wrist_position_y','wrist_position_z','Thumb_Vector',
                                                 'Index_Vector','Middle_Vector','Ring_Vector','Pinky_Vector','Thumb_x','Thumb_y','Thumb_z',
                                                 'Index_x','Index_y','Index_z','Middle_x','Middle_y','Middle_z','Ring_x','Ring_y',
                                                 'Ring_z','Pinky_x','Pinky_y','Pinky_z','label'])

            df.append(new_df)

            new_df.to_csv('./resultN.csv',index=False,header=False,mode='a')
            # new_df.to_csv('./result.csv',index=False)
            result = []


        if not frame.hands.is_empty:
            print("")

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)


    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")

    try:
        sys.stdin.readline()

    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)




if __name__ == "__main__":
    main()
