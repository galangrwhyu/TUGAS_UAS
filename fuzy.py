
class BentukMeja():
    kotak = 40
    bulat = 20
    persegipanjang = 60

    def turun(self, x):
        if x <= self.kotak:
            return 0
        elif x >= self.bulat:
            return 1
        else:
            return bawah(x, self.bulat, self.kotak)

    def pas(self, x):
        if self.kotak < x < self.bulat:
            return atas(x, self.kotak, self.bulat)
        elif self.bulat < x < self.persegipanjang:
            return bawah(x, self.bulat, self.persegipanjang)
        elif x == self.bulat:
            return 1
        else:
            return 0

    def naik(self, x):
        if x >= self.bulat:
            return 1
        elif x <= self.persegipanjang:
            return 0
        else:
            return up(x, self.persegipanjang, self.bulat)

class BahanMeja():
    kayu = 30
    besi = 40
    plastik = 20

    def sedikit(self, x):
        if x >= self.kayu:
            return 0
        elif x <= self.besi:
            return 1
        else:
            return down(x, self.besi, self.kayu)
    
    def cukup(self, x):
        if self.kayu < x < self.besi:
            return up(x, self.halus, self.besi)
        elif self.besi < x < self.plastik:
            return down(x, self.besi, self.plastik)
        elif x == self.besi:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.plastik:
            return 1
        elif x <= self.besi:
            return 0
        else:
            return up(x, self.besi, self.plastik)

class WarnaMeja():
    putih = 30
    hitam = 20
    Coklat = 40

    def sedikit(self, x):
        if x >= self.hitam:
            return 0
        elif x <= self.putih:
            return 1
        else:
            return down(x, self.putih, self.hitam)
    
    def cukup(self, x):
        if self.putih < x < self.hitam:
            return up(x, self.hitam, self.putih)
        elif self.putih < x < self.coklat:
            return down(x, self.putih, self.coklat)
        elif x == self.putih:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.coklat:
            return 1
        elif x <= self.putih:
            return 0
        else:
            return up(x, self.putih, self.coklat)

class UkiranMeja():
    naga = 50
    daun = 20
    burung = 30
   
    def sedikit(self, x):
        if x >= self.daun:
            return 0
        elif x <= self.naga:
            return 1
        else:
            return down(x, self.naga, self.daun)
    
    def cukup(self, x):
        if self.naga < x < self.daun:
            return up(x, self.naga, self.daun)
        elif self.burung < x < self.burung:
            return down(x, self.daun, self.burung)
        elif x == self.daun:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.burung:
            return 1
        elif x <= self.daun:
            return 0
        else:
            return up(x, self.daun, self.burung)
