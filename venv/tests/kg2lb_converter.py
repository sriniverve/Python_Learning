'''
This program is to take input in KGs & display the weight in pounds
'''

weight_kg = input('Enter your weight in Kilograms:')        #prompt user input
weight_lb = 2.2 * float(weight_kg)                          #1 kg is 2.2 pounds
print('You weight is '+str(weight_lb)+' pounds')
