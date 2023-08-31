#Design a modular program that asks the user to enter a distance in kilometers, and then converts that distance to miles. The conversion formula is as follows: miles= km * 0.6214 
ktomiles=0.6214
def main():
    kilometers=int(input('enter distance in km: '))
    print ('the distance entered converted to miles is:')
    print (float(kilometers * ktomiles))
    
main()