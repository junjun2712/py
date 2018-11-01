# Celery

Broker(中间人消息队列): Redis

组件介绍：https://mp.weixin.qq.com/s/AydTOwLSGWjp_RE7WVgkMA


## install redis
https://redis.io/download

```bash
export PATH=$PATH:/usr/local/redis/src/
redis-cli 
#127.0.0.1:6379>
# or
echo 'PATH=$PATH:/usr/local/redis/src/' >> /etc/profile
source /etc/profile
```

## 2 install celery
```bash
python3 -m venv ver
source  ver/bin/activate
pip install redis
pip install -U Celery==4.2

celery --version
#4.2.0 (windowlicker)
```


## 教程

http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html

```python
app = Celery('tasks', backend='redis://localhost:6379/1', broker='redis://localhost:6379/1')
```

```bash
mkdir -p /home/wwwroot/celery
```


### App1

#### Application

```bash
mkdir app1 && cd app1
```

vim tasks.py
```python
from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379/1', broker='redis://localhost:6379/1')

@app.task
def add(x, y):
    return x + y
```


### Running the Celery worker server

```bash
celery -A tasks worker --loglevel=info
```
