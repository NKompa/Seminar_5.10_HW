from datetime import datetime

def sum_log(data1, data2, data3):
    time=datetime.now().strftime('%H:%M')
    with open('calculator_log.csv', 'a') as file:
        file.write("{}    {} + {} = {} \n". format(time, data1, data2, data3))

def dif_log(data1, data2, data3):
    time=datetime.now().strftime('%H:%M')
    with open('calculator_log.csv', 'a') as file:
        file.write("{}    {} - {} = {} \n". format(time, data1, data2, data3))

def mult_log(data1, data2, data3):
    time=datetime.now().strftime('%H:%M')
    with open('calculator_log.csv', 'a') as file:
        file.write("{}    {} * {} = {} \n". format(time, data1, data2, data3))

def div_log(data1, data2, data3):
    time=datetime.now().strftime('%H:%M')
    with open('calculator_log.csv', 'a') as file:
        file.write("{}    {} / {} = {} \n". format(time, data1, data2, data3))

def pow_log(data1, data2, data3):
    time=datetime.now().strftime('%H:%M')
    with open('calculator_log.csv', 'a') as file:
        file.write("{}    {} ^ {} = {} \n". format(time, data1, data2, data3))


