#print xuv 700- position 3, black,capacity- 7, no. of cylinder-4
#print swift - position 1, blue,capacity- 5, no. of cylinder-2
#print tata safari- position 2, red,capacity-3, no. of cylinder- 3


class CarBrand:
   def __init__(self,color,capacity,position):
      self.color = color
      self.capacity = capacity
      self.position = position
   def print_clr_cap1(self):
        print(self.color,self.capacity)
   def print_clr_cap(self):
       print(self.position)

xuv_700 = CarBrand("black",7,1)
swift = CarBrand("blue",4,2)
tata_safari = CarBrand("red",3,3)

xuv_700.print_clr_cap1()
swift.print_clr_cap1()
tata_safari.print_clr_cap1()

xuv_700.print_clr_cap()
swift.print_clr_cap()
tata_safari.print_clr_cap()


