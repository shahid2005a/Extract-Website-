#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\033[1;92m🚀 Installing Website Extractor...\033[0m"

pkg update -y && pkg upgrade -y
pkg install -y python git
pip install requests pyTelegramBotAPI
termux-setup-storage
mkdir -p /storage/emulated/0/Dgtl

echo -e "\033[1;92m✅ Done! Run: python3 bot_extractor.py\033[0m"