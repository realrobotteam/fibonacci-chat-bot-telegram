The original README already includes an English version. Here's the preserved English text from the repository:

---

# Gemini_Telegram_Bot  
A Telegram bot using Gemini API.  

## Demo  
[Try the demo here](https://t.me/@Fibonacciaibot)  

## Installation  
### (1) For Linux Systems  
1. Install dependencies:  
```bash  
pip install -r requirements.txt  
```  
2. Get your Telegram Bot API key from [BotFather](https://t.me/BotFather).  
3. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).  
4. Run the bot:  
```bash  
python main.py ${Telegram_Bot_API_Key} ${Gemini_API_Key}  
```  

### (2) Docker Deployment  
#### Use Pre-built Image (x86 only):  
```bash  
docker run -d --restart=always -e TELEGRAM_BOT_API_KEY={Your_Telegram_API_Key} -e GEMINI_API_KEYS={Your_Gemini_API_Key} qwqhthqwq/gemini-telegram-bot:main  
```  

#### Build Manually:  
1. Clone the repository:  
```bash  
git clone https://github.com/H-T-H/Gemini-Telegram-Bot.git  
```  
2. Navigate to the project directory:  
```bash  
cd Gemini-Telegram-Bot  
```  
3. Build the Docker image:  
```bash  
docker build -t gemini_tg_bot .  
```  
4. Run the container:  
```bash  
docker run -d --restart=always -e TELEGRAM_BOT_API_KEY={Your_Telegram_API_Key} -e GEMINI_API_KEYS={Your_Gemini_API_Key} gemini_tg_bot  
```  



## Usage  
1. Send messages directly in private chat.  
2. In groups, use `/gemini` or `/gemini_pro` + your question.  
3. Use `/clear` to reset chat history.  
4. Use `/switch` to toggle the default model in private chats.  



https://fibonacci.monster/

--- 
