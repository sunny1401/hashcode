
from collections import OrderedDict
from abstract_class import(
    file_parser,
    get_score,
    get_pizza_delivery_data,
    write_output,
    PizzaDelivery
)
import copy


class ExDelivery(PizzaDelivery):

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
            all_ingredients = copy.deepcopy(self._pizza_dict[idx][1])
            iterv = 1
            list_idx = [i]
            key_list = [idx]
            for j, jdx in enumerate(index_remaining):
              if jdx != idx:
                  if self._pizza_dict[jdx][2]:
                      all_ingredients.update(self._pizza_dict[jdx][1])
                      list_idx.append(j)
                      key_list.append(jdx)
                      iterv += 1
                      if iterv == total_n:
                          best_team_combos[tuple(list_idx)] = [
                            len(all_ingredients) ** 2 - (len(self._pizza_dict[idx][1])+len(self._pizza_dict[jdx][1])),
                            all_ingredients,
                            key_list
                          ]
                          list_idx = [i]
                          key_list = [idx]
                          iterv = 1
                          all_ingredients = copy.deepcopy(self._pizza_dict[idx][1])

        print("Done with getting best combos")
        best_team_combos = OrderedDict(sorted(best_team_combos.items(), key=lambda item: item[1][0], reverse=True))
        first_data = next(iter(best_team_combos))
        dict_people_pizza = dict()
        keys = best_team_combos[first_data][2]
        idx_list = []
        for key in keys:
            del self._pizza_dict[key]
            idx_list.append(key - 1)

        dict_people_pizza[total_n]=[len(best_team_combos[first_data][1]), idx_list]
        return dict_people_pizza


file_names = {
    'a': '/content/drive/MyDrive/Colab Notebooks/a_example',
    'b': '/content/drive/MyDrive/Colab Notebooks/b_little_bit_of_everything.in',
    'c':'/content/drive/MyDrive/Colab Notebooks/c_many_ingredients.in',
    'd':'/content/drive/MyDrive/Colab Notebooks/d_many_pizzas.in',
    'e':'/content/drive/MyDrive/Colab Notebooks/e_many_teams.in'
    }

pizza_dict, two_member_team, three_member_team, four_member_team, total_pizza = file_parser(file_names['a'])

two_member_team = int(two_member_team)
three_member_team = int(three_member_team)
four_member_team = int(four_member_team)

# clean this
all_values = {two_member_team: 2, three_member_team: 3, four_member_team: 4}
if len(all_values) == 1:
    people = [2 for _ in range(0, two_member_team)]
    people.extend([3 for _ in range(0, three_member_team)])
    people.extend([4 for _ in range(0, four_member_team)])

else:
    max_v = max(all_values)
    people = [all_values[max_v] for _ in range(0, max_v)]
    if all_values[max_v] == 2:
        people.extend([3 for _ in range(0, three_member_team)])
        people.extend([4 for _ in range(0, four_member_team)])
    elif all_values[max_v] == 3:
        people.extend([2 for _ in range(0, two_member_team)])
        people.extend([4 for _ in range(0, four_member_team)])
    else:
        people.extend([2 for _ in range(0, two_member_team)])
        people.extend([3 for _ in range(0, three_member_team)])


r_delivery = ExDelivery(total_pizza_available=total_pizza, pizza_dict=pizza_dict)
data = get_pizza_delivery_data(r_delivery, people)
get_score(data)
write_output(obj=r_delivery, data=data, output_file='/content/drive/MyDrive/Colab Notebooks/op_a_example.op')
