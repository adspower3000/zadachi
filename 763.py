from copy import deepcopy

# def can_greet(s):
#     hello = "hello"
#     i = 0
#     for char in s:
#         if char == hello[i]:
#             i += 1
#             if i == len(hello):
#                 return "YES"
#     return "NO"
#
#
# print(can_greet("ahhellllloou"))


# def update_dict(key, value, defaults={}):
#     defaults[key] = value
#     print(defaults)
#
#
# update_dict(key='fruit', value='apple')
#
# update_dict(key='car', value='ferrari')
# update_dict(key='car1', value='ferrari')
# update_dict(key='car2', value='ferrari')
# update_dict(key='vegetable', value='tomato', defaults={'tree': 'oak'})
# update_dict(key='car3', value='ferrari')


# def update_dict(key, value, defaults=None):
#     if defaults is None:
#         defaults = {}
#     defaults[key] = value
#     print(defaults)
#
# p = update_dict(key='fruit', value='apple')
# p = update_dict(key='vegetable', value='tomato', defaults={'tree': 'oak'})
# p = update_dict(key='car', value='ferrari')

# first_list = [[0, 1, 2], [3, 4, 5]]
# second_list = list(first_list)
# first_list.append([6, 7, 8])
# first_list[1][0] = 9
#
# print(first_list)
# print(second_list)

# def multipliers():
#     return [lambda x: i * x for i in range(4)]

def multiplier(x, i):
    return i * x

def multipliers(x):
    return [multiplier(x, i) for i in range(4)]

print([m(2) for m in multipliers()])

sdasdasdSDS
