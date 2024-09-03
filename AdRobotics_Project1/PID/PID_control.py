class PIDController:
    def __init__(self, kp, ki, kd, setpoint=0, sample_time=0.01):
        """
        Initialize the PID controller with the given gains.
        kp: Proportional gain
        ki: Integral gain
        kd: Derivative gain
        setpoint: Desired value the PID will attempt to reach
        sample_time: Time between updates in seconds
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.sample_time = sample_time
        
        # Initialize previous error and integral term
        self.previous_error = 0
        self.integral = 0
        self.last_time = None

    def update(self, feedback_value, current_time=None):
        """
        Calculate the control signal based on the feedback value.
        feedback_value: Current value from the system being controlled
        current_time: The current time (in seconds). If not provided, the system will use time.time().
        """
        if current_time is None:
            import time
            current_time = time.time()
        
        # Calculate time difference
        if self.last_time is None:
            self.last_time = current_time
        delta_time = current_time - self.last_time

        if delta_time >= self.sample_time:
            # Calculate error
            error = self.setpoint - feedback_value
            
            # Proportional term
            proportional = self.kp * error
            
            # Integral term
            self.integral += error * delta_time
            integral = self.ki * self.integral
            
            # Derivative term
            derivative = self.kd * (error - self.previous_error) / delta_time
            
            # Calculate PID output
            output = proportional + integral + derivative
            
            # Update previous values for the next iteration
            self.previous_error = error
            self.last_time = current_time
            
            return output
        else:
            return None




# Example usage
"""

if __name__ == "__main__":
    import time

    # Create a PID controller with kp=1.0, ki=0.1, kd=0.05
    pid = PIDController(kp=0.4, ki=0.1, kd=0.01, setpoint=1000)

    # Simulate a process variable starting at 0
    process_variable = 0

    # Simulate control loop
    for i in range(100):
        # Get the control signal from PID controller
        control_signal = pid.update(process_variable)
        
        if control_signal is not None:
            # Apply control signal to the process variable (simple simulation)
            process_variable += control_signal * 0.1
            
            # Print the process variable
            print(f"Time: {i}, Process Variable: {process_variable:.2f}, Control Signal: {control_signal:.2f}")
        
        # Wait for a bit before next iteration
        time.sleep(0.01)

"""