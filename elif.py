#!/usr/bin/python

h = input('请输入你的身高（m）：')
w = input('请输入你的体重(kg)：')
h = float(h)
w = float(w)
bmi = w/h**2

if bmi >= 32:
    print('您的bmi指数为%.1f，严重肥胖'%(bmi))
elif bmi >= 28:
    print('您的bmi指数为%.1f，肥胖'%(bmi))
elif bmi >= 25:
    print('您的bmi指数为%.1f，过重'%(bmi))
elif bmi >= 18.5:
    print('您的bmi指数为%.1f，正常'%(bmi))
else:
    print('您的bmi指数为%.1f，过轻'%(bmi))