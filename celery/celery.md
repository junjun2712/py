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

启动信息：
```
# celery -A tasks worker --loglevel=info
/root/ver/lib/python3.6/site-packages/celery/platforms.py:796: RuntimeWarning: You're running the worker with superuser privileges: this is
absolutely not recommended!

Please specify a different user using the --uid option.

User information: uid=0 euid=0 gid=0 egid=0

  uid=uid, euid=euid, gid=gid, egid=egid,
 
 -------------- celery@localhost.localdomain v4.2.0 (windowlicker)
---- **** ----- 
--- * ***  * -- Linux-3.10.0-693.el7.x86_64-x86_64-with-centos-7.4.1708-Core 2018-11-01 10:54:22
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x7fd6847298d0
- ** ---------- .> transport:   redis://localhost:6379/1
- ** ---------- .> results:     redis://localhost:6379/1
- *** --- * --- .> concurrency: 2 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . tasks.add

[2018-11-01 10:54:22,650: INFO/MainProcess] Connected to redis://localhost:6379/1
[2018-11-01 10:54:22,672: INFO/MainProcess] mingle: searching for neighbors
[2018-11-01 10:54:23,733: INFO/MainProcess] mingle: all alone
[2018-11-01 10:54:23,755: INFO/MainProcess] celery@localhost.localdomain ready.
```

