# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the values
# defined below.    
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second

print (1*100) # метр в сантиметр
print (1*(1/1000000000)) # секунда в наносекунду
print (299792458 * 100 * 1/1000000000) # результат должен быть не целым числом, если результат получается целым - значит нужно поставить (1.0/1000000000), тогда ответ будет максимально точным