class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = 0
        for worker in self.workers:
            sum_salaries += worker.salary

        if self.__budget >= sum_salaries:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_tends = 0
        for animal in self.animals:
            sum_tends += animal.money_for_care

        if self.__budget >= sum_tends:
            self.__budget -= sum_tends
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal.__repr__())
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal.__repr__())
            else:
                cheetahs.append(animal.__repr__())

        result += f"----- {len(lions)} Lions:\n"
        result += '\n'.join(lions)
        result += f'\n----- {len(tigers)} Tigers:\n'
        result += '\n'.join(tigers)
        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += '\n'.join(cheetahs)
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker.__repr__())
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker.__repr__())
            else:
                vets.append(worker.__repr__())

        result += f"----- {len(keepers)} Keepers:\n"
        result += '\n'.join(keepers)
        result += f'\n----- {len(caretakers)} Caretakers:\n'
        result += '\n'.join(caretakers)
        result += f"\n----- {len(vets)} Vets:\n"
        result += '\n'.join(vets)
        return result
