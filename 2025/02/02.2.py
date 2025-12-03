inp = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

inp = "4487-9581,755745207-755766099,954895848-955063124,4358832-4497315,15-47,1-12,9198808-9258771,657981-762275,6256098346-6256303872,142-282,13092529-13179528,96201296-96341879,19767340-19916378,2809036-2830862,335850-499986,172437-315144,764434-793133,910543-1082670,2142179-2279203,6649545-6713098,6464587849-6464677024,858399-904491,1328-4021,72798-159206,89777719-90005812,91891792-91938279,314-963,48-130,527903-594370,24240-60212"

def invalid(x : int, y : int):
    """ Return number of invalid numbers incl x and y. A number is invalid if it is made only of some sequence of digits repeated twice. """
    sol = 0
    for v in range(x, y+1):
        vv = str(v)
        n = len(vv)
        for k in divs[n-1]:
            m = n // k
            if not all(vv[0:m] == vv[j*m:(j+1)*m] for j in range(1,k)): continue
            print(f"{vv} is a repetition of {vv[0:m]}")
            sol += v
            break
    return sol

divs = [ [] for _ in range(1,20) ]
ans = 0

for k in range(1,20):
    for m in range(2,k+1):
        if k % m == 0:
            divs[k-1].append(m)
print(divs)

for it in inp.split(','):
    x,y = it.split('-')
    ans += invalid(int(x),int(y))
print(ans)
