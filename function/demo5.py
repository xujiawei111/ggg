# -*-coding:UTF-8 -*-
def is_leap_year(start,end,qqq):
    total=0
    year_list=[]
    for i in range(start,end,):
        if i%4==0:
            year_list.append(i)
            total=total+1
            if total==qqq:
                break
    return year_list
year=is_leap_year(2030,4000,20)
print("你的闰年：%s" %year)
