from abstract_class import PizzaDelivery
from collections import OrderedDict
from random import randint


class RandomNEGDelivery(PizzaDelivery):

    def __init__(self, total_pizza_available, pizza_dict):
        super().__init__(
            total_pizza_available=total_pizza_available,
            pizza_dict=pizza_dict
        )

    def return_pizza(self, total_n):
        best_team_combos = dict()
        index_remaining = list(self._pizza_dict.keys())
        print(f"doing for {total_n} people")
        for i, idx in enumerate(index_remaining):
            all_ingredients = self._pizza_dict[idx][1]
            iterv = 1
            list_idx = [i]
            for j, jdx in enumerate(index_remaining[i:]):
                if iterv == total_n:
                    break
                all_ingredients.update(self._pizza_dict[jdx][1])
                list_idx.append(j)
                iterv += 1
            if iterv == total_n:
                print('here')
                best_team_combos[tuple(list_idx)] = [len(all_ingredients) ** 2, list_idx]

        print("Done with getting best combos")
        best_team_combos = OrderedDict(sorted(best_team_combos.items(), key=lambda item: item[1][0], reverse=True))
        import pdb
        pdb.set_trace()
        first_data = next(iter(best_team_combos))


        dict_people_pizza = dict(total_n=[len(all_ingredients), pizza_idx_list])
        return dict_people_pizza
