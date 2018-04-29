# Mary McHale, 14th April 2018
# Project based on Iris Data, Working out the mean
# https://docs.python.org/3/tutorial/floatingpoint.html?highlight=significant%20digits for reducing the number of decimal places in the mean

f = open('data/iris.csv' , 'r')
# This opens the file called iris.csv
print("Means are below")
print(" pl   pw   sl   sw")
# pl = short for Petal length
# pw = short for Petal width
# sl = short for Sepal length
# sw = short for Sepal width

c = 0
# sets the record counter to zero at beginning
totpl = 0
totpw = 0
totsl = 0
totsw = 0

# total for each of the 4 header fields
record = ""
while c < 100000:
    record = f.readline()
    if record == "":

        #print("count = ",c)
        #this was a test to ensure that the total of c was in fact 150, otherwise the results of the mean could be wrong
        temp1 = format(totpl/c, ' .1f')
        temp2 = format(totpw/c, ' .1f')
        temp3 = format(totsl/c, ' .1f')
        temp4 = format(totsw/c, ' .1f')
        print (temp1, temp2, temp3, temp4)
       
        f.close()
        quit()

    # Working out the number of characters across each row to put the data into columns
    petallength = (record[0:3])
    petalwidth = (record[4:7])
    sepallength = (record[8:11])
    sepalwidth = (record[12:15])
    name = (record[16:30])
    
    petallength = float(petallength) 
    petalwidth = float(petalwidth)
    sepallength = float(sepallength)
    sepalwidth = float(sepalwidth)
    #float is a python function to change a string variable into a decimal number for adding purposes
    
    totpl = totpl + petallength
    totpw = totpw + petalwidth
    totsl = totsl + sepallength
    totsw = totsw + sepalwidth

    #print(petallength, petalwidth, sepallength, sepalwidth)
    record = ""
    c = c + 1