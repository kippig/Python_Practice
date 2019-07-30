from datetime import datetime

def triangle(row):
    COLOUR_DICT = {('R', 'R'): 'R', ('B', 'B'): 'B', ('G', 'G'): 'G',
                   ('R', 'G'): 'B', ('R', 'B'): 'G',
                   ('B', 'G'): 'R', ('B', 'R'): 'G',
                   ('G', 'R'): 'B', ('G', 'B'): 'R'}

    while len(row) > 1:
        print(row)
        if len(row) % 1000 == 0: print(len(row))
        row = ''.join(COLOUR_DICT[x] for x in zip(row, row[1:]))


    return row

t = datetime.now()
print(triangle('RGBRBRGRGBRBR'))
print("Process ran in {}".format(datetime.now()-t))


{'RGG': 'R', 'GGR': 'R', }
