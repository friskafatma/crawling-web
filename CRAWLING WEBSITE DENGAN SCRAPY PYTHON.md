FRISKA FATMAWATININGRUM / 160411100084



**LANGKAH MELAKUKAN CRAWL WEB DENGAN LIBRARY SCRAPY DI PYTHON**

website : https://brickset.com/sets/year-2016/

website tersebut menjual permainan atau barang lego dan untuk data yang diambil adalah nama barang yang dijual pada tahun 2016

**Tools  :**

1. Python 2.7
2. Library python yang digunakan adalah scrapy
3. cmd (*command prompt*)



**Langkah - langkah :**

1. Buka cmd dan masuk ke localdisk C di folder python 2.7 dan masuk ke folder Script nya.

2. Kemudian install library scrapy di cmd menggunakan source code (***pip install scrapy***)

3. Setelah itu buatlah project spider baru dengan code  berikut :

   ```
   scrapy startproject namaprojectmu
   ```

   code diatas akan otomatis membuat folder di dalam folder spider dengan nama projet yang dibuat.

4. Buatlah file spider baru dengan code :

   ```
   scrapy genspider namafilespider urlweb
   ```

   perintah genspider pada scrapy digunakan untuk membuat file spider baru. setelah itu akan otomatis terbuat file python dengan nama *namafilespider.py* didalam folder spider.

   contoh : ***scrapy genspider coba https://brickset.com/sets/year-2016/*** dan terbentuk file *coba.py*

5. Buka file python yang telah otomatis dibuat sebelumnya. Setelah itu edit code yang berada di dalam function parse dan gunakan perintah untuk mengambil data tertentu yang diinginkan pada web. 

   Dan disini saya mengambil data berbentuk teks.

   ```
   def parse(self, response):
           titles = response.css('.title ::text').extract()
           for item in zip(titles):
           scraped_info = {
               'title' : item[0]
           }
           yield scraped_info
   ```

   code penting tersimpan pada variabel titles yang didalamnya terdapat perintah *response.css* yang digunakan untuk mengambil data pada web tersebut dengan memanfaatkan class css web tersebut. Untuk dapat mengetahui class css apa yang dibutuhkan maka lakukan inspect elemen pada web tersebut.

   yield scraped_info digunakan untuk return data yang diambil.

6. Simpan code sampai tahap 5 kemudian run file python tersebut di cmd dengan perintah :

   ```
   scrapy runspider namafilespider.py
   ```

7. Setelah berhasil simpan data yang telah diambil ke dalam bentuk excel atau csv dengan perintah :

   ```
   scrapy crawl namafilespider.py -o namafilespider.csv -t csv
   ```

   Kemudian terbentuk file dengan nama namafilespider.csv yang berisi data yang telah diambil.

8. Buatlah database baru di mysql phpmyadmin, lalu import file csv tersebut.