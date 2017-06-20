from bottle import route, run, template, redirect

vai_pros_eua = True
vai_quando = 'Abril 2018'

@route('/vai_pros_eua')
def index():
    if vai_pros_eua:
        return '<h1>Sim</h1><a href="vai_pros_eua/quando">Quando?</a>'
    else:
        return '<h1>Não</h1>'

@route('/vai_pros_eua/quando')
def index():
    if (vai_pros_eua):
        return '<h1>' + vai_quando + '</h1>'
    else:
        redirect('/vai_pros_eua')

run(host='localhost', port=8080)