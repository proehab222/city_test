#TRX_TRY  mean Top Right x , Top Right y
#BLX_BLY mean Buttom Left x , Buttom Left y

import  csv

city_data=[]
top_L_xy=[]  #to store city border
buttom_R_xy=[]  #to store city border

point_data=[] #to store point data from csv file  id ,x,y

#--------------------get city from csv file-------------------------
filePath="cities.csv"
with open(filePath,"r") as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader)
    for row in spamreader:
         city_data.append(row[0])  #city name
         top_L_xy.append([int(row[1]),int(row[2])])  #TopLeft_X  TopLeft_Y
         buttom_R_xy.append([int(row[3]),int(row[4])]) #BottomRight_X BottomRight_Y
csvfile.close()
#--------------------get point from csv file-------------------------
filePath="points.csv"
with open(filePath,"r") as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader)
    for row in spamreader:

        point_data.append([row[0],int(row[1]),int(row[2])])

csvfile.close()


#-----------------fun to check point if within city -------------------------------
def check_city_is(TLX_TLY,BRX_BRY,city_name,point):
    TRX_TRY = [BRX_BRY[0], TLX_TLY[1]]
    BLX_BLY = [TLX_TLY[0], BRX_BRY[1]]

    if((point[1] >= TLX_TLY[0] and point[1] <=TRX_TRY[0])
      and (point[2] >= TLX_TLY[1] and point[2]<= BLX_BLY [1])  ):

        return city_name


    return "None"
#--------------------------------------------------------------------------------

# city_data=[]
# top_L_xy=[]
# buttom_R_xy=[]
# point_data=[]
#check_city_is(TLX_TLY,BRX_BRY,city_name,point):


for point in point_data:
    i = 0
    found="None"
    while (i< len(city_data) and found=="None" ):
      found=check_city_is(top_L_xy[i], buttom_R_xy[i],city_data[i],point)
      i+=1
    if (found=="None"):
     print ("Point ",point," is not found")
    else:
     print("Point ",point ," is found in city",found)









