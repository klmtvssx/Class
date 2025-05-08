class Store:
    def __init__(self,summa):
        self.summa=summa
    def x(self):
        if self.summa > 10000:
            print(f'сизге скидка 1000 сом {self.summa-1000}')
        elif self.summa > 5000:
            print(f'сизге скидка {self.summa-500}')
        elif self.summa<5000 and self.summa>2000:
            print(f'сизге скидка менен {self.summa-200}')
store=Store(16000)
store.x()