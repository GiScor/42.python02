class GardenError(Exception):
    def __init__(self, message: str = "Uknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: {plant_name}")


def test_watering_system() -> None:
    plants = ['Tomato', 'lettuce', 'cabbage']
    print("Opening watering system...")
    try:
        for plant in plants:
            water_plant(plant.capitalize())
            print(f"Watering {plant}: [OK]")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system...\n")

    print("Opening watering system...")
    try:
        for plant in plants:
            water_plant(plant)
            print(f"Watering {plant}: [OK]")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n"
              "...ending tests and returning to main")
    finally:
        print("Closing watering system...\n")


if __name__ == '__main__':
    test_watering_system()
    print('Cleanup always happens, even after errors')
