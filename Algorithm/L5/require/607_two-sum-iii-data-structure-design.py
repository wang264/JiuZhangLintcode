class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.dic = dict()
        self.nums = list()
    def add(self, number):
        # write your code here
        self.nums.append(number)
        if number in self.dic.keys():
            self.dic[number] += 1
        else:
            self.dic[number] = 1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        # special case, two same number add together for that sum
        for num_1 in self.nums:
            num_2 = value - num_1
            # special case, two same number add together for that sum
            if num_1 == num_2:
                if num_1 in self.dic.keys() and self.dic[num_1] >= 2:
                    return True
            else:
                if num_2 in self.dic.keys():
                    return True
        return False