alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZаАбБвВгГдДеЕёЁжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯ.,;:?!…—–-‐‑‒―()[]{}⟨⟩«»“”„‟‘’‚‛'`´‽¡¿/|~@#№§¶*^&+=_<>°±×÷"
key = int(input())
def decoder (inp_letter, key):
    i = alphabet.find(inp_letter)
    if i != -1:
        return alphabet[(i-key)%(len(alphabet))] 
    else:
        return inp_letter

with open('encoder/Cesar/crypt_message.txt', 'r', encoding='utf-8') as input_message, \
    open('encoder/Cesar/decrypt_message.txt', 'w', encoding='utf-8') as crypt_message:
    while True:
        chunk = input_message.read(4096)
        if not chunk:
            break
        for ch in chunk:
            crypt_message.write(decoder(ch, key))
