input = open("input.txt",'r').read().strip().split('\n')
input = [[int(u) for u in interval.split('-')] for interval in input]

def mergeIntervals(arr):
    if len(arr)==0: return arr
    # Sorting based on the increasing order of the start intervals
    arr.sort(key=lambda x: x[0])
    # Stores index of last element in output array
    out = [arr[0]]
    print(out)
    # Traverse all input Intervals starting from second interval
    for i,(u,v) in enumerate(arr[1:]):
        x,y = out[-1]
        # If this is not first Interval and overlaps with the previous one,
        if y >= u:
            # Merge previous and current intervals
            out[-1] = (x,max(v,y))
        else:
            out.append([u,v])
    return out

out = mergeIntervals(input)
print(out)
if out[0][0]<=1:
    print(out[0][1]+1)
else:
    print(1)
