from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    # Inisialisasi data awal
    final_price = None
    total_awal = 0
    potongan = 0
    
    if request.method == "POST":
        try:
            # Mengambil data yang dikirim dari form HTML
            price = float(request.form.get("price"))
            quantity = int(request.form.get("quantity"))
            discount_rate = float(request.form.get("discount"))
            
            # Logika perhitungan matematika
            total_awal = price * quantity
            potongan = total_awal * (discount_rate / 100)
            final_price = total_awal - potongan
            
        except ValueError:
            # Mengantisipasi jika ada error input non-angka
            pass
            
    # render_template akan otomatis mencari file 'index.html' di dalam folder 'templates'
    return render_template("index.html", final_price=final_price, total_awal=total_awal, potongan=potongan)

if __name__ == "__main__":
    print("Server berjalan sukses!")
    app.run(debug=True)