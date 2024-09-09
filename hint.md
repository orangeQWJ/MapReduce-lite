# worker

# master

# worker




# 编程范式

业务诉求是统计文本中所有字符的数量
```python
def map(filename):
	...
	Emit(k,v)

"""
a:1
a:1
b:1
b:1
c:1


x:1
y:1
z:1


"""
		
def reduce(key, value_list):
	return key, len(value_list)



reduce("a", [1,1])
reduce("b",[1,1])

reduce("x",[1])
....

```

# 分布式计算框架

> 在局域网内, 每个节点都有自己的ip地址

import sourcefile

go 动态链接 .o

Job
M task
R task

map 阶段, reduce 阶段.

M = 2
R = 4

mapreduce  配合 gfs
文件传输

## 文件的位置

- 绝对路径
- ip, port


## client 

hugefile -> split

1. m-0
2. m-1

拉取 r1 r2 r3


## master
单点故障
性能瓶颈

先忽略

0-0 0-1 0-2 0-3

1-0 1-1 1-2 1-3


[ r1, r2 ,r3]


jobID
 uuid   产生一个唯一的ID

```python
job_Dict[uuid] {
	status done

}
```

jobQueue

taskQueue
	 {m-1-task}  {r-0}	{r-1}


workerQueue
	 {ip, port} {ip, port}
	



{task, worker}



## worker1

- m-0 (26字母都有)

产生 巨量的 k,v

hash(k) % R

r-0-0      a,b,c
r-0-1      x,y,z
r-0-2      j,k,l
r-0-3	   m,o,n

---
0-3
1-3

r3
	m:3
	o:78
	n:79

## worker2

- m-1

产生 巨量的 k,v

hash(k) % R

r-1-0      a,b,c
r-1-1      x,y,z
r-1-2      j,k,l
r-1-3	   m,o,n

---
0-2
1-2

j:10
k:11
l:12

## worker3
0-0
1-0


## worker4
0-1
1-1
