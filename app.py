from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() :
    datas = ['fulan', 'fulani', 'fulano']
    return render_template('index.html', datas=datas)

if __name__ == "__main__" :
    app.run(debug=True)