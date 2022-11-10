class Computer:
    def __init__(self, processor_frequency_MHz, number_cores, memory_capacity_MB, hard_disk_capacity_GB):
        self.processor_frequency_MHz = processor_frequency_MHz
        self.number_cores = number_cores
        self.memory_capacity_MB = memory_capacity_MB
        self.hard_disk_capacity_GB = hard_disk_capacity_GB

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
