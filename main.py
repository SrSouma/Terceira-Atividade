from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def test_show_hello():
  return render_template('index.html')

@app.route('/unifran')
def test_show_unifran():
  return render_template('unifran.html')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0')