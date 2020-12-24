# -*-coding:UTF-8 -*-
#写个程序打印出接下来的20个闰年。
class Animal():

    def __init__(self):
        self.eye = ''
        self.ear = ''

    def chi(self):
        print('动物吃')
    
    def pao(self):
        print('动物跑')


class Cat(Animal):

    def __init__(self):
        self.weiba = None
    def zhua(self):
        print('抓老鼠')
        
    #这个chi覆盖了父类的chi
    def chi(self):
        print('猫咪的吃')


class Bird():
    def fei(self):
        print('我飞飞飞')

class Dog(Cat,Bird):
    #这个chi覆盖了父类的chi
    def chi(self):
        print('我是用啃的')


tom = Cat()
tom.pao()
tom.chi()
tom.weiba='翘'
tom.zhua()

erha = Dog()
erha.ear = '尖尖的'
erha.eye = '蓝色'
erha.chi()
erha.zhua()
erha.fei()
    