from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/benefits')
def benefits():
    return render_template('benefits.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Burada form verilerini işleyebilirsiniz (örneğin, veritabanına kaydetme)
        return redirect(url_for('index'))  # Başka bir sayfaya yönlendirme
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)