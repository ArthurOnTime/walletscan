docker build . -t streamlit-app --platform linux/amd64
docker run -it \
    -v "$(pwd):/home/app"\
    -e PORT=80 \
    -p 4000:80 \
    streamlit-app
    #jedha/streamlit-sample-app