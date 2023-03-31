import os

def get_usage(p):
    total = os.path.getsize(p)
    if os.path.isdir(p):
        for f in os.listdir(p):
            childp = os.path.join(p, f)
            total += get_usage(childp)
    print(f"{total:<7}", p)
    return total

