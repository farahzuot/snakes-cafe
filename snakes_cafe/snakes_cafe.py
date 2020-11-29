intro = "**************************************\n**    Welcome to the Snakes Cafe!   **\n**    Please see our menu below.    **\n**\n** To quit at any time, type \"quit\" **\n**************************************"

print(intro)

menu = {
    'Appetizers' : ['Wings','Cookies','Spring Rolls'],
    'Entrees' : ['Salmon','Steak','Meat Tornado','A Literal Garden'],
    'Desserts' : ['Ice Cream','Cake','Pie'],
    'Drinks' : ['Coffee','Tea','Unicorn Tears']
}

content = ['Wings','Cookies','Spring Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']

def menu_print():
    for i in menu:
        print('\n' + i)
        print('---')
        for j in menu[i]:
            print(j)
    

menu_print()

print(f'\n***********************************\n** What would you like to order? **\n***********************************')
prompt = input('>')
result=[]




while True:
    if (prompt == 'quit'):
        break
    elif prompt in content:
        result.append(prompt)
        counter = result.count(prompt)
        print(f'** {counter} order of {prompt} have been added to your meal **')
        prompt = input('>')
    else: 
        prompt = input('>')

