from computer import Computer
from laptop import Laptop


def main():
    comp = Computer(processor_frequency_MHz=2000,
                    number_cores=2,
                    memory_capacity_MB=2048,
                    hard_disk_capacity_GB=320)
    print(comp)
    comp.cost()
    comp.is_suitable()

    print("-" * 50)

    laptop = Laptop(processor_frequency_MHz=3000,
                    number_cores=4,
                    memory_capacity_MB=5000,
                    hard_disk_capacity_GB=1000,
                    duration_of_autonomous_operation_in_minutes=60)
    print(laptop)
    laptop.cost()
    laptop.is_suitable()


if __name__ == '__main__':
    main()
