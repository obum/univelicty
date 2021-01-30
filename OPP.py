class DescribeList(list):
    def descirbe(self):
        length = len(self)
        first = self[0]
        last = self[-1]
        
        return f'{self} has {length} length, \nThe first character is {first} \nThe last character {last}'
    
    
new_list = DescribeList([2, 3, 5, 6, 0])

print(new_list.descirbe())