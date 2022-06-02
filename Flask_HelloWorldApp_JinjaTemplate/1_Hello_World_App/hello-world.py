from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello world from Flask"

@app.route("/second")
def second():
    return "This is my second page"

@app.route("/third/subthird")
def third():
    return "<center><h2>This is the subpath of third page</h2></center>"  

@app.route("/forth/<string:id>")
def forth(id):
    return f'<h2>Id of this page is {id}</h2>' #  browsere girilen yaziyi alt klasör olarak görür

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)    # host ile tüm dünyaya yayin yap anlamindadir
    #app.run(debug=True, port=80)    # default olarak 5000 port gelir ama istedigimiz gibi tanimlayabiliriz