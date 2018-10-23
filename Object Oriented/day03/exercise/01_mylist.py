
class Mylist(list):
    def insert_head(self, value):
        '''将value值插入到列表前面去
        '''
        self.insert(0, value)


L = Mylist(range(1,5))
print(L) #[1, 2, 3, 4]
L.insert_head(0)
print(L) #[0, 1, 2, 3, 4]
L.append(5)
print(L) #[0,1,2,3,4,5]