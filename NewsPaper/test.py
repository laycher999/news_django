items = {
'Закалённый в боях процессор насмешек робота ': 3.23,
'Повидавшая битвы денежная печь робота ': 3.19,
'Повидавшая битвы KB-808 робота ': 3.28,
'Армированный насос подавления юмора робота ': 0.43,
'Армированный детектор эмоций робота ': 0.39,
'Армированный стабилизатор бомбы робота ': 0.43,
'Неповрежденный валютный желудок робота ': 7.82,
'Неповрежденная мозговая лампа робота ': 7.01
}
str = """
Закалённый в боях процессор насмешек робота x 7
Повидавшая битвы денежная печь робота x 9
Армированный детектор эмоций робота x 3
Армированный стабилизатор бомбы робота x 3
Неповрежденный валютный желудок робота x 3
"""
newdict = {}
def score():
    x = 1
    final = ''
    for item in str.split():
        if item == 'x':
            x = 0
        if item != 'x' and x != 0:
            final += f'{item} '
        if item.isdigit() and x == 0:
            newdict[final] = item
            x = 1
            final = ''
    total_price = 0
    for a, b in newdict.items():
        for item, price in items.items():
            if a in item:
                total_price += int(b) * price

    print(total_price)


score()
