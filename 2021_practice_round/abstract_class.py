from abc import ABC, abstractmethod


class PizzaDelivery(ABC):

    def __init__(self, total_pizza_available, pizza_dict):
        self._total_pizza_available = int(total_pizza_available)
        self._pizza_delivery: int = 0
        self._pizza_dict = pizza_dict
        self._result_dict = dict()

    @abstractmethod
    def return_pizza(self, total_n=None):
        raise NotImplementedError

    @property
    def total_pizza_available(self):
        return self._total_pizza_available

    @total_pizza_available.setter
    def total_pizza_available(self, value):
        self._total_pizza_available = value

    @property
    def pizza_delivery(self):
        return self._pizza_delivery

    @pizza_delivery.setter
    def pizza_delivery(self, value):
        self._pizza_delivery = value

    @property
    def pizza_dict(self):
        return self._pizza_dict


file_names = {
    'a': 'a_example',
    'b': 'b_little_bit_of_everything.in',
    'c': 'c_many_ingredients.in',
    'd': 'd_many_pizzas.in',
    'e': 'e_many_teams.in'
}


def file_details(file_key):
    pizza_dict = dict()
    pizza_count, two_people, three_people, four_people = (None, None, None, None)
    line_count = 0
    with open(file_names[file_key], 'r') as f:
        all_file_lines = f.readlines()

    for line in all_file_lines:
        if not line_count:
            pizza_count, two_people, three_people, four_people = (int(i) for i in line.split())
            pizza_dict = {key: set() for key in range(pizza_count)}
        else:
            pizza_dict[line_count - 1] = set(line.split()[1:])

        line_count += 1
    return pizza_dict, pizza_count, two_people, three_people, four_people


def get_score(data):
    score = sum([values[0] ** 2 for dicky in data for key, values in dicky.items()])
    return score


def get_2combo_count(values, denom, N):
    last_sm = -1
    last_hg = -1
    value = -1
    for i in range(1, values[0] + 1):
        for j in range(1, values[1]+ 1):
            value = (i*denom[0])+(j*denom[1])
            if value <= N:
                last_sm = i
                last_hg = j
            else:
                break
        if value > N:
            break
    return last_sm, last_hg


def get_3combo_count(values, N):
    last_sm = -1
    last_mid = -1
    last_hg = -1
    for i in range(1, values[0] + 1):
        value = -1
        for j in range(1, values[1] + 1):
            for k in range(1, values[2] + 1):
                value = (i * 2) + (j * 3) + (k * 4)
                if value <= N:
                    last_sm = i
                    last_mid = j
                    last_hg = k
                else:
                    break
            if value > N:
                break
        if value > N:
            break

    return last_sm, last_mid, last_hg


def get_people_count(N, two_people, three_people, four_people):
    # first dp prob - check or tools (limited coin change)

    ways = {}
    combo_ways = {}
    if two_people * 2 < N:
        ways[(2,)] = two_people

    else:
        ways[(2,)] = {int(N / 2)}
    if three_people * 3 < N:
        ways[(3,)] = three_people
    elif int(N / 3) < three_people:
        ways[(3,)] = int(N / 3)
    if four_people * 4 < N:
        ways[(4,)] = four_people
    elif int(N / 4) < four_people:
        ways[(4,)] = int(N / 4)

    ways[(2, 3)] = get_2combo_count([ways[2,], ways[3,]], [2, 3], N)
    ways[(2, 4)] = get_2combo_count([ways[2,], ways[4,]], [2, 4], N)
    ways[(3, 4)] = get_2combo_count([ways[3,], ways[4,]], [3, 4], N)

    ways[2, 3, 4] = get_3combo_count([ways[2,], ways[3,], ways[4,]], N)
    updated_ways = dict()

    for k, v in ways.items():
        if (isinstance(v, tuple)) and all(i > 0 for i in v):
            updated_ways[k] = v, sum(v)
        elif isinstance(v, int):
            updated_ways[k] = v, v

    del ways
    return updated_ways


def get_pizza_delivery_data(obj, people):
    data = []
    for number in people:
        if obj.total_pizza_available >= number:
            obj.pizza_delivery += 1
            obj.total_pizza_available -= number
            dict_pizza_list = obj.return_pizza(number)
            data.append(dict_pizza_list)
        else:
            print(f"{obj.total_pizza_available} and {number}")
    return data


def write_output(obj, data, output_file):
    with open(output_file, 'w') as f:
        f.write(f"{obj.pizza_delivery} \n")
        for i in range(obj.pizza_delivery):
            dictty = data[i]
            key = list(dictty.keys())[0]
            output_idx = ' '.join(str(i) for i in dictty[key][1])
            f.write(f"{key} {output_idx} \n")
