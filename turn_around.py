import time

class TurnAround:
    def __init__(self, reverse_duration=0.7, forward_throttle=0.8, reverse_throttle=-1.0, pivot_count=13):
        """
        Initialize the TightTurn part.

        Args:
            pivot_duration (float): Time (in seconds) for the pivot (turning in place).
            reverse_duration (float): Time (in seconds) for reversing in a straight line.
            forward_throttle (float): Throttle value for forward movement.
            reverse_throttle (float): Throttle value for reverse movement.
            pivot_count (int): Number of pivot cycles to complete a tight turn.
        """
        self.reverse_duration = reverse_duration
        self.forward_throttle = forward_throttle
        self.reverse_throttle = reverse_throttle
        self.pivot_count = pivot_count
        self.state = "forward"  # Initial state
        self.start_time = None
        self.current_pivot = 0
        self.enabled = False
        self.pause_default = 5
        self.pause_reverse = self.pause_default
        self.pause_forward = self.pause_default

    def launch(self):
        print(self.enabled)
        self.enabled = True

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

        current_time = time.time()


        # Start timing for the first state
        if self.start_time is None:
            self.start_time = current_time

        # Reverse straight
        if self.state == "reverse":
            self.pause_forward = self.pause_default
            if self.pause_reverse > 0:
                self.pause_reverse -= 1
                if self.pause_reverse == 2 or self.pause_reverse == 4:
                    return -0.7, 0
                return -0.0, 0.0
            if current_time - self.start_time < self.reverse_duration:
                print('reversing...')
                return self.reverse_throttle, 1.0
            else:
                self.state = "forward"
                self.start_time = current_time

        # Move forward slightly
        elif self.state == "forward":
            self.pause_reverse = self.pause_default
            if self.pause_forward > 0:
                self.pause_forward -= 1
                return 0.0, 0
            if current_time - self.start_time < self.reverse_duration:
                print('goin forward')
                return self.forward_throttle, -1.0
            else:
                self.state = "reverse"
                self.start_time = current_time
                self.current_pivot += 1
                if self.pivot_count == self.current_pivot:
                    self.state = "done"


        # Done state
        elif self.state == "done":
            print("TURN_AROUND - Turn around cicle done")
            self.enabled = False
            self.current_pivot = 0
            self.start_time = None
            self.state = "forward"
            self.pause_reverse = self.pause_default
            self.pause_forward = self.pause_default


        return 0.0,0.0  # Default return if something goes wrong

    def shutdown(self):
        """Clean up resources when shutting down."""
        pass
