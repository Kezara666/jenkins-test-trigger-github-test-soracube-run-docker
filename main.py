def main():
    print("🚀 Jenkins Build Test - Buggy Version")
    # Intentional bug: division by zero
    result = 10 / 0
    print(f"Result is {result}")

if __name__ == "__main__":
    main()
