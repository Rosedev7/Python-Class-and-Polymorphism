# Base class: Device
class Device:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def info(self):
        return f"{self.brand} {self.model} with {self.battery_life} hours of battery life."

# Subclass: Smartwatch
class Smartwatch(Device):
    def __init__(self, brand, model, battery_life, water_resistant, heart_rate_monitor):
        super().__init__(brand, model, battery_life)
        self.water_resistant = water_resistant
        self.heart_rate_monitor = heart_rate_monitor

    def track_activity(self):
        return "Tracking your steps, distance, and calories burned!"

    def check_heart_rate(self):
        return f"Heart rate: {self.heart_rate_monitor} bpm."

# Subclass: FitnessTracker (inheritance with a twist)
class FitnessTracker(Smartwatch):
    def __init__(self, brand, model, battery_life, water_resistant, heart_rate_monitor, sleep_tracking):
        super().__init__(brand, model, battery_life, water_resistant, heart_rate_monitor)
        self.sleep_tracking = sleep_tracking

    def track_sleep(self):
        return f"Monitoring sleep for {self.sleep_tracking} hours."

# Testing the classes
if __name__ == "__main__":
    device1 = Device("Generic", "Model X", 24)
    print(device1.info())

    smartwatch = Smartwatch("FitBrand", "Active2", 48, True, 72)
    print(smartwatch.info())
    print(smartwatch.track_activity())
    print(smartwatch.check_heart_rate())

    fitness_tracker = FitnessTracker("TrackPro", "Elite", 72, True, 68, 8)
    print(fitness_tracker.info())
    print(fitness_tracker.track_activity())
    print(fitness_tracker.track_sleep())
