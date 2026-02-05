#!/usr/bin/env python3

class GardenManager:
    """Represents a GardenManager."""

    def __init__(self, name: str) -> None:
        """Initialize a new GardenManager.

        Args:
            name: The name of the garden
        """
        self.name = name
        self.plants: list = []

    def add_plants(self, plants: list) -> None:
        """Add a list of plants to the garden.

        Args:
            plants: The list of plants to be added
        """
        for plant in plants:
            try:
                if plant == "":
                    raise ValueError("Plant name cannot be empty!")
                self.plants += [plant]
                print(f"Added {plant[0]} successfully")
            except ValueError as e:
                print(f"Error adding plant: {e}")

    def water_plants(self, plants: list) -> None:
        """Water the plants in the garden.

        Args:
            plants: The list of plants to be watered
        """
        print("Opening watering system")
        try:
            for plant in plants:
                print(f"Watering {plant[0]} - success")
        except Exception:
            pass
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plants: list) -> None:
        """Check the health of the plants in the garden.

        Args:
            plants: The list of plants to be checked
        """
        try:
            for plant in plants:
                if plant[1] < 1:
                    raise WaterError(f"Water level {plant[1]} "
                                     "is too low (min 1)")
                elif plant[1] > 10:
                    raise WaterError(f"Water level {plant[1]} "
                                     "is too high (max 10)")
                if plant[2] < 2:
                    raise PlantError(f"Sunlight hours {plant[2]} "
                                     "is too low (min 2)")
                elif plant[2] > 12:
                    raise PlantError(f"Sunlight hours {plant[2]} "
                                     "is too high (max 12)")
                print(f"{plant[0]}: healthy (water: {plant[1]}, "
                      f"sun: {plant[2]})")
        except (WaterError, PlantError) as e:
            print(f"Error checking {plant[0]}: {e}")


class GardenError(Exception):
    """General exception type for garden errors."""

    pass


class PlantError(GardenError):
    """Exception type for plant errors that inherits from GardenError."""

    pass


class WaterError(GardenError):
    """Exception type for water errors that inherits from GardenError."""

    pass


def test_garden_management(garden: GardenManager) -> None:
    """Test the error handling of the GardenManager's methods.

    Args:
        garden: The garden instance to be tested
    """
    print("Adding plants to garden...")
    garden.add_plants([["tomato", 5, 8], ["lettuce", 15, 5], ""])
    print("\nWatering plants...")
    garden.water_plants(garden.plants)
    print("\nChecking plant health...")
    garden.check_plant_health(garden.plants)
    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")


def main() -> None:
    """Run the main program."""
    print("=== Garden Management System ===\n")
    garden = GardenManager("Garden")
    test_garden_management(garden)
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
