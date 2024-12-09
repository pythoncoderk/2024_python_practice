class employee:
    def make(self, make, num, name, arr):
        arr.append([num, name])
        return arr

    def getnum(self, num, dic):
        return dic[int(num)]

    def getname(self, num):

l = []
em = employee()
print(em.make("make", "2742", "mako", l))