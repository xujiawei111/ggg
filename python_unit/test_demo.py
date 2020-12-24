# -*-coding:UTF-8 -*-
# def fun(x):
#     return x
# def test_one():
#     assert fun(3)==3 


# 加上类的玩法
class Testgoods():
    def fun(self,x):
        return x
    def test_one(self):
        assert self.fun(3)==5 
good=Testgoods()          
good.test_one()



   