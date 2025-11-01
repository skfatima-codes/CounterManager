from counters.up_counter import UpCounter
from counters.down_counter import DownCounter

def main():
    counters = []  # polymorphic list (holds both UpCounter & DownCounter)

    while True:
        print("\n=== Counter System Menu ===")
        print("1. Add Up Counter")
        print("2. Add Down Counter")
        print("3. Count All Counters")
        print("4. Show Counter Values")
        print("5. Reset All Counters")
        print("6. Exit")

        choice = input(" Enter your choice (1–6): ")

        if choice == "1":
            start = int(input("Enter starting value: "))
            
            step = int(input("Enter step value: "))
            counters.append(UpCounter(start, step))
            print(" UpCounter added!")

        elif choice == "2":
            start = int(input("Enter starting value: "))
            step = int(input("Enter step value: "))
            counters.append(DownCounter(start, step))
            print("DownCounter added!")

        elif choice == "3":
            if not counters:
                print(" No counters to count!")
            else:
                print("\n Counting all counters...")
                for i, c in enumerate(counters, start=1):
    # f-string displays class name + new counted value
                    print(f"Counter {i} ({type(c).__name__}) new value → {c.count()}")

        elif choice == "4":
            if not counters:
                print(" No counters created yet!")
            else:
                print(" Current counter values:")
                for i, c in enumerate(counters, start=1):
        # type(c).__name__ → shows class name (UpCounter or DownCounter)
        # {c} → automatically calls __str__() of that counter
                    print(f"Counter {i} ({type(c).__name__}): {c.get_value()}")

        elif choice == "5":
            if not counters:
                print(" No counters to reset!")
            else:
                print("\n Resetting all counters...")
                for i, c in enumerate(counters, start=1):
                    c.reset()
                    print(f"Counter {i} reset → {c.get_value()}")
                print(" All counters reset successfully!")

        elif choice == "6":
            print("Exit")
            break

        else:
            print(" Invalid choice!")


if __name__ == "__main__":
    main()
