import sys
sys.path.insert(0, '../')
import get_pictures
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time



token =''
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)



def create_keyboard(response):
    keyboard = VkKeyboard(one_time=True)

    if response == 'команды':

        keyboard.add_button('Баланс', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Пополнить баланс', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  
        keyboard.add_button('Халява', color=VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Гемы', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Акаунты', color=VkKeyboardColor.PRIMARY)

    elif response =='пополнить баланс':
        keyboard.add_button('Qiwi wallet', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Другой', color=VkKeyboardColor.NEGATIVE)

    elif response == 'начать':
        keyboard.add_button('Команды', color=VkKeyboardColor.POSITIVE)
    elif response == '+':
        keyboard.add_button('Команды', color=VkKeyboardColor.POSITIVE)

    elif response == 'qiwi wallet':
        keyboard.add_button('Как пополнить??', color=VkKeyboardColor.POSITIVE)
    elif response == 'халява':
        keyboard.add_button('Тест', color=VkKeyboardColor.NEGATIVE)
    elif response == 'тест':
        keyboard.add_button('2017 год', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('2014 год', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('2015 год', color=VkKeyboardColor.PRIMARY)
    elif response == '2014 год':
        keyboard.add_button('2017 год', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('2015 год', color=VkKeyboardColor.PRIMARY)
    elif response == '2015 год':
        keyboard.add_button('2017 год', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('2014 год', color=VkKeyboardColor.NEGATIVE)
    elif response == '2017 год':
        keyboard.add_button('Покко', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Кольт', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Леон', color=VkKeyboardColor.PRIMARY)
    elif response == 'Покко':
        keyboard.add_button('Кольт', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Леон', color=VkKeyboardColor.PRIMARY)
    elif response == 'Кольт':
        keyboard.add_button('Покко', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Леон', color=VkKeyboardColor.PRIMARY)




    




    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        print(event.user_id)
        response = event.text.lower()
        keyboard = create_keyboard(response)

        if event.from_user and not event.from_me:
            if response == "котики":
                attachment = get_pictures.get(vk_session, -130670107, session_api)
                send_message(vk_session, 'user_id', event.user_id, message='Держи котиков!', attachment=attachment, keyboard=keyboard)
            elif response == "привет":
                send_message(vk_session, 'user_id', event.user_id, message='Нажми на кнопку, чтобы получить список команд',keyboard=keyboard)
            elif response == "гемы":
                send_message(vk_session, 'user_id', event.user_id, message= 'Промокоды на гемы ты можешь приобрести в нашем магазине - https://vk.com/market-190437731?section=album_2')
            elif response=='команды':
                send_message(vk_session, 'user_id', event.user_id, message='Список команд бота: \n \n Баланс \n Пополнить баланс \n \n Халява \n \n Гемы \n Акаунты',keyboard=keyboard)
            elif response == 'начать':
                send_message(vk_session, 'user_id', event.user_id, message='Приветствую тебя', keyboard=keyboard)
            elif response == '+':
                send_message(vk_session, 'user_id', event.user_id, message='Приветствую тебя', keyboard=keyboard)
            elif response == "акаунты":
                send_message(vk_session, 'user_id', event.user_id, message= 'Аккаунт ты можешь приобрести в нашем магазине - https://vk.com/market-190437731?section=album_1')
            elif response =='пополнить баланс':
                send_message(vk_session, 'user_id', event.user_id, message='Выберите способ оплаты', keyboard=keyboard)
            elif response == 'qiwi wallet':
                send_message(vk_session, 'user_id', event.user_id, message='Отправте нужную сумму на кошелек +79778576316 \n \n Обязательно в комментарий укажите свое Имя и Фамилию', keyboard=keyboard)
            elif response == 'другой':
                send_message(vk_session, 'user_id', event.user_id, message='\n \n https://vk.com/app6887721_-190437731 \n \n Чтобы оплатить,нужно: \n  ➤ Зайти по ссылке. \n  ➤ Нажать "Оплатить" \n  ➤ Ввести сумму стоимости товара \n  ➤ Написать название товара в комментарий \n \n Оплатили? Напишите в этот диалог : "проверить оплату"')
                send_message(vk_session, 'user_id', event.user_id, message='Оплатили? Напишите в этот диалог : "проверить оплату"')
            elif response == 'проверить оплату':
                send_message(vk_session, 'user_id', event.user_id, message='Оплата не пришла. Причины: \n \n ➤ Не скинули деньги \n ➤ Не скинули точную сумму \n \n Если вы все сделали правильно, но баланс не пополнился пиши сюда - https://vk.com/tol79l ')
            elif response == 'баланс':
                send_message(vk_session, 'user_id', event.user_id, message='Ваш баланс составляет: 0.00 рублей \n Чтобы пополнить ваш баланс вы должны перейти по ссылке ниже! \n \n https://vk.com/app6887721_-190437731 \n \n В цене указывать столько денег, на сколько хотите пополнить баланс! \n \n Как только оплатите, вводите команду: "проверить пополнение"')
            elif response == 'халява':
                send_message(vk_session, 'user_id', event.user_id, message='Пройди тест и получи бонус', keyboard=keyboard)
            elif response =='тест':
                send_message(vk_session, 'user_id', event.user_id, message='И так приступим. \n Первый вопрос: \n \n Когда вышла игра Brawl Stars?', keyboard=keyboard)
            elif response == '2017 год':
                send_message(vk_session, 'user_id', event.user_id, message='Ты чертовски прав, второй вопрос: \n \n Кто из них легендарный персонаж из игры Brawl Stars?', keyboard=keyboard)
            elif response == '2014 год':
                send_message(vk_session, 'user_id', event.user_id, message='Неверный ответ,попробуй еще раз.', keyboard=keyboard)
            elif response == '2015 год':
                send_message(vk_session, 'user_id', event.user_id, message='Неверный ответ,попробуй еще раз.', keyboard=keyboard)
            elif response == 'покко':
                send_message(vk_session, 'user_id', event.user_id, message='Неверный ответ,попробуй еще раз.', keyboard=keyboard)
            elif response == 'кольт':
                send_message(vk_session, 'user_id', event.user_id, message='Неверный ответ,попробуй еще раз.', keyboard=keyboard)
            elif response == 'леон':
                send_message(vk_session, 'user_id', event.user_id, message='Поздравляю, \n \n Ты получаешь от нас ПОДАРОК, теперь любой товар в нашем маркете для тебя стоит 39р. \n Что-бы активировать скиду напиши в лс кодовое слово: "изи" \n \n Писать сюда - https://vk.com/tol79l' )
