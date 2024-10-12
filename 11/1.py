class Dori:
    def __init__(self, nomi, narxi, kompaniya, srok, tasir):
        self.nomi=nomi
        self.narxi=narxi
        self.kompaniya=kompaniya
        self.srok=srok
        self.tasir=tasir

    def __repr__(self):
        return f"Dori(nomi={self.nomi},narxi={self.narxi},kompaniya={self.kompaniya},srok={self.srok},tasir={self.tasir})"


class Apteka:
    def __init__(self,nomi):
        self.nomi=nomi
        self.kassa=100000
        self.dorilar={
            "Aspirin":{
                "narxi":20000,
                "soni":20,
                "kompaniya":"PharmaCo",
                "srok":"2025-12",
                "tasir":"Bosh og'rig'i"
            }
        }

    def dori_append(self, dori_obj):
        if dori_obj.nomi in self.dorilar:
            self.dorilar[dori_obj.nomi]['soni']+=1
        else:
            self.dorilar[dori_obj.nomi]={
                "narxi":dori_obj.narxi,
                "soni":1,
                "kompaniya":dori_obj.kompaniya,
                "srok":dori_obj.srok,
                "tasir":dori_obj.tasir
            }
        print(f"{dori_obj.nomi} dorisi qo'shildi yoki yangilandi.")

    def dori_sotmoq(self, dori_nomi, miqdori):
        if dori_nomi in self.dorilar:
            if self.dorilar[dori_nomi]['soni']>=miqdori:
                umumiy_narx=self.dorilar[dori_nomi]['narxi']*miqdori
                self.kassa+=umumiy_narx
                self.dorilar[dori_nomi]['soni']-=miqdori
                print(f"{miqdori} ta {dori_nomi} sotildi. Jami: {umumiy_narx} so'm.")
            else:
                print(f"{dori_nomi} dan yetarlicha miqdor yo'q!")
        else:
            print(f"{dori_nomi} dorisi topilmadi!")

    def delete(self, dori_nomi):
        if dori_nomi in self.dorilar:
            del self.dorilar[dori_nomi]
            print(f"{dori_nomi} dorisi o'chirildi.")
        else:
            print(f"{dori_nomi} dorisi topilmadi!")

    def ogriq_boyicha_dori_berish(self, ogriq_nomi):
        topilgan_dorilar = [dori for dori, info in self.dorilar.items() if info['tasir'] == ogriq_nomi]
        if topilgan_dorilar:
            print(f"{ogriq_nomi} uchun dorilar: {', '.join(topilgan_dorilar)}")
        else:
            print(f"{ogriq_nomi} uchun dori topilmadi.")


apteka = Apteka("Shifo Apteka")

nomi = input("Dorining nomi: ")
narxi = int(input("Dorining narxi: "))
kompaniya = input("Dorining kompaniyasi: ")
srok = input("Dorining srok muddati: ")
tasir = input("Dorining tasiri: ")

yangi_dori = Dori(nomi, narxi, kompaniya, srok, tasir)

apteka.dori_append(yangi_dori)

apteka.dori_sotmoq("Aspirin", 2)

apteka.ogriq_boyicha_dori_berish("Bosh og'rig'i")

apteka.delete("Aspirin")
