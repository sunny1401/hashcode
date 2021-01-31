from abstract_class import(
    file_parser,
    file_parser2,
    get_score,
    get_pizza_delivery_data,
    write_output,
    PizzaDelivery
)
from itertools import combinations
from collections import OrderedDict
import random


file_names = {
    'a': 'a_example',
    'b': 'b_little_bit_of_everything.in',
    'c': 'c_many_ingredients.in',
    'd': 'd_many_pizzas.in',
    'e': 'e_many_teams.in'
    }


def findsubsets(s, n):
    return set(combinations(s, n))


class HEDelivery(PizzaDelivery):

    def __init__(self, total_pizza_available, pizza_dict):
        super().__init__(
            total_pizza_available=total_pizza_available,
            pizza_dict=pizza_dict
        )

    def _return_less_than_4_people_pizza(self, n):
        all_combinations = findsubsets(self._pizza_dict.keys(), n)
        new_selection_dict = dict()
        for key in all_combinations:
            data = set()
            for i in key:
                data = data.union(self._pizza_dict[i])
            new_selection_dict[tuple(key)] = [list(data), len(data) ** 2]
        new_selection_dict = OrderedDict(sorted(new_selection_dict.items(), key=lambda item: item[1][1], reverse=True))
        first_key = next(iter(new_selection_dict))
        selected_data = [len(new_selection_dict[first_key][0]), first_key]
        for key in first_key:
            del self._pizza_dict[key]
        del new_selection_dict
        del all_combinations
        return selected_data

    def _get_pizza_for_4(self, n):
        pizza_idx_list = set()
        dict_ingredients = set()
        while n:
            pizza_idx = random.choice(list(self._pizza_dict.keys()))
            print(f"pizza_idx is {pizza_idx}")
            if pizza_idx in self._pizza_dict and pizza_idx not in pizza_idx_list:
                for i in self._pizza_dict[pizza_idx]:
                    dict_ingredients.add(i)
                pizza_idx_list.add(int(pizza_idx)- 1)
                n -= 1
                del self._pizza_dict[pizza_idx]

        return [len(dict_ingredients), pizza_idx_list]

    def return_pizza(self, total_n):
        print(f"getting for {total_n}")
        dict_people_pizza = dict()
        n = total_n
        if total_n < 4:
            data = self._return_less_than_4_people_pizza(total_n)
        else:
            data = self._get_pizza_for_4(total_n)

        dict_people_pizza[total_n] = data
        return dict_people_pizza
