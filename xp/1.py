class Book:
    def __init__(self,book_id,name,author,count,price):
        self.book_id=book_id
        self.name=name
        self.author=author
        self.count=count
        self.price=price

    def __str__(self):
        return f'\nID:{self.book_id},Name:{self.name},Author:{self.author},Count:{self.count},Price:{self.price}'

def faylga_yozish(book_list,filename='books.txt'):
    with open(filename,'w') as f:
        for book in book_list:
            f.write(f'{book.book_id},{book.name},{book.author},{book.count},{book.price}\n')


def fayldan_oqish(filename='books.txt'):
    book_list=[]
    try:
        with open(filename) as f:
            for i in f:
                book_data=i.strip().split(',')
                book=Book(book_data[0],book_data[1],book_data[2],int(book_data[3]),float(book_data[4]))
                book_list.append(book)
    except FileNotFoundError:
        print(f"{filename} not found.")
    return book_list


def kamaytirish(book_list, book_id):
    for book in book_list:
        if book.book_id==book_id:
            if book.count>0:
                book.count-=1
                print(f"'{book.name}'ni counti kamaytirildi.Yengi count:{book.count}")
            else:
                print(f"Book' {book.name}' nomli kitob yoq.")
            return
    print(f"Kitob {book_id} bunaqa ID bilan topilmadi.")
    
def chiqish():
    print("Hayr")
    exit()

def ochirish(book_list,book_id):
    for book in book_list:
        if book.book_id==book_id:
            book_list.remove(book)
            return
    print(f"Kitob {book_id} bunaqa ID bilan topilmadi.")



if __name__=="__main__":
    
    book1=Book('1','Messi','Cristiano',5,25.99)
    book2=Book('2','Pythonni organish','Kimdur',3,40.50)
    book3=Book('3','Salom','Ozodbek',5,55.5)
    book4=Book('4','Futbol','Great Britian',1,32.1)
    book5=Book('5','C#',"Anders Hejlsberg",0,68.9)
    
    book_list=[book1,book2,book3,book4,book5]

    faylga_yozish(book_list)

    fayldan_kitob=fayldan_oqish()
        
    while True:
        menu=int(input("\tQilishiz imkoniyati bolgan narsalar:\n1-Kitobni countini kamaytirish\n2-Kitobni ochirish\n3-Fayldgi narsalarni oqish\n4-Chiqish\nTanlang:"))
        if menu<0 and menu>3:
            print("Notogri son kiritmang!")
            continue
        if menu==1:
            kitob_ID=int(input("\nKamaytirmoqchi bolgan Kitobni IDsini yozing(1dan 5gacha):"))
            if kitob_ID<0 and kitob_ID>5:
                print("Notogri son boshqatdan kiriting!")
                continue
            else:
                kamaytirish(fayldan_kitob,str(kitob_ID))
                m1=int(input("\nDavom etasizmi yoki chiqasizmi?\n1[Davom etish]2[Chiqish]"))
                if m1==1:
                    continue
                elif m1==2:
                    chiqish()
                else:
                    print("Notogri son yozmang")
                    continue
                
        elif menu==2:
            ochir=int(input("\nOchirmoqchi bolgan kitobni IDsini kiriting(1dan 5gacha):"))
            if ochir<0 and ochir>5:
                print("Notogri son kiritdingiz!")
                continue
            else:
                ochirish(fayldan_kitob,str(ochir))
                m2=int(input("\nDavom etasizmi yoki chiqasizmi?\n1[Davom etish]2[Chiqish]"))
                if m2==1:
                    continue
                elif m2==2:
                    chiqish()
                else:
                    print("Notogri son yozmang")
                    continue
                
        elif menu==3:
            print("Fayldan oqilgan kitoblar:")
            for i in fayldan_kitob:
                print(i)
            m3=int(input("\nDavom etasizmi yoki chiqasizmi?\n1[Davom etish]2[Chiqish]"))
            if m3==1:
                continue
            elif m3==2:
                chiqish()
            else:
                print("Notogri son yozmang")
                continue
                
        elif menu==4:
            chiqish()
    
        
        faylga_yozish(fayldan_kitob)
