# Wtracker
notifications whenever a wallet executes a swap on an EVM-compatible blockchain  Topics
<h1 align="center">
🔎 Wallet Trades Tracker 🔍
<img src="images/img1.png"/>
</h1>

---

<p align="center">
    <img src="https://img.shields.io/github/stars/cahsun147/Wtracker">
    <img src="https://img.shields.io/github/forks/cahsun147/Wtracker">
    <br>
    <img src="https://img.shields.io/github/issues/cahsun147/Wtracker">
    <img src="https://img.shields.io/github/issues-closed/cahsun147/Wtracker">
    <br>
    <img src="https://img.shields.io/github/languages/top/cahsun147/Wtracker">
    <img src="https://img.shields.io/github/last-commit/cahsun147/Wtracker">
    <br>
</p>

# 📖 Introduction
**Wallet Trades Tracker** is a Python tool that allows you to get notifications when a wallet from the list make a trade.
At this moment, **the tool only supports Ethereum** but it's probably working with others EVM-compatible blockchain.

# ⚠️ Disclaimer
**Please note that I'm not responsible for any loss of funds, damages, or other libailities resulting from the use of this software or any associated services.<br>
This tool is provided for educational purposes only and should not be used as financial advice, it is still in expiremental phase so use it at your own risk.**

## How it works 🔬
Each EVM-compatible blockchain bot will **scan every new block** to find wallets **matching those in the `wallets.txt`** file.
Upon finding a match, it will **check if the transaction is a swap**, if so, it will then **notify this transaction using Discord and Telegram**.

## Features ✨
- **Real-time monitoring**: Tracking each new swaps from any DEXs
- **Wallet filtering**: Allowing users to specify which wallets to track
- **Instant notification**: Sending real-time alerts via Discord, Telegram, or other platforms
- **Transaction analysis**: Providing details about transactions such as amounts, involved addresses, exchanged tokens...

## Requirements 📄

To run the tool, you will **need these packages**
- `web3` (interacting with EVM-compatible blockchain)
- `multicall` (for making multi RPC calls)
- `discord.py` (to create an embed for each notification)
- `python-dotenv` (for managing environment variables in Python applications)

## Installation 🛠️

1. Clone this repository: `git clone https://github.com/cahsun147/Wtracker.git`
2. Create a virtual environnment : `python -m venv venv`
3. Install the required packages: `pip install -r requirements.txt`
4. Populate these variables located in .env file located in the main directory.
```python
DISCORD_WEBHOOK_URL=""
TELEGRAM_BOT_TOKEN=""
TELEGRAM_CHAT_ID=""
```
4. Edit `wallets.txt` with your own wallets to track<br>Format: BLOCKCHAIN:ADDRESS (e.g.:ETHEREUM:0xae2fc483527b8ef99eb5d9b44875f005ba1fae13)
5. Start the tool with `python run.py`

## Known issues 🚩

`ImportError: cannot import name 'getargspec' from 'inspect'` : you need to uninstall web3 and install it again in order to update it.



# 📝 TO-DO
- [ ] Integrate others EVM-compatible blockchains


## License 🧾

This project is licensed under the MIT license. Feel free to edit and distribute this template as you like.<br>
See [LICENSE](LICENSE) for more information.
