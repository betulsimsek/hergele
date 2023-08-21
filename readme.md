Postman API:https://blue-moon-503502.postman.co/workspace/Team-Workspace~164df39a-2847-4ba2-8867-062d1b738a06/collection/18954017-49ced358-d20a-4718-8735-59c4bcfe7012?action=share&creator=18954017

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

veritabanı oluşturmak için aşağıdaki komutu kullanın:
  ```
  use mydatabase
  ```
  Burada "mydatabase", oluşturacağınız veritabanının adıdır. Sizin isteğiniz doğrultusunda başka bir isim de kullanabilirsiniz.
- Ardından, örnekteki yapıya uygun şekilde bir koleksiyon oluşturmak için aşağıdaki komutu kullanın:
  ```

Örnekteki alanlar:

userNo: Kullanıcı numarası
authCode: Yetkilendirme kodu veya şifre
name: Kullanıcının adı
surname: Kullanıcının soyadı
birthDate: Kullanıcının doğum tarihi
phoneNumber: Kullanıcının telefon numarası
email: Kullanıcının e-posta adresi
selectedCard: Seçili kart bilgisi
allCards: Tüm kartların listesi
balance: Bakiye

db.users.insertMany([
    {
        userNo: "123456",
        authCode: "abc123",
        name: "John",
        surname: "Doe",
        birthDate: "1990-01-01",
        phoneNumber: "+123456789",
        email: "johndoe@example.com",
        selectedCard: "1234 5678 9012 3456",
        allCards: ["1234 5678 9012 3456", "9876 5432 1098 7654"],
        balance: 1000.50
    },
    {
        userNo: "654321",
        authCode: "xyz789",
        name: "Jane",
        surname: "Smith",
        birthDate: "1985-05-20",
        phoneNumber: "+987654321",
        email: "janesmith@example.com",
        selectedCard: "5678 9012 3456 7890",
        allCards: ["5678 9012 3456 7890", "0987 6543 2109 8765"],
        balance: 500.75
    },
    {
        userNo: "987654",
        authCode: "def456",
        name: "Alice",
        surname: "Johnson",
        birthDate: "1978-11-30",
        phoneNumber: "+543216789",
        email: "alicejohnson@example.com",
        selectedCard: "4321 9876 5432 1098",
        allCards: ["4321 9876 5432 1098", "8765 2109 6543 0987"],
        balance: 2500.10
    },
    {
        userNo: "246813",
        authCode: "uvw789",
        name: "Michael",
        surname: "Brown",
        birthDate: "1995-09-15",
        phoneNumber: "+135792468",
        email: "michaelbrown@example.com",
        selectedCard: "1111 2222 3333 4444",
        allCards: ["1111 2222 3333 4444", "5555 6666 7777 8888"],
        balance: 750.25
    },
    {
        userNo: "135792",
        authCode: "pqr456",
        name: "Emma",
        surname: "Wilson",
        birthDate: "1983-07-10",
        phoneNumber: "+987654321",
        email: "emmawilson@example.com",
        selectedCard: "9999 8888 7777 6666",
        allCards: ["9999 8888 7777 6666", "3333 2222 1111 0000"],
        balance: 1345.90
    },
    {
        userNo: "112233",
        authCode: "xyz123",
        name: "Robert",
        surname: "Lee",
        birthDate: "1997-03-25",
        phoneNumber: "+123456789",
        email: "robertlee@example.com",
        selectedCard: "5555 4444 3333 2222",
        allCards: ["5555 4444 3333 2222", "0000 1111 2222 3333"],
        balance: 234.50
    },
    {
        userNo: "111222",
        authCode: "xyz789",
        name: "Sarah",
        surname: "Johnson",
        birthDate: "1982-09-12",
        phoneNumber: "+987654321",
        email: "sarahjohnson@example.com",
        selectedCard: "7777 8888 9999 0000",
        allCards: ["7777 8888 9999 0000", "1111 2222 3333 4444"],
        balance: 1800.35
    },
    {
        userNo: "444555",
        authCode: "mno123",
        name: "David",
        surname: "Taylor",
        birthDate: "1991-06-25",
        phoneNumber: "+543216789",
        email: "davidtaylor@example.com",
        selectedCard: "2222 3333 4444 5555",
        allCards: ["2222 3333 4444 5555", "6666 7777 8888 9999"],
        balance: 930.90
    },
    {
        userNo: "666777",
        authCode: "pqr456",
        name: "Olivia",
        surname: "Thomas",
        birthDate: "1994-04-15",
        phoneNumber: "+135792468",
        email: "oliviathomas@example.com",
        selectedCard: "9999 8888 7777 6666",
        allCards: ["9999 8888 7777 6666", "3333 2222 1111 0000"],
        balance: 1575.60
    },
    {
        userNo: "888999",
        authCode: "abc123",
        name: "Sophia",
        surname: "Brown",
        birthDate: "1986-10-30",
        phoneNumber: "+123456789",
        email: "sophiabrown@example.com",
        selectedCard: "5555 4444 3333 2222",
        allCards: ["5555 4444 3333 2222", "0000 1111 2222 3333"],
        balance: 890.75
    }
]);


//- Verileri başarıyla ekledikten sonra, performans için indexler oluşturmamız önerilir. Örneğin, "userNo" alanı üzerinde index oluşturmak için aşağıdaki komutu kullandım:


// Create index for userNo field
db.users.createIndex({ userNo: 1 })

// Create index for authCode field
db.users.createIndex({ authCode: 1 })

// Create index for name field
db.users.createIndex({ name: 1 })

// Create index for surname field
db.users.createIndex({ surname: 1 })

// Create index for birthDate field
db.users.createIndex({ birthDate: 1 })

// Create index for phoneNumber field
db.users.createIndex({ phoneNumber: 1 })

// Create index for email field
db.users.createIndex({ email: 1 })

// Create index for selectedCard field
db.users.createIndex({ selectedCard: 1 })

// Create index for allCards field
db.users.createIndex({ allCards: 1 })

// Create index for balance field
db.users.createIndex({ balance: 1 })


- Scale amaçlı yapılabilecek ayarlar, performans veya yüksek veritabanı trafiği durumunda kullanılabilen çözümler içerir. Bazı yaygın yöntemler şunlardır:
  - Shardlama: Verileri birden fazla fiziksel sunucuya dağıtarak yükü paylaştırma.
  - Replica Set: Verileri yedekleyerek yüksek düzeyde veri erişilebilirliği sağlama.
  - Indeks optimizasyonu: Sorguların performansını artırmak için doğru indexlerin kullanılması.
  - Caching: Sık kullanılan verilerin bellekte tutulmasıyla veritabanına olan talebi azaltma.
  - Sorgu optimizasyonu: Karmaşık sorguların optimize edilmesi.
  
Projede ise caching yapmaya çalıştım.
MongoDB'de caching yapmak için genellikle önbellekleme ("caching") katmanı olarak bir ana bellek veritabanı hizmeti kullanılır. Bu tip hizmetler, verileri geçici olarak bellekte depolayarak sorgu sürelerini azaltır ve veritabanının yükünü hafifletir.

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

User Authenticate and Create User
### authenticate_first_route:
Bu rota, ilk adım için kimlik doğrulama sürecini yönetir. POST isteği alır, isteğin başlıklarını alır ve başlıklardan 'Filo' ve 'userNo' değerlerini alır. Ardından, 'userNo' değerine göre kullanıcı belgesini bulur ve `secrets.token_hex()` fonksiyonunu kullanarak yeni bir yetkilendirme kodu oluşturur. Yeni yetkilendirme kodu, kullanıcı için 'auth' koleksiyonunda saklanır. Son olarak, 'Filo' ve 'userNo' değerlerine dayanarak kimlik doğrulama yapar ve kullanıcının bulunup bulunmadığına dair bir yanıt döndürür.

POST /authenticate_first_route
Content-Type: application/json

{
  "Filo": "exampleFilosu",
  "userNo": "12345"
}
### authenticate_second_route:
Bu rota, ikinci adım için kimlik doğrulama sürecini yönetir. Bu da bir POST isteği alır ve isteğin başlıklarını alır. Önceki rotada olduğu gibi, başlıklardan 'Filo', 'Authorization' ve 'userNo' değerlerini alır. 'userNo' değerine göre kullanıcı belgesini bulur ve yeni bir yetkilendirme kodu oluşturur. Yeni yetkilendirme kodu, kullanıcı için 'auth' koleksiyonuna kaydedilir. Daha sonra, 'Filo', 'Authorization' ve 'userNo' değerlerine dayanarak kimlik doğrulama yapar. Tüm koşullar sağlandığında, kullanıcının doğrulandığını belirten bir yanıt döndürür. Aksi takdirde, kullanıcı kimlik doğrulamasının başarısız olduğunu belirten bir yanıt döndürür.

POST /authenticate_second_route
Content-Type: application/json
Authorization: Bearer exampleToken
userNo: 12345
Filo: hergele

### create_user:
Bu rota, yeni bir kullanıcı oluşturmayı sağlar. Bir POST isteği alır ve isteğin JSON verilerini alır. Verilerden 'userNo', 'authCode', 'name', 'surname', 'birthDate', 'phoneNumber', 'email', 'selectedCard', 'allCards' ve 'balance' gibi gereken alanları çıkarır. Bu alanlarla birlikte bir kullanıcı belgesi oluşturur ve 'users' koleksiyonuna ekler. Son olarak, kullanıcının başarıyla oluşturulduğunu belirten bir yanıt döndürür.

{
  "userNo": "12345",
  "authCode": "abcdef",
  "name": "John",
  "surname": "Doe",
  "birthDate": "1990-01-01",
  "phoneNumber": "555-5555",
  "email": "john.doe@example.com",
  "selectedCard": "1234 5678 1234 1334",
  "balance": 100.00
}


