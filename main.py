from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return '<h1>Meu primeiro template</h1>'

@app.route('/unifran')
def unifran ():
  return '<h2>Universidade de Franca</h2>'

@app.route('/dashboard/<nome>')
def dashboard(nome):
    return f'Olá, {nome}'
if __name__ == '__main__':
  app.run(host='0.0.0.0')