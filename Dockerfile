FROM python:3.9.0

RUN set -x \
   && apt update \
   && apt upgrade -y \
   && apt install -y

RUN echo "===> Installing system dependencies..." && \
    BUILD_DEPS="curl unzip" && \
    apt-get update && apt-get install --no-install-recommends -y \
    python3 python3-pip wget \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 libgbm1 \
    $BUILD_DEPS \
    xvfb

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

WORKDIR /match-tracker

COPY requirements.txt .

RUN pip install -r requirements.txt


RUN pip install webdriver_manager

COPY ./api_esports_matches ./api_esports_matches

CMD ["python", "api_esports_matches/database_update.py"]

# Docker commands :
# docker build -t db-update .
# docker run --network bridge  -p 8000:8000 -v logs:/match-tracker/api_esports_matches/logs db-update
# docker exec -it <container-id> bash
