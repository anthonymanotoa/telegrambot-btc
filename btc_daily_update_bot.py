from bs4 import BeautifulSoup
import requests
import schedule


def bot_send_text(bot_message):
    
    bot_token = 'YOUR_TOKEN'
    bot_chatID = 'YOUR_CHATID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def btc_scraping():
    url = requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})
    format_result = result.text

    return format_result


def report():
    btc_price = f'El precio de Bitcoin es de {btc_scraping()}'
    bot_send_text(btc_price)


if __name__ == '__main__':
        
    schedule.every().day.at("12:34").do(report)

    while True:
        schedule.run_pending()