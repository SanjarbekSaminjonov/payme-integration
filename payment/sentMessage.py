from requests import get

from environs import Env

env = Env()
env.read_env()


def sent_message(order):
    token = env.str('BOT_TOKEN')

    chat_id = env.str('CHAT_ID')

    text = f'{order.id} - raqamli to\'lov amalga oshirildi ************ ' \
           f'{order.place_name} uchun {order.number_of_people} ta odamga to\'lov qilindi ************ ' \
           f'Summa miqdori: {order.amount} so\'m ************ ' \
           f'Xaridor: {order.customer_full_name} ************ ' \
           f'Telefon raqami: {order.customer_phone_number} ************ ' \
           f'Pasport seriyasi va raqami: {order.customer_passport}'

    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    try:
        _ = get(url)
    except:
        print('Telegramga ma\'lumot jo\'natishda xatolik')
