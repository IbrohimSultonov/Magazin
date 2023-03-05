class Magazin:
    def __init__(self, madeli, rangi, narxi, xotira):
        self.madeli = madeli
        self.rangi = rangi
        self.narxi = narxi
        self.xotira = xotira
        
    
    def kriditga_olish(self, mudat1, mudat2,):
        print(f"Bizning do'konda {self.madeli} madelli tilifon {mudat1} oy dan {mudat2} oygacha berilad!") 
        print("Xar oylik to'lovingizga atiga 5% qo'shib to'laysiz xurmatli mijoz.")


    @staticmethod
    def malumot():
        print('''
        Bizning do'konda siz:
        1.iPhone
        2.SAMSUNG
        3.Redmi
        4.HUAWEI
        tilifonlarini xarid qilishingiz mumkun!

        ''')
    
class iPhone(Magazin):
     def tilifon(self):
        print(f"{self.rangi} rangli xotirasi: {self.xotira} GB bo'lgan {self.madeli} ning narxi: {self.narxi} $ bizning do'konimizda!")


class samsung(Magazin):
    def tilifon(self):
        print(f"{self.rangi} rangli xotirasi: {self.xotira} GB bo'lgan {self.madeli} ning narxi: {self.narxi} $ bizning do'konimizda!")


class redmi(Magazin):
    def tilifon(self):
        print(f"{self.rangi} rangli xotirasi: {self.xotira} GB bo'lgan {self.madeli} ning narxi: {self.narxi} $ bizning do'konimizda!")

        
class huawei(Magazin):
    def tilifon(self):
        print(f"{self.rangi} rangli xotirasi: {self.xotira} GB bo'lgan {self.madeli} ning narxi: {self.narxi} $ bizning do'konimizda!")
    


redmi = Magazin("Redmi", "Qora", 800, 512)           
samsung = samsung("SAMSUNG", "Havo Rang", 1100, 256)  
huawei = Magazin("HUAWEI", "Qizil", 900, 256)  
iPhone = Magazin("Apple iPhone 14 Pro Max", "Oq", 1200, 512) 


iPhone.kriditga_olish(12, 24)

# Magazin.malumot()

# print(samsung.tilifon())