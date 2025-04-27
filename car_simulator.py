# first git commit!

class Car():
    """
    A Car class that simulates basic operations of a car such as moving, stopping, and refueling.

    Attributes:
        model (str): The model of the car.
        gas_level (float): Current gas level in gallons.
        gas_max (float): Maximum gas capacity in gallons.
        consumption_rate (float): Gas consumption per mile.
        brand (str): Car brand (default: 'Ford').
        is_moving (bool): Indicates whether the car is currently moving.
    """
    def __init__(self, model: str, gas_level: float, gas_max: float, consumption_rate: float, brand: str ='Ford'):
        """
        Initializes a Car object with the provided attributes.

        Args:
            model (str): The model of the car.
            gas_level (float): Initial gas level (must be >= 0).
            gas_max (float): Maximum gas capacity.
            consumption_rate (float): Gas consumption rate per mile (must be > 0).
            brand (str): The brand of the car.

        Raises:
            ValueError: If gas_level is less than 0.
            ValueError: If consumption_rate is less than or equal to 0.
        """
        if gas_level < 0:
            # Prevent creation of a car with an invalid gas level.
            raise ValueError("A car cannot have less than a 0 level of gas!")
        if consumption_rate <= 0:
            raise ValueError("A car cannot use 0 or less gas while moving!")

        self.model = model
        self.gas_level = gas_level
        self.gas_max = gas_max
        self.consumption_rate = consumption_rate  # Gas used per mile.
        self.brand = brand
        self.is_moving = False

    def __str__(self):
        """
        Returns a human-readable string representation of the Car object.
        """
        return (f"Brand: {self.brand}, Model: {self.model}, "
                f"Gas Level: {self.gas_level}, Maximum Gas: {self.gas_max}, "
                f"Consumption Rate: {self.consumption_rate}")

    def go(self, speed: float, distance: float):
        """
        Starts the car's movement after validating inputs and calculating gas usage.

        Args:
            speed (float): The speed of the car (must be > 0).
            distance (float): The distance to travel (must be > 0).

        Returns:
            str: A message indicating the car's speed and remaining gas.

        Raises:
            Exception: If the car is already moving.
            ValueError: If speed, distance, or gas_level is invalid.
        """
        if self.is_moving:
            # Prevent starting movement if the car is already moving.
            raise Exception("The car is already moving! Are you paying attention?")
        elif speed <= 0 or distance <= 0 or self.gas_level <= 0:
            # Ensure valid input values for speed, distance, and gas level.
            raise ValueError("Speed and distance must be greater than 0, and the car must have gas!")
        else:
            # Calculate gas required for the journey.
            gas_used = distance * self.consumption_rate
            if gas_used > self.gas_level:
                # Ensure sufficient gas for the journey.
                raise ValueError("You cannot complete this journey. Not enough gas.")
            else:
                # Update the car state and reduce gas level.
                self.is_moving = True
                self.gas_level -= gas_used
                return (f"The car will travel at {speed} miles per hour. "
                        f"{self.gas_level} gallons of gas will remain after the journey.")

    def stop(self):
        """
        Stops the car if it is currently moving.

        Returns:
            str: A message confirming the car has stopped and remaining gas.

        Raises:
            Exception: If the car is already stopped.
        """
        if not self.is_moving:
            raise Exception(f"The car is already stopped. {self.gas_level} gallons of gas remain.")
        else:
            self.is_moving = False
            return f"The car is stopping. {self.gas_level} gallons of gas remain."

    def refill_gas(self, amount: float):
        """
        Refills the car with the specified amount of gas.

        Args:
            amount (float): The amount of gas to refill (must be > 0).

        Returns:
            str: A message confirming the new gas level.

        Raises:
            ValueError: If the refill amount is less than or equal to 0.
            ValueError: If the refill exceeds the gas tank's capacity.
        """
        gas_level_new = amount + self.gas_level
        if amount <= 0:
            raise ValueError("You cannot refill with 0 or a negative amount of gas!")
        elif gas_level_new > self.gas_max:
            raise ValueError("The gas tank cannot hold that much gas!")
        else:
            self.gas_level += amount
            return f"You now have {self.gas_level} gallons of gas!"

# Example car instance for testing.
car_1 = Car(model='Fiesta', gas_level=50, gas_max=100, consumption_rate=2)

def main():
    """
    Main function to demonstrate the Car class functionality.
    """
    try:
        print(car_1)
        print(car_1.go(speed=30, distance=2))
        print(car_1.stop())
        print(car_1.refill_gas(25))
    except Exception as e:
        # Print any error encountered during the demonstration.
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
