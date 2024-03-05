#Вывести на экран таблицу из 4 строк: три товара и сумма без использования цикла
milk   = int(input('Количество бутылок молока'))
potato = int(input('сколько кг картошки'))
bread  = int(input('количество батонов'))
print('') #Чтобы была пустая строка 
milk_cena   = 60
potato_cena = 30
bread_cena  = 80
pay_milk   = milk_cena * milk
pay_potato = potato_cena * potato
pay_bread  = bread_cena * bread 
total = pay_milk + pay_potato + pay_bread 
print('Навзание товара','Количество','Цена',sep=' '*5)
print('Молоко',' '*18 ,milk,' '*7 ,pay_milk, end='\n')
print('Картошка',' '*16 ,potato,' '*7 ,pay_potato, end='\n')
print('Хлеб',' '*20,bread,' '*7 ,pay_bread,end='\n')
print ('Всего к оплате:',total,sep=' '*21)

#не понял как сделать с циклом while
