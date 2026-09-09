def input_temperature(temp_str: int | str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    tests: list[int | str] = [25, 'abc']
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
