# Задача с игрой и подсчетом баллов за слово
def cost(symb):
    return [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10][ ord( symb.lower() ) - ord('a') ]

print( sum( cost(x) for x in list( input( '-> ' ) ) ) )
