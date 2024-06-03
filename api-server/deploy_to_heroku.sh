heroku login
heroku container:login
heroku create walletscan-api
docker build . -t walletscan-api --platform linux/amd64
docker tag walletscan-api registry.heroku.com/walletscan-api/web
docker push registry.heroku.com/walletscan-api/web
heroku container:release web -a walletscan-api