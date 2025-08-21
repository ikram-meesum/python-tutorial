class Car():

    def start(self):
        print("Start the car.")

    def stop(self):
        print("Stop the car.")


class Honda(Car):
    def __init__(self, brand):
        self.brand = brand


class Toyota(Honda):
    def __init__(self, types):
        self.types = types


car1 = Toyota("petrol")
car1.start()
car1.stop()
