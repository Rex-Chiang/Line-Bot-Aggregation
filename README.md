# Line-Bot-Aggregation

## Overview
Users can receive messages with english vocabulary and example through LINE (Communication App) to help users expand their vocabulary and improve their english skills.

This project was deployed on **Fly.io (https://fly.io)**

## Developing
- Back-End
  - Python3
  - Django
  - Django Rest Framwork
  - Line-bot-sdk
  - Asyncio
  - Celery
  - OpenAI
- Database
  - SQLite
- Deployment
  - Docker
  - Fly.io

## Quick start
- Clone this repository
```
git clone https://github.com/Rex-Chiang/line-bot-aggregation.git
cd line-bot-aggregation
```
- Setup environment variables
  - PORT 
      - Required in **gunicorn.conf.py**
      - Host port for server
  - VOCABULARY_HOST
      - Required in **settings.py**
      - English vocabulary API
  - LINE_CHANNEL_SECRET
      - Required in **settings.py**
      - LINE App secret key
  - LINE_CHANNEL_ACCESS_TOKEN
      - Required in **settings.py**
      - LINE App access token
  - MESSAGE_PICTURE_URL
      - Required in **settings.py**
      - Picture in LINE flex message
  - CELERY_BROKER_URL
      - Required in **settings.py**
      - Broker for Celery library
  - CELERY_RESULT_BACKEND
      - Required in **settings.py**
      - Result storage for Celery library
  - OPENAI_API_KEY
      - Required in **settings.py**
      - OpenAI API key
  - CHATGPT_PROMPT_EXAMPLE
      - Required in **settings.py**
      - ChatGPT prompt for making example
  - CHATGPT_PROMPT_TRANSLATION
      - Required in **settings.py**
      - ChatGPT prompt for making translation
  - LOG_VERSION
      - Required in **settings.py**
      - Log type for logger
- Setup virtual environment
```
python3 -m venv YourVirtualEnvironmentName
source YourVirtualEnvironmentName/bin/activate
```
- Inatall required libraries
```
pip3 install -r requirements.txt
```
- Run the Django server
```
sh runserver.sh
```

## Deployment
- Clone this repository
```
git clone https://github.com/Rex-Chiang/line-bot-aggregation.git
cd line-bot-aggregation
```
- Setup environment variables
  - PORT 
      - Required in **gunicorn.conf.py**
      - Host port for server
  - VOCABULARY_HOST
      - Required in **settings.py**
      - English vocabulary API
  - LINE_CHANNEL_SECRET
      - Required in **settings.py**
      - LINE App secret key
  - LINE_CHANNEL_ACCESS_TOKEN
      - Required in **settings.py**
      - LINE App access token
  - MESSAGE_PICTURE_URL
      - Required in **settings.py**
      - Picture in LINE flex message
  - CELERY_BROKER_URL
      - Required in **settings.py**
      - Broker for Celery library
  - CELERY_RESULT_BACKEND
      - Required in **settings.py**
      - Result storage for Celery library
  - OPENAI_API_KEY
      - Required in **settings.py**
      - OpenAI API key
  - CHATGPT_PROMPT_EXAMPLE
      - Required in **settings.py**
      - ChatGPT prompt for making example
  - CHATGPT_PROMPT_TRANSLATION
      - Required in **settings.py**
      - ChatGPT prompt for making translation
  - LOG_VERSION
      - Required in **settings.py**
      - Log type for logger
- Build and tag docker image
```
docker build -t line-bot-aggregation .
docker tag line-bot-aggregation  YourDockerHubAccount/line-bot-aggregation
```
- Push docker image to DockerHub
```
docker push YourDockerHubAccount/line-bot-aggregation
```
- Init the **Fly.io** application
```
flyctl launch
```
- Setup the **Fly.io** configuraton
  - Refer to **fly.toml**
- Deploy **Fly.io** application
```
flyctl deploy
```
