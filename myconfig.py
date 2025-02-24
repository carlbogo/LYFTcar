MM1_STEERING_MID = 1550
#MM1_STEERING_MID = 1600
MM1_MAX_FORWARD = 1620  # Max is 2000
MM1_MAX_REVERSE = 1350
MM1_STOPPED_PWM = 1500
MM1_SHOW_STEERING_VALUE = False
MM1_SERIAL_PORT = '/dev/ttyS0'

THROTTLE_FORWARD_PWM = 430      #pwm value for max forward throttle
THROTTLE_STOPPED_PWM = 370      #pwm value for no movement
THROTTLE_REVERSE_PWM = 320      #pwm value for max reverse throttle

DRIVE_TRAIN_TYPE = "MM1"

JOYSTICK_MAX_THROTTLE = 1.0
JOYSTICK_THROTTLE_DIR = -1.0

CONTROLLER_TYPE='F710'           #(ps3|ps4)
DRIVE_LOOP_HZ = 20

if (CONTROLLER_TYPE=='F710'):
    JOYSTICK_DEADZONE = 0.1

AUTO_CREATE_NEW_TUB = True
#TRANSFORMATIONS = ["BLUR"]
#BLUR_KERNEL = 101        # blur kernel horizontal size in pixels
#BLUR_KERNEL_Y = None   # blur kernel vertical size in pixels or None for square kernel
#BLUR_GAUSSIAN = True   # blur is gaussian if True, simple if False
