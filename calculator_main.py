import calculator_logger
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def Show_Menu(message):
    bot.send_message(message.chat.id, f"Меню:\n1. Сложить\n2. Вычесть\n3. Умножить\n4. Разделить\n5. Возвести в степень")

@bot.message_handler(content_types=['text'])
def Controller(message):
    choice = message.text
    if choice == '1':
        bot.send_message(message.chat.id, 'Введите два числа через пробел')
        bot.register_next_step_handler(message, Get_Sum)
    if choice == '2':
        bot.send_message(message.chat.id, 'Введите уменьшаемое и вычитаемое через пробел')
        bot.register_next_step_handler(message, Get_Difference)
    if choice == '3':
        bot.send_message(message.chat.id, 'Введите два числа через пробел')
        bot.register_next_step_handler(message, Get_Mult)
    if choice == '4':
        bot.send_message(message.chat.id, 'Введите делимое и делитель через пробел')
        bot.register_next_step_handler(message, Get_Division)
    if choice == '5':
        bot.send_message(message.chat.id, 'Введите число и степень через пробел')
        bot.register_next_step_handler(message, Get_Power)

def Get_Sum(message):
    numbers = list(map(float,message.text.split(' ')))
    result = numbers[0] + numbers[1]
    bot.send_message(message.chat.id, result)
    calculator_logger.sum_log(numbers[0], numbers[1], result)
    Show_Menu(message)
    bot.register_next_step_handler(message,Controller)

def Get_Difference(message):
    numbers = list(map(float,message.text.split(' ')))
    result = numbers[0] - numbers[1]
    bot.send_message(message.chat.id, result)
    calculator_logger.dif_log(numbers[0], numbers[1], result)
    Show_Menu(message)
    bot.register_next_step_handler(message,Controller)

def Get_Mult(message):
    numbers = list(map(float,message.text.split(' ')))
    result = numbers[0] * numbers[1]
    bot.send_message(message.chat.id, result)
    calculator_logger.mult_log(numbers[0], numbers[1], result)
    Show_Menu(message)
    bot.register_next_step_handler(message,Controller)

def Get_Division(message):
    numbers = list(map(float,message.text.split(' ')))
    result = numbers[0] / numbers[1]
    bot.send_message(message.chat.id, result)
    calculator_logger.div_log(numbers[0], numbers[1], result)
    Show_Menu(message)
    bot.register_next_step_handler(message,Controller)

def Get_Power(message):
    numbers = list(map(float,message.text.split(' ')))
    result = pow(numbers[0],numbers[1])
    bot.send_message(message.chat.id, result)
    calculator_logger.pow_log(numbers[0], numbers[1], result)
    Show_Menu(message)
    bot.register_next_step_handler(message,Controller)

bot.polling(none_stop=True, interval=0)