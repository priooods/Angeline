# Angeline 

Angeline adalah Project besar yang sedang saya buat untuk masa depan dan bersifat Open Source. Angeline sendiri merupakan project yang dibagi menjadi dua role model yaitu Machine Learning dan Blockchain & Cryptocurency.


## Role Model

1. **Machine Learning**

Fungsi utama Angeline pada Machine Learning adalah untuk membuat Assistant Pintar yang dapat
membantu aktifitas satu manusia, atau manusia dengan manusia lain tanpa batasan tempat, waktu
dan kebutuhan.

2. **Blockchain & Cryptocurency**

Fungsi utama Angeline pada Blockchain & Cryptocurency adalah untuk menopang kebutuhan Machine Learning
dengan menerapkan konsep Blockchain dan Peer to Peer pada setiap interaksi data antar pengguna serta Cryptocurency yang akan diselaraskan untuk kebutuhan dalam menampung semua dukungan dalam bentuk uang digital serta untuk menjadi bentuk mata uang yang akan diterapkan pada setiap transaksi jual beli
antar pengguna apabila melalui Angeline


## Instalasi

Untuk dapat menjalankan atau bergabung dalam proses pembuatan Angeline anda dapat mengcloning
Angeline pada komputer anda dengan memasukan perintah pada Terminal

``` bash
git clone https://github.com/priooods/Angeline.git
```

setelah anda berhasil melakukan cloning Project Angeline, silahkan anda buka project Angeline
pada Code Editor pilihan anda. Saya menyarankan anda menggunakan VSCode.

1. **Machine Learning**
        
    Untuk menggunakan atau bergabung dengan project Angeline pada role Machine Learning anda
    diharuskan untuk menjalankan instalasi module yang saya pakai dalam pembuatan Angeline Machine Learning. cara instalasi module anda dapat pergi ke folder ***artificial*** melalui terminal dengan cara berikut :

    ``` bash
    ## pergi ke folder artificial
    C:/User/Angeline: cd artificial
    ```

    - **Noted**

    Apabila anda belum melakukan setup [ffmpeg](https://ffmpeg.org/download.html) atau [libav](https://libav.org/) pada Enviroment, anda dapat mendownload melalui halaman berikut [download libav](http://builds.libav.org/windows/release-gpl/)

    **cara setup**

    - download libav pada link diatas
    - extract zip
    - copy lokasi directory `/bin` ke `PATH` Environment
    - lanjutkan step selanjutnya untuk menginstall requirement.txt

    *lewati noted ini apabila anda telah mensetup **[ffmpeg](https://ffmpeg.org/download.html)** atau **[libav](https://libav.org/)** sebelumnya*

    ``` bash
    ## jalankan perintah install module pada file requirement.txt
    C:/User/Angeline/artifical: pip install -r requirement.txt
    ```

    1. Voice Biometric

        Pada tahap pertama angeline akan dibekali dengan kemampuan Voice Biometric, dan untuk melakukan setup pada voice biometric anda dapat memperhatikan beberapa point penting, yaitu :

        - **MODEL AUDIO**

            Model audio yang bisa anda pakai sebagai sample data, dapat anda lihat pada `/artificial/audio` . pada `PATH` tersebut anda juga dapat memasukan semua audio model yang ingin anda masukan sendiri. 

            Saya juga menyediakan beberapa method yang dapat anda gunakan langsung tanpa perlu membuat lagi dari awal

            ``` python

            def create_voice_model() # method untuk membuat model baru dari rekaman audio langsung

            def manipulate_audio_filename() # method untuk mereplace audio file dengan audio baru dan dengan filename custom

            ```

            lihat method lain dengan pergi ke file `/artificial/voice_biometric/utils.py` . ( saya menyertakan documentasi code )


        - **FEATURE EXTRACTION**

            Untuk melakukan feature extraction saya menggunakan pendekatan yang lebih spesific dengan melakukan banyak extraction pada audio data, dan saya melakukan ini dengan referensi extraction yang dapat ada lihat pada link berikut [Referensi Extraction Audio](https://www.kaggle.com/primaryobjects/voicegender)

            Untuk melihat bagaimana saya melakukan Feature Extraction terhadap Audio anda dapat mempelajarinya dengan membuka file `/artificial/voice_biometric/prepocessing.py` . ( saya menyertakan documentasi code )

        - **DATASETS**

            Dataset pada Angeline disimpan dalam bentuk `.. .cvs` yang berisikan value - value yang didapat dari hasil Prepocessing. [Referensi Format Audio Datasets](https://www.kaggle.com/primaryobjects/voicegender)

            Apabila anda ingin membuat datasets sendiri, anda dapat memanggil Method yang sudah saya siapkan, anda bisa melihat pada file `/artificial/voice_biometric/create-dataset.py`

            ``` python

            def _new_dataset() # method untuk membuat atau melakukan update datasets, Sesuaikan value pada argument dengan tujuan anda

            ```

1. **Blockchain & Cryptocurency**
        
    Untuk menggunakan atau bergabung dengan project Angeline pada role Blockchain & Cryptocurency anda
    diharuskan untuk menginstall **node_module** yang menjadi kerangka kerja **Node JS**. untuk cara instalasi anda dapat pergi ke folder ***cryptocurency*** melalui terminal dengan cara berikut :

    ``` bash
    ## pergi ke folder artificial
    C:/User/Angeline: cd cryptocurency

    ## jalankan perintah install module pada file requirement.txt
    C:/User/Angeline/artifical: npm install
    ```

    - **Noted**

    **Untuk saat ini blockchain & Crytptocurency masih dalam tahap blueprint yang saya buat menggunakan *JavaScript* , Saya harus melakukan migrasi ke dalam bahasa C . dan saya saat ini sedang belajar bahasa C**

    

## License
MIT License

Copyright (c) 2021 Prio Dwi Sembodo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

        



