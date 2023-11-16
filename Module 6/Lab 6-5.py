def unite_lists(list1, list2):
    united_list = []
    for element in list1:
        if element not in united_list:
            united_list.append(element)
    for element in list2:
        if element not in united_list:
            united_list.append(element)
    return united_list

# Test your code here
if __name__ == '__main__':
    print(unite_lists([2,4,6,8],[3,6,9,12]))
