from computer import Computer


class Laptop(Computer):
    def __init__(self,
                 processor_frequency_MHz,
                 number_cores,
                 memory_capacity_MB,
                 hard_disk_capacity_GB,
                 duration_of_autonomous_operation_in_minutes):
        super(Laptop, self).__init__(processor_frequency_MHz, number_cores, memory_capacity_MB, hard_disk_capacity_GB)

        self.duration_of_autonomous_operation_in_minutes = duration_of_autonomous_operation_in_minutes

    def _cost(self):
        return super(Laptop, self)._cost() + self.duration_of_autonomous_operation_in_minutes / 10

    def _is_suitable(self):
        if self.duration_of_autonomous_operation_in_minutes < 60:
            return False
        return super(Laptop, self)._is_suitable()
    
    def cost(self, **kwargs):
        super(Laptop, self).cost(name="ноутбука")

    def is_suitable(self, **kwargs):
        super(Laptop, self).is_suitable(name="Ноутбук")
