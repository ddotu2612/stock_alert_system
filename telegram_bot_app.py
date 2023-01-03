import os
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    ConversationHandler,
    filters
)
from vnstock import *

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Get stock price from ticket
def get_price_change(ticker):
    start_date = '2022-11-01'
    end_date = '2022-11-02'
    try:
        df =  stock_historical_data(symbol=ticker, start_date=start_date, end_date=end_date)
    except:
        df = f'No data for ticker {ticker}'
    
    return df


def get_px_change(update: Updater, context: CallbackContext, ticker: str = None,):
    
    ticker = update.message.text.split("/get_px_change")[1].strip()

    df = get_price_change(ticker)
    time = df.iloc[0]['TradingDate']
    close = df.iloc[0]['Close']
    message = f'Close Price date {time} is {close}'

    update.message.reply_text(message)

def main() -> None:
    updater = Updater(TOKEN)

    # get dispatcher to register handler
    dispatcher = updater.dispatcher

    # add handler
    dispatcher.add_handler(CommandHandler("get_px_change", get_px_change))

    # start the bot
    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()









