#!/usr/bin/env python3

class GardenManager:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants: list = []

    def add_plants(self, plants: list) -> None:
        for plant in plants:
            try:
                if plant == "":
                    raise ValueError("Plant name cannot be empty!")
                self.plants += [plant]
                print(f"Added {plant} successfully")
            except ValueError as e:
                print(f"Error adding plant: {e}")

    def water_plants(self, plants: list) -> None:
        print("Opening watering system")
        try:
            for plant in plants:
                print(f"Watering {plant} - success")
        except Exception:
            pass
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plants: list) -> None:
        pass


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
    print("Adding plants to garden...")
    garden.add_plants(["tomato", "lettuce", ""])
    print("\nWatering plants...")
    garden.water_plants(garden.plants)


def main() -> None:
    """Run the main program."""
    print("=== Garden Management System ===\n")
    garden = GardenManager("Garden")
    test_garden_management(garden)


if __name__ == "__main__":
    main()
