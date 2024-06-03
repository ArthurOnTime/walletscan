#docker build . -t streamlit-app --platform linux/amd64
docker run -it \
    -v "$(pwd):/home/app"\
    -e PORT=80 \
    -e NIXTLA_API_KEY=$NIXTLA_API_KEY \
    -p 4001:80 \
    streamlit-app