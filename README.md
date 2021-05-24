# Anti-Spam-Bot
An anti-spam/anti-raid bot for discord. It detects the number of messages being sent in a chat. Every time a message us sent, the bot stores the message in a .txt file and it's an async event so it'll be called personally for every time someone sends a message to the chat which is then counted. If it exceeds a certain threshold, the bot removes the user from the server.
