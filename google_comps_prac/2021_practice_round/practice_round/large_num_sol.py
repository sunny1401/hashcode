from abstract_class import PizzaDelivery
from collections import OrderedDict
from structlog import getLogger

log = getLogger()


class LNPizza(PizzaDelivery):

    def __init__(self, total_pizza_available, pizza_dict, four_people, three_people, two_people):
        super().__init__(
            total_pizza_available=total_pizza_available,
            pizza_dict=pizza_dict
        )
        self._pizza_dict = OrderedDict(sorted(self._pizza_dict.items(), key=lambda item: len(item[1]), reverse=True))
        self._four_people = four_people
        self._three_people = three_people
        self._two_people = two_people
        self._people_num = dict()
        self._all_data = list()
        self._original_count = {2: two_people, 3: three_people, 4: four_people}

    def return_pizza(self):
        log.info("Getting optimal people count")
        self._get_people_count()
        self._people_num = {k: v for k, v in sorted(self._people_num.items(), key=lambda item: item, reverse=True)}
        max_ingredients = set()
        new_data_dict = dict()
        log.info("calculating the max difference between different pizzas' ingredients")
        for i in self._pizza_dict:
            if len(self._pizza_dict[i]) > 0:
                max_ingredients = self._pizza_dict[i] - max_ingredients
                new_data_dict[i] = (self._pizza_dict[i], len(max_ingredients))

        new_data_dict = {k: v for k, v in sorted(new_data_dict.items(), key=lambda item: item[1], reverse=True)}

        log.info("calculating the best possible data combinations")
        for i in self._people_num:
            j = 0
            while j < (i * self._people_num[i]):
                temp_data = set()
                keys = list(new_data_dict.keys())[:i]
                for k in keys:
                    temp_data = temp_data.union(self._pizza_dict[k])
                    del new_data_dict[k]
                self._all_data.append({i: (len(temp_data), keys)})
                j += i

        log.info("All done!")
        self.pizza_delivery = len(self._all_data)

    def _check_single_count(self, num, num_total):
        """
        num: int
        num_total: int
        """
        condition = not self._total_pizza_available % num and \
                    int(self._total_pizza_available / num) <= num_total and \
                    int(self._total_pizza_available / num) * num == self._total_pizza_available
        if condition:
            self._people_num[num] = int(self._total_pizza_available / num)
            self._total_pizza_available = 0

    def _add_people(self):

        for people in self._people_num:
            ds = int(self._total_pizza_available / people)
            if ds < self._people_num[people] and self._total_pizza_available - (ds * people) >= 0:
                self._people_num[people] = ds
            self._total_pizza_available -= (self._people_num[people] * people)

    def _get_people_count(self):
        for i in self._original_count:
            if self._total_pizza_available:
                self._check_single_count(i, self._original_count[i])

        if self._total_pizza_available:
            if not (self._total_pizza_available % 24):
                self._people_num[2] = self._two_people
                self._people_num[3] = self._three_people
                self._people_num[4] = self._four_people
                self._add_people()

            elif not (self._total_pizza_available % 12):
                self._people_num[3] = self._three_people
                self._people_num[4] = self._four_people
                self._add_people()

            elif not (self._total_pizza_available % 6):
                self._people_num[2] = self._two_people
                self._people_num[3] = self._three_people
                self._add_people()

            elif not (self._total_pizza_available % 8):
                self._people_num[2] = self._two_people
                self._people_num[4] = self._four_people
                self._add_people()

        while self._total_pizza_available > 1:
            count = 0
            for i in self._original_count:
                if i not in self._people_num:
                    log.info(f"checking for {i} which is not in original count")
                    rs = None
                    ds = int(self._total_pizza_available / i)
                    if ds > 0:
                        if ds < self._original_count[i]:
                            rs = i * ds

                        else:
                            ds = self._original_count[i]
                            rs = i * self._original_count[i]
                    if rs:
                        self._total_pizza_available = self._total_pizza_available - rs

                    if self._total_pizza_available >= 0 and rs:
                        self._people_num[i] = ds

                    if self._total_pizza_available < 2:
                        break
                count += 1

            if count == len(self._original_count):
                break


    @property
    def people_num(self):
        return self._people_num

    @property
    def data(self):
        return self._all_data
