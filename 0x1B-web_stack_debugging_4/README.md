# 0x1B. Web stack debugging #4
<p align="center"> <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/313/frdkCrb.jpg"></p>

## Requirements
## General
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp
- Files will be checked with Puppet v3.4

## Install puppet-lint
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

# How Fix the code
- 1. Install strace inspect the systemcall failure
```
sudo apt install strace
strace -c ls
root@eda09a18e277:~# strace -c ls                                                                   
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
0.00    0.000000           0        10           read
0.00    0.000000           0         1           write
0.00    0.000000           0        24         1 open
0.00    0.000000           0        26           close
0.00    0.000000           0        24           fstat
0.00    0.000000           0        35           mmap
0.00    0.000000           0        14           mprotect
0.00    0.000000           0         4           munmap
0.00    0.000000           0         3           brk
0.00    0.000000           0         2           ioctl
0.00    0.000000           0         8         8 access
0.00    0.000000           0         1           execve
0.00    0.000000           0         2           getdents
0.00    0.000000           0         2         2 statfs
0.00    0.000000           0         1           arch_prctl
0.00    0.000000           0         1           openat
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000                   158        11 total
root@eda09a18e277:~#
```

## Open the file error.log for nginx
```
root@eda09a18e277:~# cat /var/log/nginx/error.log  | tail -3
2020/10/05 14:19:34 [crit] 32#0: *1999 open() "/usr/share/nginx/html/index.html" failed (24: Too many open files), client: 127.0.0.1, server: localhost, request: "GET / HTTP/1.0", host: "localhost"
2020/10/05 14:20:52 [emerg] 142#0: epoll_create() failed (24: Too many open files)
2020/10/05 14:20:52 [alert] 138#0: worker process 142 exited with fatal code 2 and cannot be respawned
root@eda09a18e277:~# 
```
## Google it problem:
Your operating system set limits on how many files can be opened by nginx server.
You can easily fix this problem by setting or increasing system open file limits under Linux. Edit file /etc/default/nginx, and inclease value of UNLIMIT var:
create puppet file for change value var and restart nginx.
```
puppet apply 0-the_sky_is_the_limit_not.pp
Notice: Compiled catalog for eda09a18e277.ec2.internal in environment production in 0.02 seconds
Notice: Finished catalog run in 1.10 seconds
```
## Test finsh
```
Server Software:		nginx/1.4.6
Server Hostname:		localhost
Concurrency Level:      100
Time taken for tests:   0.171 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      1706000 bytes
HTML transferred:       1224000 bytes
Requests per second:    11681.63 [#/sec] (mean)
Time per request:       8.560 [ms] (mean)
Time per request:       0.086 [ms] (mean, across all concurrent requests)
Transfer rate:          9730.89 [Kbytes/sec] received
```                                                                                                                                                              ```
