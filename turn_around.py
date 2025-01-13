#Implmentation to the manage.py file

#from donkeycar.parts.tight_turn import TightTurn
#tight_turn = TurnAround(pivot_duration=1.5, reverse_duration=1.0)
#V.add(tight_turn, inputs=['user/throttle', 'user/steering'], outputs=['throttle', 'steering'])


import time

class TurnAround:
    def __init__(self, pivot_duration=1.5, reverse_duration=1.0, forward_throttle=0.85, reverse_throttle=-0.85, pivot_count=3):
        """
        Initialize the TightTurn part.

        Args:
            pivot_duration (float): Time (in seconds) for the pivot (turning in place).
            reverse_duration (float): Time (in seconds) for reversing in a straight line.
            forward_throttle (float): Throttle value for forward movement.
            reverse_throttle (float): Throttle value for reverse movement.
            pivot_count (int): Number of pivot cycles to complete a tight turn.
        """
        self.pivot_duration = pivot_duration
        self.reverse_duration = reverse_duration
        self.forward_throttle = forward_throttle
        self.reverse_throttle = reverse_throttle
        self.pivot_count = pivot_count
        self.state = "reverse"  # Initial state
        self.start_time = None
        self.current_pivot = 0
        self.enabled = False

    def launch(self):
        print('turnAround launched!')
        self.enabled = not self.enabled

    def run(self, throttle, steering):
        """
        Generate throttle and steering values for tight turnaround.

        Args:
            throttle (float): Current throttle input (ignored in this part).
            steering (float): Current steering input (ignored in this part).

        Returns:
            tuple: (throttle, steering) values to control the car.
        """
        if not self.enabled:
            return throttle, steering
        
        print('turnAround - start')

        current_time = time.time()

        # Start timing for the first state
        if self.start_time is None:
            self.start_time = current_time

        # Reverse straight
        if self.state == "reverse":
            if current_time - self.start_time < self.reverse_duration:
                print('reversing...')
                return self.reverse_throttle, 0.0
            else:
                self.state = "pivot_left"
                self.start_time = current_time

        # Pivot left (turn left in place)
        elif self.state == "pivot_left":
            if current_time - self.start_time < self.pivot_duration:
                print('turn left')
                return 0.0, -1.0  # Zero throttle, max left steering
            else:
                self.state = "forward"
                self.start_time = current_time

        # Move forward slightly
        elif self.state == "forward":
            if current_time - self.start_time < self.reverse_duration:
                print('goin forward')
                return self.forward_throttle, 0.0
            else:
                self.state = "pivot_right"
                self.start_time = current_time

        # Pivot right (turn right in place)
        elif self.state == "pivot_right":
            if current_time - self.start_time < self.pivot_duration:
                print('turnin right')
                return 0.0, 1.0  # Zero throttle, max right steering
            else:
                self.current_pivot += 1
                if self.current_pivot >= self.pivot_count:
                    self.state = "done"
                else:
                    self.state = "reverse"
                self.start_time = current_time

        # Done state
        elif self.state == "done":
            self.enabled = False

        return throttle, steering  # Default return if something goes wrong

    def shutdown(self):
        """Clean up resources when shutting down."""
        pass
