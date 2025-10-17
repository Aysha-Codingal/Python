def flipflop(tuple1):
    s = 0
    e = len(tuple1) - 1
    while s < e:
        if tuple1[s] != tuple1[e]:
            return False
        s+=1
        e-=1
    return True

tuple1 = (1,2,3,3,2,1)
flag = flipflop(tuple1)

if flag:
    print("the given tuple is a flip flop")
else:
    print("the given flip flop is not a flip flop ")