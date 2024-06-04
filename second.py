def average(array):
    totalsum=sum(set(array))
    x=len(set(arr))
    
    avg = float(totalsum) / x
    return round(avg, 3)
