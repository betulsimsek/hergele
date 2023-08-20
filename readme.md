Bu proje, bir ödeme işlemi gerçekleştirmek, geri ödeme yapmak, kart listelemek ve kart kaydetmek gibi özellikleri olan bir ödeme sistemini içermektedir. 

Projenin çalışma mantığı şu şekildedir:

- İlk olarak, `pymongo` modülü kullanılarak MongoDB veritabanına bağlanılır.
- Projede kullanılacak hata mesajları ve çevresel değişkenler `.env` dosyasından alınır.
- Ardından, `perform_payment` fonksiyonu, kullanıcının hesabından belirli bir miktar parayı çekerek ödeme işlemini gerçekleştirir. Kullanıcının hesabında yeterli bakiye yoksa veya kullanıcı bulunamazsa hata mesajı döner.
- `process_refund` fonksiyonu ise kullanıcının en son ödeme işlemini geri ödemeyi işleme alır. Eğer kullanıcının geçmişinde ödeme işlemi yoksa veya daha önce geri ödeme yapıldıysa hata mesajı döner.
- `card_listing` fonksiyonu kullanıcının kaydedilmiş kartlarını listeler. Eğer kullanıcının kartları kaydedilmemişse hata mesajı döner.
- `card_registration` fonksiyonu ise kullanıcının yeni bir kartı kaydetmesini sağlar. Eğer kullanıcının koleksiyonunda kart zaten mevcut ise veya kart numarası geçerli değilse hata mesajı döner.
- `update_balance_with_card` fonksiyonu ise kullanıcının hesabındaki bakiyeyi günceller. Eğer kullanıcı bulunamazsa veya kart kayıt edilmemişse hata mesajı döner.

Bu projedeki fonksiyonlar, bir ödeme sistemi oluşturmak için kullanılabilir ve MongoDB veritabanını kullanarak kullanıcı bilgilerini saklamaktadır.

Postman sorguları:

1. Kart Saklama: Bu sorgu, kullanıcının belirli bir kartı saklamasını sağlar. userNo ve cardNo parametrelerini alır. Bu bilgileri kullanarak card_registration fonksiyonunu çağırır ve kartın kaydedilmesini sağlar.
   - Request Method: POST
   - Endpoint: `http://localhost:5000/kart-saklama`
   - Query Parameters: 
     - userNo: `<kullanıcı numarası>`
     - cardNo: `<kart numarası>`

2. Kart Saklamalı Ödeme: Bu sorgu, kullanıcının belirli bir miktarı kartıyla ödemesini sağlar. userNo ve amount parametrelerini alır. Bu bilgileri kullanarak perform_payment fonksiyonunu çağırır ve ödemenin gerçekleştirilmesini sağlar.
   - Request Method: POST
   - Endpoint: `http://localhost:5000/kart-saklamali-odeme`
   - Query Parameters: 
     - userNo: `<kullanıcı numarası>`
     - amount: `<ödeme miktarı>`

3. İade: Bu sorgu, kullanıcının önceki bir ödemeyi iade etmesini sağlar. userNo parametresini alır. Bu bilgiyi kullanarak process_refund fonksiyonunu çağırır ve iade işleminin gerçekleştirilmesini sağlar.
   - Request Method: POST
   - Endpoint: `http://localhost:5000/iade`
   - Query Parameters: 
     - userNo: `<kullanıcı numarası>`

4. Bakiye Güncelleme: Bu sorgu, kullanıcının bakiyesini belirli bir miktarla güncellemesini sağlar. userNo ve balance parametrelerini alır. Bu bilgileri kullanarak update_balance_with_card fonksiyonunu çağırır ve bakiye güncellemesinin gerçekleştirilmesini sağlar.
   - Request Method: POST
   - Endpoint: `http://localhost:5000/update_balance`
   - Query Parameters: 
     - userNo: `<kullanıcı numarası>`
     - balance: `<bakiye miktarı>`

5. Kart Saklama Listesi: Bu sorgu, kullanıcının sakladığı tüm kartların bir listesini döndürür. userNo parametresini alır. Bu bilgiyi kullanarak collection.find_one fonksiyonunu çağırır ve kullanıcının tüm kartlarını döndürür.
   - Request Method: GET
   - Endpoint: `http://localhost:5000/kart-saklama-listesi`
   - Query Parameters: 
     - userNo: `<kullanıcı numarası>`


