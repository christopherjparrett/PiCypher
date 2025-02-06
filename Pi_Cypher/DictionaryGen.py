import random
import time
random.seed(time.time())
Items = "1234567890"
x=0
print("\\{")
print()
print()
print()
print()
while(x<10):
    ListOfItems = [x  for x in Items]
    ListOfItemsTwo = [ x  for x in Items]
    i=0
    lengthOfItems = len(ListOfItems)
    print("TempDictionary = {",end='')
    secondList = "TempDictionary = {"
    while(len(ListOfItemsTwo)>0):
        SlotUsed = random.randint(1,lengthOfItems-i)-1
        print( "'" + ListOfItems[i] + "'" + ": '"+ ListOfItemsTwo[SlotUsed] + "',",end='')
        secondList += ("'" + ListOfItemsTwo[SlotUsed]+ "'" + ": '"+ ListOfItems[i] + "',")
        ListOfItemsTwo.pop(SlotUsed)
        i+=1
    print("}")
    print("NumberList.append(TempDictionary)")
    secondList+=("}")
    print(secondList)
    print("InverseNumberList.append(TempDictionary)")
    x+=1
