def ceros_consecutivos(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

print(ceros_consecutivos(5,6,1,0,0,9,3,5)) # True
print(ceros_consecutivos(6,0,5,1,0,3,0,1)) # False