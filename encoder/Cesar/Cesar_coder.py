alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZаАбБвВгГдДеЕёЁжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯ.,;:?!…—–-‐‑‒―()[]{}⟨⟩«»“”„‟‘’‚‛'`´‽¡¿/|~@#№§¶*^&+=_<>°±×÷"
key = int(input())
def encoder (inp_letter, key):
    i = alphabet.find(inp_letter)
    return alphabet[(i+key)%(len(alphabet))] 
with open('encoder/Cesar/input.txt', 'r', encoding='utf-8') as input_message, \
    open('encoder/Cesar/crypt_message.txt', 'w', encoding='utf-8') as crypt_message:
    while True:
        chunk = input_message.read(4096)
        if not chunk:
            break
        for ch in chunk:
            crypt_message.write(encoder(ch, key))

