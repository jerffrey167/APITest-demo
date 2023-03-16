
class Test_01:

    def add(self,x,y):
            c = x + y
            return c

    def test_001(self):
        a = 1
        b = 2
        assert self.add(a,b) == 4 , '当前传入的a值：%s，传入的b值：%s' %(a,b)

