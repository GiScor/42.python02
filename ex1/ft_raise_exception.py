def input_temperature(temp_str: str | int) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    tests: list[int | str] = [25, 'abc', 100, -50]
    for t in tests:
        print(f"Input data is '{t}'")
        try:
            input_temperature(t)
            print(f"Temperature is now {t}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}\n")
    print("=== Test complete. No crashes ===")


def main() -> None:
    test_temperature()


main()
