#program to convert decimal number into octal representation
def convert(num,format_type):
    return format(num,format_type)
result=convert(145,'o')
print("octal representation:",result)
#program to calculate the area of a pond and amount of water
r=34
pi=3.14
area=pi*r*r
water=area*1.4
print("area of pond:",int(area),"square meters")
print("total water:",int(water),"litres")
#program to calculate speed in meters per second
distance=490
time=7*60#convert 7 minutes to seconds
speed=distance/time
print("speed:",speed,"meters/second")