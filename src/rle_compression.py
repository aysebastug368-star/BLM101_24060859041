# Run-Length Encoding (RLE) Sıkıştırma Algoritması
# BLM101 Bilgisayar Mühendisliğine Giriş Dersi Projesi

def rle_encode(text):
    """
    Bu fonksiyon verilen metni
    Run-Length Encoding yöntemiyle sıkıştırır.
    """
    if not text:
        return ""

    encodedData = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encodedData += str(count) + text[i - 1]
            count = 1

    encodedData += str(count) + text[-1]
    return encodedData


def rle_decode(encodedData):
    """
    Bu fonksiyon RLE ile sıkıştırılmış metni
    tekrar eski haline çevirir.
    """
    decoded_text = ""
    number = ""

    for char in encodedData:
        if char.isdigit():
            number += char
        else:
            decoded_text += char * int(number)
            number = ""

    return decoded_text


def compression_ratio(original, compressed):
    """
    Sıkıştırma oranını yüzde olarak hesaplar.
    """
    return (1 - len(compressed) / len(original)) * 100


def main():
    # Kullanıcıdan veri al
    userInput = input("Sıkıştırılacak metni giriniz: ")

    encoded = rle_encode(userInput)
    decoded = rle_decode(encoded)
    ratio = compression_ratio(userInput, encoded)

    print("\n--- SONUÇLAR ---")
    print("Orijinal Metin:", userInput)
    print("Sıkıştırılmış Metin:", encoded)
    print("Açılmış Metin:", decoded)
    print("Sıkıştırma Oranı: %{:.2f}".format(ratio))


if __name__ == "__main__":
    main()
