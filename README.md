Para deploy no Heroku

Fazer login

cria app
heroku create

cria Banco
heroku addons:create heroku-postgresql:hobby-dev --app

ve config do app
heroku config --app blog-python-ocean

para atualizar
git push heroku main 