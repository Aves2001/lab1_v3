from computer import Computer
from laptop import Laptop


def main():
    comp = Computer()
    comp.input_info()
    comp.cost()
    comp.is_suitable()

    print("-" * 50)

    laptop = Laptop(processor_frequency_MHz=3000,
                    number_cores=4,
                    memory_capacity_MB=5000,
                    hard_disk_capacity_GB=1000,
                    duration_of_autonomous_operation_in_minutes=120)
    print(laptop)
    laptop.cost()
    laptop.is_suitable()


if __name__ == '__main__':
    main()
