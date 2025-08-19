import json
import phonenumbers
import csv

def is_valid_phone(phone):
    try:
        parsed = phonenumbers.parse(phone, "TR")
        return phonenumbers.is_valid_number(parsed)
    except phonenumbers.NumberParseException:
        return False

def normalize_phone(phone):
    return phone.strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "").replace(" ", "")

def kontrol_et(json_dosya):
    with open(json_dosya, 'r', encoding='utf-8') as f:
        veriler = json.load(f)

    gecerli_kayitlar = []
    gecersiz_kayitlar = []

    for kayit in veriler:
        raw_tel = kayit.get("TelefonEMailWeb", "")
        temiz_tel = normalize_phone(raw_tel)

        if not temiz_tel.startswith("+"):
            temiz_tel = "+" + temiz_tel  # uluslararası format için başına + ekle

        if is_valid_phone(temiz_tel):
            gecerli_kayitlar.append(kayit)
        else:
            gecersiz_kayitlar.append(kayit)

    # CSV'ye yazma işlemi
    def write_to_csv(kayitlar, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["AdiSoyadi", "NufusCuzdani_TCKimlikNo", "NufusCuzdani_PasaportNo", "TelefonEMailWeb"])
            writer.writeheader()
            for kayit in kayitlar:
                writer.writerow(kayit)

    # Geçerli ve geçersiz telefon numaralarını ayrı ayrı CSV'ye yazıyoruz
    write_to_csv(gecerli_kayitlar, "gecerli_kayitlar.csv")
    write_to_csv(gecersiz_kayitlar, "gecersiz_kayitlar.csv")

    sonuc = {
        "GecerliKayitlar": gecerli_kayitlar,
        "GecersizKayitlar": gecersiz_kayitlar
    }
    with open("sonuc.json", "w", encoding="utf-8") as out:
        json.dump(sonuc, out, ensure_ascii=False, indent=2)

    print("İşlem tamamlandı. 'gecerli_kayitlar.csv' ve 'gecersiz_kayitlar.csv' dosyalarına yazıldı.")

if __name__ == "__main__":
    kontrol_et("veriler.json")
