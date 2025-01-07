import time

class TurnAround:
    def __init__(self, pivot_duration=1.5, reverse_duration=1.0, forward_throttle=0.3, reverse_throttle=-0.3, pivot_count=2):
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

    def run(self, throttle, steering):
        """
        Generate throttle and steering values for tight turnaround.

        Args:
            throttle (float): Current throttle input (ignored in this part).
            steering (float): Current steering input (ignored in this part).

        Returns:
            tuple: (throttle, steering) values to control the car.
        """
        current_time = time.time()

        # Start timing for the first state
        if self.start_time is None:
            self.start_time = current_time

        # Reverse straight
        if self.state == "reverse":
            if current_time - self.start_time < self.reverse_duration:
                return self.reverse_throttle, 0.0
            else:
                self.state = "pivot_left"
                self.start_time = current_time

        # Pivot left (turn left in place)
        elif self.state == "pivot_left":
            if current_time - self.start_time < self.pivot_duration:
                return 0.0, -1.0  # Zero throttle, max left steering
            else:
                self.state = "forward"
                self.start_time = current_time

        # Move forward slightly
        elif self.state == "forward":
            if current_time - self.start_time < self.reverse_duration:
                return self.forward_throttle, 0.0
            else:
                self.state = "pivot_right"
                self.start_time = current_time

        # Pivot right (turn right in place)
        elif self.state == "pivot_right":
            if current_time - self.start_time < self.pivot_duration:
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
            return 0.0, 0.0  # Stop movement

        return 0.0, 0.0  # Default return if something goes wrong

    def shutdown(self):
        """Clean up resources when shutting down."""
        pass
