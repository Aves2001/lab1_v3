class Computer:
    def __init__(self,
                 processor_frequency_MHz=0,
                 number_cores=0,
                 memory_capacity_MB=0,
                 hard_disk_capacity_GB=0):
        self.__processor_frequency_MHz = processor_frequency_MHz
        self.__number_cores = number_cores
        self.__memory_capacity_MB = memory_capacity_MB
        self.__hard_disk_capacity_GB = hard_disk_capacity_GB

    @property
    def processor_frequency_MHz(self):
        return self.__processor_frequency_MHz

    @processor_frequency_MHz.setter
    def processor_frequency_MHz(self, processor_frequency_MHz):
        self.__processor_frequency_MHz = processor_frequency_MHz

    @property
    def number_cores(self):
        return self.__number_cores

    @number_cores.setter
    def number_cores(self, number_cores):
        self.__number_cores = number_cores

    @property
    def memory_capacity_MB(self):
        return self.__memory_capacity_MB

    @memory_capacity_MB.setter
    def memory_capacity_MB(self, memory_capacity_MB):
        self.__memory_capacity_MB = memory_capacity_MB

    @property
    def hard_disk_capacity_GB(self):
        return self.__hard_disk_capacity_GB

    @hard_disk_capacity_GB.setter
    def hard_disk_capacity_GB(self, hard_disk_capacity_GB):
        self.__hard_disk_capacity_GB = hard_disk_capacity_GB

    def __str__(self):
        return f"""Частота процесора: {self.processor_frequency_MHz} MHz
Кількість ядер: {self.number_cores}
ОЗУ: {self.memory_capacity_MB} МБ
Обсяг жорсткого диска: {self.hard_disk_capacity_GB} GB"""

    def _cost(self):
        return self.processor_frequency_MHz * self.number_cores / 100 + \
               self.memory_capacity_MB / 80 + \
               self.hard_disk_capacity_GB / 20

    def _is_suitable(self):
        if self.processor_frequency_MHz < 2000:
            return False
        if self.number_cores < 2:
            return False
        if self.memory_capacity_MB < 2048:
            return False
        if self.hard_disk_capacity_GB < 320:
            return False
        return True

    def cost(self, name="комп'ютера"):
        print(f"Приблизна розрахункова вартість {name}: {self._cost()}")

    def is_suitable(self, name="Комп'ютер"):
        if self._is_suitable():
            print(f"{name} придатний для використання")
        else:
            print(f"{name} НЕ придатний для використання")


    def input_info(self):
        try:
            self.processor_frequency_MHz = int(input("Частота процесора в MHz: "))
            self.number_cores = int(input("Кількість ядер: "))
            self.memory_capacity_MB = int(input("ОЗУ в МБ: "))
            self.hard_disk_capacity_GB = int(input("Обсяг жорсткого диска в GB: "))
        except Exception as err:
            print("!!!Не коректно введено дані!!!\n")
            print(self)

