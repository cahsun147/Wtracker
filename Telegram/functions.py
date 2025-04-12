from dotenv import load_dotenv
import os
import requests

# Memuat variabel lingkungan dari file .env
load_dotenv()

async def send_telegram_message(swap_infos: dict):
    """
    Posts a Telegram message containing all the swap informations using the TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID specified in .env/.env
    
    Parameters:
        ``swap_infos (dict)``: dictionary containing all the informations from the swap, e.g. tokens names, amounts swapped, transaction link...
    """
    
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    if not bot_token or not chat_id:
        print("[!] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID is not set in the .env file.")
        return  # Menghentikan eksekusi jika token tidak ada

    message = (
        f"✨ <a href='{swap_infos['LINKS']['SCAN']['TRANSACTION']}'>{swap_infos['CHAIN']} - {swap_infos['MAKER_INFOS']['SHORT_ADDRESS']}</a>\n" +
        f"👤 <a href='{swap_infos['LINKS']['SCAN']['MAKER']}'>{swap_infos['MAKER_INFOS']['SHORT_ADDRESS']}</a>\n" +
        f"📜 <a href='{swap_infos['LINKS']['SCAN']['TRANSACTION']}'>TX</a>\n\n"
    )
    for swap_id, swap_infos in swap_infos['SWAPS'].items():
        emoji_swap_id = await get_emoji_swap_id(swap_id=swap_id)
        message += (
            f"{emoji_swap_id} SWAP {swap_infos['SYMBOLS']['TOKEN0']} » {swap_infos['SYMBOLS']['TOKEN1']}\n" +
            f"• 💵 {swap_infos['AMOUNTS']['TOKEN0']} ${swap_infos['SYMBOLS']['TOKEN0']} » {swap_infos['AMOUNTS']['TOKEN1']} ${swap_infos['SYMBOLS']['TOKEN1']}\n" +
            f"• 📊 <a href='{swap_infos['LINKS']['CHART']}'>CHART/TRADING</a>\n"
        )
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    try:
        requests.post(url=url, data={"chat_id": chat_id, "text": message, "parse_mode": "HTML"})
    except Exception as e:
        print(f"[!] Couldn't send Telegram message: {e}")


async def get_emoji_swap_id(swap_id: int) -> str:
    """
    Returns an emoji for the swap ID.
    
    Parameters:
        ``swap_id (int)``: id of the swap
    """
    
    swap_id_emoji = (
        "1️⃣" if swap_id == 1 else
        "2️⃣" if swap_id == 2 else
        "3️⃣" if swap_id == 3 else
        "4️⃣" if swap_id == 4 else
        "5️⃣" if swap_id == 5 else
        "6️⃣" if swap_id == 6 else
        "7️⃣" if swap_id == 7 else
        "8️⃣" if swap_id == 8 else
        "9️⃣" if swap_id == 9 else
        "1️⃣0️⃣" if swap_id == 10 else
        "1️⃣1️⃣" if swap_id == 11 else
        "1️⃣2️⃣" if swap_id == 12 else
        "1️⃣3️⃣" if swap_id == 13 else
        "1️⃣4️⃣" if swap_id == 14 else
        "1️⃣5️⃣" if swap_id == 15 else
        "1️⃣6️⃣" if swap_id == 16 else
        "1️⃣7️⃣" if swap_id == 17 else
        "1️⃣8️⃣" if swap_id == 18 else
        "1️⃣9️⃣" if swap_id == 19 else
        "2️⃣0️⃣" if swap_id == 20 else
        "🔢"
    )
    return swap_id_emoji