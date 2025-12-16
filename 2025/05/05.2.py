def unionSize(intervals):
    # Sort intervals by their start points
    intervals.sort(key=lambda x: x[0])

    merged_intervals = []
    for current_start, current_end in intervals:
        if not merged_intervals or current_start > merged_intervals[-1][1]:
            # No overlap or adjacent, add as a new interval
            merged_intervals.append([current_start, current_end])
        else:
            # Overlap or adjacent, merge with the last interval
            merged_intervals[-1][1] = max(merged_intervals[-1][1], current_end)

    return sum(y - x + 1 for (x,y) in merged_intervals)

sol = 0
ranges = []
for l in open('input.txt','r'):
    l = l.strip()
    if '-' in l:
        x,y = l.split('-')
        ranges.append( (int(x),int(y)) )
    elif len(l) == 0:
        print(unionSize(ranges))
