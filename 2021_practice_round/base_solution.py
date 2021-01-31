import random

from abstract_class import (
    PizzaDelivery,
    file_parser,
    get_score,
    get_pizza_delivery_data,
    write_output
)


class BrutePizzaDelivery(PizzaDelivery):

    def __init__(self, total_pizza_available, pizza_dict):
        super().__init__(
            total_pizza_available=total_pizza_available,
            pizza_dict=pizza_dict
        )

    def return_pizza(self, total_n):
        dict_people_pizza = dict()
        pizza_idx_list = list()
        dict_ingredients = set()

        print(f"doing for {total_n} people")
        n = total_n
        while n:
            pizza_idx = random.randint(1, len(self.pizza_dict))
            print(f"pizza_idx is {pizza_idx} and {self.pizza_dict[pizza_idx][2]}")
            if self.pizza_dict[pizza_idx][2]:
                for i in self.pizza_dict[pizza_idx][1]:
                    dict_ingredients.add(i)
                self.pizza_dict[pizza_idx][2] = 0
                pizza_idx_list.append(pizza_idx - 1)
                n -= 1

        dict_people_pizza[total_n] = [len(dict_ingredients), pizza_idx_list]
        print(f" - deliveries = {self.pizza_delivery}")
        return dict_people_pizza


pizza_dict, two_member_team, three_member_team, four_member_team, total_pizza = file_parser('../a_example')

two_member_team = int(two_member_team)
three_member_team = int(three_member_team)
four_member_team = int(four_member_team)

people = [2 for _ in range(0, two_member_team)]
people.extend([3 for _ in range(0, three_member_team)])
people.extend([4 for _ in range(0, four_member_team)])
brte_piz = BrutePizzaDelivery(total_pizza_available=total_pizza, pizza_dict=pizza_dict)

data = get_pizza_delivery_data(obj=brte_piz, people=people)
score = get_score(data)
write_output(obj=brte_piz, data=data, output_file='/content/drive/MyDrive/Colab Notebooks/output_d_brtz_many_pizza.in')
