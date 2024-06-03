docker build . -t walletscan-api --platform linux/amd64
docker run -it \
-v "$(pwd):/home/app" \
-p 4000:4000 \
-e PORT=4000 \
walletscan-api #nom de l'image docker