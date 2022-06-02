from flask import Flask, render_template    # cagirilan html dosyalarini kullan anlaminda

app = Flask(__name__)

@app.route("/")     # yolunu belli etmek icin kullanilir
def head():
    return render_template('index.html', number1 = 20, number2 = 40)

@app.route("/mult")     #   ana root altina klasör olusturur ve orada acar
def number():
    var1, var2 = 30, 70
    return render_template('body.html', num1=var1, num2=var2, mul=var1*var2)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    #app.run(debug=True)     #   debug modunu calistir ve hata varsa göster anlaminda