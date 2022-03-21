#Author: TienDong2k and Vuong Truong Son
#Date : 20-03-2021
def f2():
  sec = int(input("Enter seconds: "))
  m, s = divmod(sec, 60)
  h, m = divmod(m, 60)
  #New issue in task2.py
  return "{:02d}:{:02d}:{:02d}".format(h, m, s)