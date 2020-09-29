# 0x17. Web stack debugging #3
For this project, students are expected to look at these concepts:
## Background Context
- [Web Server](https://intranet.hbtn.io/concepts/17)
- [Web stack debugging](https://intranet.hbtn.io/concepts/68)
<p align="center"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png"></p>
When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.

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

## More Info
### **Install puppet-lint**
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```
## **command used for fix**
### show all proccess running
```
root@43a0713fd2d2:~# ps -auxf                                                                           
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  17956  2880 ?        Ss   18:04   0:00 /bin/bash ./tmp/run.sh
root        15  0.0  0.1  61380  5352 ?        S    18:04   0:00 /usr/sbin/sshd -D
root       585  0.0  0.1  66012  5632 ?        Ss   18:04   0:00  \_ sshd: root@pts/0
root       587  0.0  0.0  19920  3632 pts/0    Ss   18:04   0:00      \_ -bash
root       598  0.0  0.0  17248  2456 pts/0    R+   18:04   0:00          \_ ps -auxf
root        66  0.0  0.5 276396 21460 ?        Ss   18:04   0:00 /usr/sbin/apache2 -k start
www-data    95  0.0  0.1 276420  7432 ?        S    18:04   0:00  \_ /usr/sbin/apache2 -k start
root        70  0.0  0.0   4444  1624 ?        S    18:04   0:00 /bin/sh /usr/bin/mysqld_safe
mysql      418  0.6  1.6 574652 66892 ?        Sl   18:04   0:00  \_ /usr/sbin/mysqld --basedir=/usr --droot@43a0713fd2d2:~#
```
### Attach process by PID
```
root@43a0713fd2d2:~# strace -p 95
Process 70 attached
wait4(-1,
```

### in other terminal(tty2) run curl -sI 127.0.0.1:80
```
root@43a0713fd2d2:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Tue, 29 Sep 2020 18:09:43 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html
root@43a0713fd2d2:~#
```

### list all system call in tty2
```
root@43a0713fd2d2:~# strace -c ls
                                                                     
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
0.00    0.000000           0        10           read                                                   
0.00    0.000000           0        24         1 open                                                   
0.00    0.000000           0        26           close                                                  
0.00    0.000000           0        23           fstat                                                  
0.00    0.000000           0        35           mmap                                                   
0.00    0.000000           0        14           mprotect                                               
0.00    0.000000           0         3           munmap                                                
0.00    0.000000           0         3           brk                                                    
0.00    0.000000           0         2           ioctl                                                  
0.00    0.000000           0         8         8 access                                                 
0.00    0.000000           0         1           execve                                                 
0.00    0.000000           0         2           getdents                                               
0.00    0.000000           0         2         2 statfs                                                 
0.00    0.000000           0         1           arch_prctl                                             
0.00    0.000000           0         1           openat                                               
------ ----------- ----------- --------- --------- ----------------                                     
100.00    0.000000                   155        11 total                                                
root@43a0713fd2d2:~#   
```
### find error in systemcall open that have one error in tty1
```
stat("/var/www/html/wp-includes/cache.php", {st_mode=S_IFREG|0644, st_size=22058, ...}) = 0
stat("/var/www/html/wp-includes/default-filters.php", {st_mode=S_IFREG|0644, st_size=25220, ...}) = 0
stat("/var/www/html/wp-includes/l10n.php", {st_mode=S_IFREG|0644, st_size=43130, ...}) = 0
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffc1ffd5480) = -1 ENOENT (No such file or directory)
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffc1ffd5350) = -1 ENOENT (No such file or directory)
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffc1ffd7580) = -1 ENOENT (No such file or directory)
/**syscall error output **/
open("/var/www/html/wp-includes/class-wp-locale.phpp", O_RDONLY) = -1 ENOENT (No such file or directory)
chdir("/")=0 
```
## find file
The extension in php file is php. That say it, is good find whare is set this name file "class-wp-locale.phpp"
```
root@43a0713fd2d2:~# grep -Rl .phpp /var                                                                                                         
grep: /var/run/mysqld/mysqld.sock: No such device or address                                                                                                     
/var/www/html/wp-includes/js/zxcvbn.min.js                                                                                                          
/var/www/html/wp-settings.php                                                                                                         
root@43a0713fd2d2:~#
```
## open file found
wp-setting.php for it be config file and change line 137 save, reset apache2
```
vim /var/www/html/wp-settings.php
~
~
134 
135 // Load the L10n
library.
136 require_once( ABSPATH . WPINC . '/l10n.php' );
137 require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );
138 require_once( ABSPATH . WPINC . '/class-wp-locale-switcher.php' );                                                                                                                                          139                                                                      
```
##  Test again and all done problem fix
```
root@43a0713fd2d2:~# curl -sI 127.0.0.1
HTTP/1.1 200 OK
Date: Tue, 29 Sep 2020 18:34:01 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8
root@43a0713fd2d2:~#
```
## write poppet solution file
```
# Fix wp-settings.php
exec { 'fix-wordpress-php-confg':
  command => '/bin/sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php',
}
```