from nltk.chat.util import Chat, reflections

myself = [
    [
        r"(.*)my name is (.*)",
        ["Hello , How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is latest version, but you can just call me robot and I'm a chatfriend.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["I never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health " ,"how is your health",]
    ],
    [
        r"what(.*) is your age?",
        ["im a robot"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) "]
    ],
    [
        r"(.*)",
        ['we will get back to you soon']
    ],
 ]   

#default message at the start of chat
print("Hi, I'm latestversion and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(myself, reflections)


chat.converse()
