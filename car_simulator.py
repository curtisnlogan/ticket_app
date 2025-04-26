class Car():
    """ DOCSTRINGS (Classes & Functions)
    Description: A Car class that simulates some basic operations of a car such as going, stopping, and refilling gas.

    Attributes:
        model (str): The model of the car.
        gas_level (float): Current gas level.
        gas_max (float): Maximum gas capacity.
        consumption_rate (float): Gas consumption per mile.
        brand (str): Car brand (default: 'Ford').
        is_moving (bool): Indicator whether the car is moving.
    DOCSTRINGS """
    def __init__(self, model: str, gas_level: float, gas_max: float, consumption_rate: float, brand: str ='Ford'): # model: str etc. increases readability of your code
        if gas_level < 0:
            # raising an exception here stops the creation of an invalid Car object, which is preferable to returning a message.
            raise ValueError("A car cannot have less than a 0 level of gas!")
        if consumption_rate <= 0:
            raise ValueError("A car cannot use 0 or less gas whilst going!")
        
        self.model = model
        self.gas_level = gas_level
        self.gas_max = gas_max
        self.consumption_rate = consumption_rate  # How much the gas level is reduced per mile traveled on average.
        self.brand = brand

        self.is_moving = False
    
    def __str__(self):
        """
        Returns a human-readable string representation of the Car object; useful for printing.
        """
        return f"Brand: {self.brand}, Model: {self.model}, Gas Level: {self.gas_level}, Maximum Amount of Gas: {self.gas_max}, Consumption Rate: {self.consumption_rate}"

    def go(self, speed: float, distance: float):
        """
        Attempts to start the car's movement. It checks if the car is already moving, validates inputs, calculates gas usage, and then updates the car's state if there is sufficient gas.
        """
        if self.is_moving:
            # Check if the car is already in motion. Check for True Bool.
            raise Exception("The car is already going! Are you paying attention?")
        elif speed <= 0 or distance <= 0 or self.gas_level <= 0:
            # Validate that speed and distance are positive values.
            raise ValueError("You cannot go anywhere at 0 mph or below! and/or you cannot travel 0 miles or lower and/or you cannot go without gas!")
        else:
            # Calculate the gas used for the journey (distance multiplied by consumption rate).
            gas_used = distance * self.consumption_rate
            if gas_used > self.gas_level:
                # Ensure there is enough gas for the journey.
                raise ValueError("You cannot complete this journey. You do not have a high enough level of gas.")
            else:
                # Set the car to moving and update the gas level after the journey.
                self.is_moving = True
                self.gas_level -= gas_used
                return f"The car will travel at {speed} miles per hour. {self.gas_level} gallons of gas will remain after you have completed this journey."

    # Stops the car and updates its moving state accordingly.
    def stop(self):
        if not self.is_moving:
            raise Exception(f"The car has already stopped. {self.gas_level} gallons of gas remain.")
        else:
            self.is_moving = False
            return f"The car is stopping. {self.gas_level} gallons of gas remain."
    
    def refill_gas(self, amount: float):
        gas_level_new = amount + self.gas_level
        if amount <= 0:
            raise ValueError (f"You cannot refill with 0 or minus amounts of gas!")
        elif gas_level_new > self.gas_max:
            raise ValueError("Your gas tank is too small for that refill!")
        else:
            self.gas_level += amount
            return f"You now have {self.gas_level} gallons of gas!"

car_1 = Car(model='Fiesta', gas_level=50, gas_max=100, consumption_rate=2)

def main():
    try:
        print(car_1)
        print(car_1.go(speed=30, distance=2))
        print(car_1.stop())
        print(car_1.refill_gas(25))
    except Exception as e:
        # 'e' is the exception object that holds details of any error encountered in the try block. Good to include this for testing purposes. This file would be a module file in the dunder "__main__" framework.
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
