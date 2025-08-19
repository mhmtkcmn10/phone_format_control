📞 Türkiye Telefon Numarası Doğrulayıcı
Türkiye telefon numaralarını doğrulamak ve geçerli/geçersiz olanları ayrı dosyalara ayırmak için geliştirilmiş Python projesi.
🚀 Özellikler

Telefon Numarası Doğrulama: phonenumbers kütüphanesi kullanarak Türkiye telefon numaralarının geçerliliğini kontrol eder
Otomatik Temizleme: Parantez, tire, boşluk gibi karakterleri otomatik olarak temizler
Esnek Format Desteği: Farklı formatlardaki telefon numaralarını normalize eder
Çoklu Çıktı: Sonuçları hem CSV hem de JSON formatında kaydeder
Ayrılmış Kayıtlar: Geçerli ve geçersiz numaraları ayrı dosyalarda saklar

📋 Gereksinimler
txtphonenumbers==8.13.0
🛠️ Kurulum

Projeyi klonlayın:

bashgit clone https://github.com/mhmtkcmn10/phone_format_control.git
cd phone-number-validator

Gerekli paketleri yükleyin:

bashpip install phonenumbers
📝 Kullanım
Giriş Verisi Hazırlama
veriler.json dosyasını aşağıdaki formatta hazırlayın:
json[
  {
    "AdiSoyadi": "Ahmet Yılmaz",
    "NufusCuzdani_TCKimlikNo": "12345678901",
    "NufusCuzdani_PasaportNo": "",
    "TelefonEMailWeb": "+90 532 123 45 67"
  },
  {
    "AdiSoyadi": "Ayşe Demir",
    "NufusCuzdani_TCKimlikNo": "98765432109",
    "NufusCuzdani_PasaportNo": "",
    "TelefonEMailWeb": "0541-987-65-43"
  }
]
Programı Çalıştırma
bashpython phone_validator.py
Çıktı Dosyaları
Program çalıştıktan sonra aşağıdaki dosyalar oluşturulur:

gecerli_kayitlar.csv - Geçerli telefon numarasına sahip kayıtlar
gecersiz_kayitlar.csv - Geçersiz telefon numarasına sahip kayıtlar
sonuc.json - Tüm sonuçları içeren JSON dosyası

📊 Desteklenen Telefon Formatları
Program aşağıdaki telefon numarası formatlarını destekler:

+90 532 123 45 67
0532 123 45 67
532-123-45-67
(532) 123 45 67
5321234567

🔧 Kod Yapısı
Ana Fonksiyonlar

is_valid_phone(phone): Telefon numarasının geçerliliğini kontrol eder
normalize_phone(phone): Telefon numarasını temizler ve standardize eder
kontrol_et(json_dosya): Ana işlem fonksiyonu, dosyayı okur ve sonuçları kaydeder

Algoritma Akışı

JSON dosyasını okur
Her kayıt için telefon numarasını normalize eder
Gerektiğinde başına + ekler
phonenumbers kütüphanesi ile Türkiye standardında doğrular
Geçerli ve geçersiz kayıtları ayrı listelere böler
Sonuçları CSV ve JSON formatında kaydeder

📈 Örnek Çıktı
Terminal Çıktısı:
İşlem tamamlandı. 'gecerli_kayitlar.csv' ve 'gecersiz_kayitlar.csv' dosyalarına yazıldı.
CSV Çıktı Örneği (gecerli_kayitlar.csv):
csvAdiSoyadi,NufusCuzdani_TCKimlikNo,NufusCuzdani_PasaportNo,TelefonEMailWeb
Ahmet Yılmaz,12345678901,,+90 532 123 45 67
🛡️ Hata Yönetimi

NumberParseException: Geçersiz format durumunda kayıt geçersiz olarak işaretlenir
Dosya Okuma Hatası: UTF-8 encoding kullanılarak Türkçe karakter desteği sağlanır
Boş Değerler: Boş telefon numaraları otomatik olarak geçersiz sayılır



⭐ Bu projeyi beğendiyseniz yıldızlamayı unutmayın!
