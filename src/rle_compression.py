# Run-Length Encoding (RLE) Sıkıştırma Algoritması
# BLM101 Dönem Projesi

def rle_encode(data):
    # Bu fonksiyon metni RLE yöntemiyle sıkıştırır
    encoded = ""
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded += str(count) + data[i - 1]
            count = 1

    encoded += str(count) + data[-1]
    return encoded


def rle_decode(data):
    # Bu fonksiyon RLE ile sıkıştırılmış metni açar
    decoded = ""
    count = ""

    for char in data:
        if char.isdigit():
            count += char
        else:
            decoded += char * int(count)
            count = ""

    return decoded


def compression_ratio(original, compressed):
    # Sıkıştırma oranını yüzde olarak hesaplar
    return (1 - len(compressed) / len(original)) * 100


if __name__ == "__main__":
    original = "AAAAABBBCCDAA"
    encoded = rle_encode(original)
    decoded = rle_decode(encoded)

    print("Orijinal:", original)
    print("Sıkıştırılmış:", encoded)
    print("Açılmış:", decoded)
    print("Sıkıştırma Oranı: %{:.2f}".format(
        compression_ratio(original, encoded)))
