def target_sum(arr, sum):
    s = set()

    for i in range(0, len(arr)):
        temp = sum-arr[i]
        if(temp in s):
            print(str(sum) + ": " + str(arr[i]) + ", " + str(temp))
            s.add(arr[i])
