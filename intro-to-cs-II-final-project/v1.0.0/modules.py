def linearSearch(array, target) -> list: 
    '''
    Linear Search function that appends each step into a list
    ''' 

    output = []
    n = len(array)
    step = 1
    found = False

    output.append(f'{'Step #':^{20}}{'Index Checked':^{20}}{'Value Checked':^{20}}{'Action':^{20}}')

    for i in range(n): 
        action = None
        if array[i] == target: 
            action = 'Target found'
            output.append(f'{step:^{20}}{i:^{20}}{array[i]:^{20}}{action:^{20}}')
            found = True
            break
        else: 
            action = 'Continue'
            output.append(f'{step:^{20}}{i:^{20}}{array[i]:^{20}}{action:^{20}}')
            step += 1

    if found == True: 
        output.append(f'{'Algorithm succeeds after ' + str(step) + ' steps':^{80}}')
    else: 
        output.append(f'{'Algorithm fails after ' + str(step - 1) + ' steps':^{80}}')

    return output

def binarySearch(array, target):
    '''
    Binary search function that appends each step into a list
    ''' 

    array.sort()
    output = []
    low = 0
    high = len(array) - 1
    step = 1
    found = False

    output.append(f'{"Step #":^{10}}{"Low":^{10}}{"Mid":^{10}}{"High":^{10}}{"Array[Mid]":^{15}}{"Action":^{20}}')

    while low <= high: 
        mid = (low + high) // 2
        action = None
        
        if array[mid] == target: 
            action = 'Target found'
            output.append(f'{step:^{10}}{low:^{10}}{mid:^{10}}{high:^{10}}{array[mid]:^{15}}{action:^{20}}')
            found = True
            break
        elif array[mid] < target: 
            action = 'l = m + 1'
            output.append(f'{step:^{10}}{low:^{10}}{mid:^{10}}{high:^{10}}{array[mid]:^{15}}{action:^{20}}')
            low = mid + 1
        else: 
            action = 'r = m - 1'
            output.append(f'{step:^{10}}{low:^{10}}{mid:^{10}}{high:^{10}}{array[mid]:^{15}}{action:^{20}}')
            high = mid - 1

        step += 1

    if found: 
        output.append(f'{"Algorithm succeeds after " + str(step) + " steps":^{80}}')
    else: 
        output.append(f'{"Algorithm fails after " + str(step - 1) + " steps":^{80}}')

    return output

def bubbleSort(array):
    '''
    Bubble sort function that appends each step into a list with exactly n-1 steps.
    '''
    output = []
    n = len(array)

    output.append(f'{"Original Array":^{20}}{str(array):^{60}}')

    for step in range(n - 1):
        for i in range(n - 1 - step): 
            if array[i] > array[i + 1]: 
                array[i], array[i + 1] = array[i + 1], array[i]
        output.append(f'{"Step " + str(step + 1):^{20}}{str(array):^{60}}')

    output.append(f'{"Array sorted in " + str(n - 1) + " steps":^{80}}')
    return output

def selectionSort(array):
    '''
    Selection sort function that appends each step into a list with exactly n-1 steps.
    '''
    output = []
    n = len(array)

    output.append(f'{"Original Array":^{20}}{str(array):^{60}}')

    for step in range(n - 1):
        min_idx = step
        for j in range(step + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        if min_idx != step:
            array[step], array[min_idx] = array[min_idx], array[step]
        output.append(f'{"Step " + str(step + 1):^{20}}{str(array):^{60}}')

    output.append(f'{"Array sorted in " + str(n - 1) + " steps":^{80}}')
    return output

def insertionSort(array):
    '''
    Insertion sort function that appends each step into a list with exactly n-1 steps.
    '''
    output = []
    n = len(array)

    output.append(f'{"Original Array":^{20}}{str(array):^{60}}')

    for step in range(1, n): 
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        output.append(f'{"Step " + str(step):^{20}}{str(array):^{60}}')

    output.append(f'{"Array sorted in " + str(n - 1) + " steps":^{80}}')
    return output
