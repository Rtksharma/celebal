def solve(s):
    ipstr = s.split(" ")
    name = ""
    for a in ipstr:
        name += a.capitalize() + " "
    return name
