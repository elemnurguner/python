# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"merhaba|selam|hey",
        ["Merhaba! Nasıl yardımcı olabilirim?", "Selam! Nasılsın?"]
    ],
    [
        r"nasılsın\?",
        ["İyiyim, sen nasılsın?", "Harika hissediyorum, sen nasılsın?"]
    ],
    [
        r"benim adım (.*)",
        ["Merhaba %1! Nasılsın?", "Hoş geldin %1!"]
    ],
    [
        r"ne yapıyorsun\?",
        ["Seninle sohbet ediyorum!", "Sana yardımcı olmaya çalışıyorum."]
    ],
    [
        r"görüşürüz|hoşça kal",
        ["Görüşürüz! İyi günler.", "Hoşça kal!"]
    ],
    [
        r"(.*) yaşın kaç\?",
        ["Ben bir botum, yaşım yok :)"]
    ],
    [
        r"(.*) (mutsuzum|üzgünüm)",
        ["Üzgün hissetmen üzücü. Neden böyle hissediyorsun?", "Neden üzgünsün? Anlatmak ister misin?"]
    ],
    [
        r"(.*) (mutluyum|iyiyim)",
        ["Bu harika bir haber!", "Ne güzel! Mutlu olduğunu duymak beni de mutlu ediyor."]
    ],
    [
        r"(.*) (teşekkür ederim|teşekkürler)",
        ["Rica ederim! Başka bir şey var mı?", "Ne demek, her zaman!"]
    ],
    [
        r"(.*)",
        ["Anlamadım, biraz daha açıklar mısın?", "Üzgünüm, bunu anlayamadım."]
    ]
]

chatbot = Chat(pairs, reflections)

print("Merhaba! Ben basit bir chatbotum. Sorularınızı sorabilirsiniz.")
while True:
    user_input = input("Sen: ")
    if user_input.lower() in ["çıkış", "exit", "quit"]:
        print("Chatbot: Görüşürüz!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)