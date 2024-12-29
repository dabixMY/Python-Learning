import random

food=['Kuey Teow Grng Ayam', 'Mee Hoon Grng Tom Yam Ayam','Mee Hoon Grng Ayam','Mee Hoon Grng Kpg Ayam','Nasi Grng Ayam','Nasi Grng Cina Ayam','Nasi Goreng Kpg Ayam','Nasi Grng Tom Yum Ayam','Nasi Lemak Ayam']
drinks=['Milo Ais','Milo Nestum Ais','Cham C Ais','Cham Ais','Extra Joss Mango C','Extra Joss Mango','Extra Joss Anggur','Extra Joss Anggur C','Kopi Ais','Kopi C Ais','Horlicks Ais','Nescafe C Ais','Nescafe Ais','Nescafe O Ais','Nestum Ais','Teh C Ais','Teh Ais','Teh O Ais','Syrup Bandung Ais','Syrup Ais','Lychee Ais','Teh O Lychee Ais','Cincau Ais','Teh Ais Cincau','Syrup Bandung Cincau Ice','Nestlo Ais']

repeat = "y"
while repeat.upper() == "y":

    random.shuffle (food)
    random.shuffle (drinks)
    eat=random.choice(food)
    drink=random.choice(drinks)
    print(f'Food  :{eat}')
    print(f'Drinks:{drink}')

    repeat  = input("Regenerate? (y/n) >> ")