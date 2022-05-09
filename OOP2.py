import threading

class Kocka:
    
    def __init__(self):
        print('Unesite duzinu ivice kocke: ')
        self.num=int(input())     #Duzinu stranice kocke odredjena unosom sa tastature
        
    def zapremina(self) :
        
        return('Zapremina kocke je: {} {}'.format(self.num*self.num*self.num,"cm^3"))

    def duzina_stranica(self):

        return('Ukupna duzina stranica kocke je: {} {}'.format(12*self.num,'cm'))    

    def run(self):

        t1=threading.Thread(target=self.duzina_stranica)
        t2=threading.Thread(target=self.zapremina)

        print('done1')

        t1.start()
        t2.start() 

        print('done2')

        t1.join()
        t2.join()

        print('done3')
        

if __name__ == '__main__':
    d = Kocka()
    d.run()
    print(d.zapremina())
    print(d.duzina_stranica())

    
















