def print_rangoli(size):
    
    # your code goes here
    az = [chr(i) for i in range(97, 123)]
    c = list(reversed(az[:size]))
    t, w, u = [], [], []
    r = (4*size)-3
    for j in range(size):
        
        t.append(c[j])
        w = t.copy()
        w.pop()
        w = list(reversed(w))
        s = t+w
        q = "-".join(s)
        p = q.center(r, "-")
        u.append(p)
        print(p)
        if j == size-1:
            
            u = list(reversed(u))
            u.pop(0)
            u = "\n".join(u)
            print(u) 

if __name__ == '__main__':
