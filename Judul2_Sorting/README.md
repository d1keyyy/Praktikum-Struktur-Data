Program : Leaderboard hasil turnamen MPL
Ini adalah program menggunakan Insertion Sorting yang berfungsi untuk mengurutkan hasil turnamen MPL secara descending(Besar ke Kecil)
<img width="1762" height="1900" alt="code-snapshot" src="https://github.com/user-attachments/assets/4644720a-4f27-4f91-a4e7-51f5e0cbaa92" />
Logika Berjalan :
1. membuat class bernama Leaderboard
2. membuat class berisikan array kosong untuk penyimpanan dengan parameter self bernama team
3. membuat fungsi add_or_update_team untuk menambah atau mengupdate data team
4. dalam fungsi tersebut terdapat kode untuk mengecek apakah nama team sudah ada di dalam data? Jika ya maka update point jika tidak maka tambahkan team dan point lalu akan memaggil fungsi _insertion_sort untuk di sortir
5. pada fungsi _insertion_sort akan membandingkan point, jika lebih besar maka akan menggeser team lainnya
6. lalu fungsi show leaderboard untuk menampilkan output an sortingan tadi dengan kolom rank, nama tim, dan match point
7. baris selanjutnya diluar class leaderboard ada deklarasi lb untuk memanggil class leaderboard
8. lalu ada data team untuk dipakai oleh fungsi add_or_update_team
9. lalu perulangan mengambil data dari data_team dan akan memangil fungsi add_or_update_team
10. terakhir output dengan memanggil lb.show_leaderboard

Hasil Output
<img width="387" height="304" alt="Screenshot 2026-05-04 225520" src="https://github.com/user-attachments/assets/9f0d7283-1531-435a-bf91-8a4a5753ee61" />
Terlihat bahwa output diatas menghasilkan team yang terurut beradasarkan point secara descending
Link Video : https://youtu.be/MQTGbiz-zB4
