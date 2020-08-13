# 607. Two Sum III - Data structure design
# 中文English
# Design and implement a TwoSum class. It should support the following operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
# Example
# Example 1:
#
# add(1); add(3); add(5);
# find(4) // return true
# find(7) // return false


class TwoSum2:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.number_to_occourance = dict()
        self.numbers = list()

    def add(self, number):
        self.numbers.append(number)
        if number in self.number_to_occourance.keys():
            self.number_to_occourance[number] += 1
        else:
            self.number_to_occourance[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for num_1 in self.numbers:
            num_2 = value - num_1
            if num_2 == num_1:
                if num_1 in self.number_to_occourance.keys() and self.number_to_occourance[num_1] >= 2:
                    return True
            else:
                if num_1 in self.number_to_occourance.keys() and num_2 in self.number_to_occourance.keys():
                    return True
        return False


ts = TwoSum2()
ts.add(2)
ts.add(3)
ts.find(4)
ts.find(5)
ts.find(6)
ts.add(3)
ts.find(6)
