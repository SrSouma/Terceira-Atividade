from flask import Flask
app = Flask('app')

@app.route('/')
def test_show_hello():
  return '<h1>Meu primeiro template</h1>'

@app.route('/unifran')
def test_show_unifran():
  return '<h2>Universidade de Franca</h2>'

@app.route('/dashboard/<nome>')
def dashboard(nome):
    return f'Olá, {nome}'
if __name__ == '__main__':
  app.run(host='0.0.0.0')