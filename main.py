from pyqrcode import QRCode
import pyqrcode

from pyfiglet import Figlet

def ShowMenu():
    print(' 1-Add product \n 2-Edit product \n 3-Delete product \n 4-Search \n 5-show_list \n 6-buy \n 7-saveandexit \n 8-QR code')
products =[]

def load_product():
    f= open ('database.txt', 'r')
    print('loading...')
    
    big_text= f.read
    rows = big_text.split('\n')
    for i in range(len(rows)):
         info = rows[i].split(',')
         products.append = {'id':int(info[0]),'name': info[1], 'price': float(info[2]), 'count':int(info[3])}
    f.close()
    print('program is ready to use!')
         
def AddProduct():
    id = int(input('please enter id:'))
    name = input('please enter name:')
    price = float(input('please enter price:'))
    count = int(input('please enter count:'))
    products.append({'id': id, 'name': name, 'price': price, 'count':count})
    print('new product added!')
    
   
def show_edit_menu():
    print('1-name ')
    print('2-price')
    print('3-count')
    print('4-end edit')
     

def EditProduct():
    id = int(input('please enter product id:'))
    
    for i in range(len(products)):
        if products[i]['id']==id:
           while True:
             show_edit_menu()
            
             choice = int(input('please choose from edit menu:'))
             
             if choice == 1:
                products[i]['name'] = input('please enter new name:')
                 
             elif choice == 2:
                 products[i]['price'] = float(input('please enter new price:'))
                 
             elif choice == 3:
                products[i]['count'] = int(input('please enter new count:')) 
                
             elif choice == 4:
                 break
             else:
                 print('error value!!')
                 
    
    
def DeleteProduct():
    id = int(input('please enter product id :'))
    for i in range(len(products)):
        if products[i]['id']== id:
            products.pop(i)
            print('product removed')
            break
        
    

def Search():
    user_keyword = input('please enter id or name:')
    for i in range(len(products)):
         if products[i]['name'] == user_keyword or str(products[i]['id'])== user_keyword:
             
          print(products[i])
    
    

def buy():
    basket= []
    while True:
        id = int(input('please enter product id:'))
        
        for i in range(len(products)):
            if products[i]['id']==id:
                count= int(input('please enter count:'))
                
                if products[i]['count']>=count:
                    basket.append({'name': products[i]['name'],'price': products[i]['price']})
                    products[i]['count'] -= count
                    print('product added to basket')
                    
                else:
                    print('not exist')
                    print('we have', products[i]['count'], 'from this products')
        choice = input('do you want to continue? (y/n)')
         
        if choice == 'n' or 'N':
            break
        
    print(basket)
    total_price = 0
    for i in range(len(basket)):
        total_price +=basket[i]['price']*basket[i]['count']
        print('total price is:', total_price)
        print('tnx')
        
def saveandexit():
    f = open('database.txt', 'w')
    
    for i in range(len(products)):
        row = str(products[i]['id'])+','+ products[i]['name']+','+ str(products[i]['price'])+','+str(products[i]['count']+ '\n')
        
        f.write(row)
    f.close()
    exit 
    
def qrcode_id():
    id=int(input('id: '))
    NUMBERl = pyqrcode.create(id)

    
    NUMBERl.svg("myqr.svg", scale=8)
    
    NUMBER1.png('myqr.png', scale=6) 
    
load_product()
    

f = Figlet(font = 'standard')
print(f.renderText('shadi store'))

def show_list():
    for i in range(len(products)):
        print(products[i]['id'], '\t', products[i]['name'],'\t', products[i]['price'],'\t', products[i]['count'],'\t')

while True:

    ShowMenu()

    choice = int(input('Please choose a number : '))

    if choice == 1:
        AddProduct()
    
    elif choice == 2:
        EditProduct()
                
    elif choice == 3:
        DeleteProduct()

    elif choice == 4:
        Search()

    elif choice == 5:
        show_list()

    elif choice == 6:
        buy()
           
    elif choice == 7:
        saveandexit()


    elif choice == 8:
        qrcode_id()
        
        
   
            