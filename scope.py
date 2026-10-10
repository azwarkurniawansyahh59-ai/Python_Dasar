# Scope Variabel (scope.py) #
x = "global"

def tes():
    x = "lokal"
    print(x)  # hanya di dalam tes()

tes()
print(x)
