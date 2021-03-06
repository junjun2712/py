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


### App1 异步执行

#### Application

```bash
mkdir app1 && cd app1
```

vim tasks.py
```python
import time

from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379/1', broker='redis://localhost:6379/1')

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    time.sleep(5)
    return x * y
```


#### Running the Celery worker server

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
--- * ***  * -- Linux-3.10.0-693.el7.x86_64-x86_64-with-centos-7.4.1708-Core 2018-11-01 13:42:51
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x7fb82ad85518
- ** ---------- .> transport:   redis://localhost:6379/1
- ** ---------- .> results:     redis://localhost:6379/1
- *** --- * --- .> concurrency: 2 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . tasks.add
  . tasks.mul

[2018-11-01 13:42:51,428: INFO/MainProcess] Connected to redis://localhost:6379/1
[2018-11-01 13:42:51,453: INFO/MainProcess] mingle: searching for neighbors
[2018-11-01 13:42:52,504: INFO/MainProcess] mingle: all alone
[2018-11-01 13:42:52,516: INFO/MainProcess] celery@localhost.localdomain ready.
```


#### Calling the task 另个终端窗口

要调用我们的任务，可以使用delay()方法。

这是apply_async()方法的一个快捷方式，可以更好地控制任务执行(参见[调用任务](http://docs.celeryproject.org/en/latest/userguide/calling.html#guide-calling))。

```bash
cd ~
source ver/bin/activate
cd /home/wwwroot/celery/app1/
```

```python
>>> from tasks import add
>>> result = add.delay(4, 4)
>>> result # result是个对象，要通过get()或者.result打印结果
<AsyncResult: 85d9866d-1e27-4552-8427-99ef43d92e12>
>>> result.ready() # 通过ready()和.status查看任务的执行状态
True
>>> result.status
'SUCCESS'
>>> result.get(timeout=1)
8
>>> result.get(propagate=False)
8
>>> result.traceback
>>>
```

```bash
(ver) [root@localhost app1]# pwd
/home/wwwroot/celery/app1
(ver) [root@localhost app1]# tree
.
├── client.py
└── tasks.py

0 directories, 2 files
```

程序执行： vim client.py
```python
import time

from tasks import add,mul

add_ret = add.delay(4, 4)
mul_ret = mul.delay(5, 5)

while not add_ret.ready():
    time.sleep(1)
    print("waiting for task to be done")
print('add task done: {0}'.format(add_ret.get()))

while not mul_ret.ready():
    time.sleep(2)
    print("waiting for task to be done")
print('mul task done: {0}'.format(mul_ret.get()))
```

```bash
# python client.py 
waiting for task to be done
add task done: 8
waiting for task to be done
waiting for task to be done
waiting for task to be done
mul task done: 25
```
