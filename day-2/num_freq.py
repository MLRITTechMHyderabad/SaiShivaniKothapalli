def count_freq():
    nums = input("Enter numbers: ").split()
    freq_dict = {}
    for i in nums:
        i = int(i) 
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1 
    return freq_dict
print(count_freq())
