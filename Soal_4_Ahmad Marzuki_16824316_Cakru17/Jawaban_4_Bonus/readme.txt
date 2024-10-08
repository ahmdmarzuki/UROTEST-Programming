Untuk soal 4 bonus, saya membuat algoritma A* (A Star)

Cara kerja A*:
setiap node pada A* memiliki dua nilai yaitu g(n) dan h(n).
g(n) yaitu Jarak yang telah ditempuh dari node awal sampai node saat ini.
h(n) adalah nilai heuristic yaitu nilai estimasi Jarak dari node saat ini ke tujuan.
yang terakhir ada nilai f(n), yaitu akumulasi dari nilai g(n) dan h(n) ----> f(n) = g(n) + h(n)

Algoritma A* akan memilih nilai f(n) terkecil, melebar ke node lain dan memperbarui nilai g(n) dan h(n) untuk setiap node, proses ini akan berlanjut sampai ke titik tujuan.

key:
LEFT MOUSE BUTTON = untuk menggambar start point, end point, dan barrier.
RIGHT MOUSE BUTTON = Menghapus spot yang sudah Digambar.
SPACE = untuk menjalankan algoritma Ketika start point dan end point sudah Digambar.
C = reset.

untuk penjelasan code nya saya sertakan dalam bentuk comment di setiap bagian code nya.