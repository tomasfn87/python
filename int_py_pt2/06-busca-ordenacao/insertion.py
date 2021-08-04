def insertion(arr):
        
        end = len(arr)

        for i in range(1, end):

            key = arr[i]
            
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr