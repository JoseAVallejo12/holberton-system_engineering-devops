# Command line for the win
![img](https://cdn.pixabay.com/photo/2013/07/13/13/41/bash-161382_960_720.png)
<h1><img src='https://cdn.pixabay.com/photo/2019/11/28/14/31/nintendo-4659315_960_720.png' width=200> Background Context </h1>

CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

## Requirements
General
- A README.md file, at the root of the folder of the project, is mandatory
- This project will be manually reviewed.
- As each task is completed, the name of that task will turn green
- Create a screenshot, showing that you completed the required levels
- Push this screenshot with the right name to Github, in either the PNG or JPEG format

## Task 0 (🐌):
Print "hello world". Hint: There are many ways to print text on the command line, one way is with the 'echo' command. Try it below and good luck!
```
usage:
echo hello world

Other:
echo hello\ world
echo "hello world";
cat<<<"hello world"
echo -e hello world
cat<<< "hello world"
printf "hello world"
cat <<<"hello world"
cat <<<'hello world'
printf "hello world\n"
printf '%s\n' 'hello world'
dash -c 'echo "hello world"'
printf \%s 'hello ' $'world\n'
export b="hello world"; echo $b
perl -e 'print("hello world\n")'
awk 'BEGIN {print "hello world"};'
awk 'END {print "hello world"}' /dev/null
echo "something different" | awk '{print "hello world"}'
```

## Task 1 (🦋):
Print the current working directory.
```
Usage:
pwd

Other:
pwd -L
pwd cwd
pwd ../
/bin/pwd
pwd user
echo |pwd
echo $PWD
pwd 'dir'
echo $PWD;
echo | pwd
echo `pwd`
realpath .
echo $(pwd)
echo ${PWD}
readlink -f .
pwd is /bin/pwd
pwd 'hello world'
printf \%s\\n "$PWD"
pwd home cmdchallange
```

# Task 2 (:bug:)
List names of all the files in the current directory, one file per line.
```
Usage:
ls

Other:
ls *
ls .
ls ./
ls -h
ls -k
ls -X
ls -t
ls -G
ls -A
ls --
ls -q
ls -p
ls -1
ls -S
find *
```

## Task 3 (🐜):
There is a file named access.log in the current directory. Print the contents.
```
Usage:
cat access.log

Other:
cat *.log
cat acces*
pg access.log
cat<access.log
cat access.log
head access.log
tail access.log
cat *access.log
cat ./access.log
cat "access.log"
cat < access.log
head -100 access.log
tac access.log | tac
```

## Task 4 (🕸)
Print the last 5 lines of "access.log".
```
Usage:
cat access.log | tail -n 5

Other:
tail access.log --lines=5
tail --lines 5 access.log
tail access.log --lines 5
cat access.log | tail -n5
cat access.log |tail -n 5
cat | tail -n 5 access.log
cat access.log | tail -n 5
grep 5 access.log | tail -5
ls -t | tail -n 5 access.log
awk 'NR>=6 && NR<=10' access.log
```

## Task 5 (🐝)
There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET".
```
Usage:
cat access.log | grep "GET"

Other:
cat access.log | egrep GET
cat |grep 'GET' ./access.log
cat | grep -r GET access.log
grep "GET" access.log | more
grep "GET" access.log
```


## Task 6 (🐞)
Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".
```
Usage:
grep -nRl "500"

Other:
grep -R 500 -l
egrep -l 500 *
grep -lR "500"
grep -ll 500 *
grep -wls 500 *
grep "500" -l *
grep -rl -e '500'
grep -rl * -e 500
grep -Ril "500" *
grep "500" *.* -l
grep -l 500 $(ls)
ls | grep -rl 500
grep -l "500" *.*
grep -rwl -e "500"
grep -Ril -e '500'
```

## Task 7 (🦗):
Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.
```
Usage:
find . -name 'access.log*'

Other:
ls -S | grep access
ls | grep "access*"
ls -a | grep access
ls -1 ./access.log*
ls -rtd access.log*
find -L access.log*
ls | grep access.log
ls -1d ./access.log*
ls access.log* | sort
ls |grep "access.log"
ls | grep $access.log
find . -name "access*"
find | grep access.log
find . |grep access.log
find . -name "access.*"
ls -1 | grep access.log
ls | grep "access.log*"
ls | grep '^access.log'
find . | grep access.log
find access.log* | ls -1
```

## Task 8 (🕷):
Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".

Note that there are no files named access.log in the current directory, you will need to search recursively.
```
Usage:
grep -rwh -e "500"

Other:
grep -Rh 500 ./
egrep -rh 500 *
grep -rhw 500 *
grep -hR "500" .
grep -Rh 500 ./*
grep -r -h "500"
grep "500" -r -h
grep -Rh -e "500"
grep -R 500 ./ -h
grep -irh 500 var
grep -ihr "500" *
grep -rhe '500' .
grep -r -h '500' *
grep -iRh "500" ./
```

## Task 9 (🦂):
Extract all IP addresses from files that start with "access.log" printing one IP address per line.
```
Usage:
grep -oRPh "[\d.]{11,15}" *

Other:
grep -hRi HTTP | cut -f1 -d" "
grep -roP "\d+\.\d+\.\d+\.\d+"
grep -rhoE '([0-9]*\.){3}[0-9]*'
awk '{ print $1 }' **/access.log*
grep -Rh ' ' ./ | cut -d ' ' -f 1
grep -hr "[0-9]*" | cut -d" " -f1
egrep -rnho '^[0-9.]+' .|sort|uniq
grep -h -r \. | sed 's/\ \(.*\)//'
cat **/access.log* | cut -d' ' -f1
cat var/log/httpd/*|cut -d ' ' -f 1
cat **/access.log* | cut -d ' ' -f 1
egrep -Rho '^[0-9.]+' **/access.log*
grep -r -h "\." | sed 's/\s\(.*\)//'
grep -roP '([0-9]{1,3}\.){3}[0-9]{1,3}'
egrep '[0-9]{1,3}\.' -r | cut -d" " -f1
```

## Task 10 (🦟):
Delete all of the files in this challenge directory including all subdirectories and their contents.
```
Usage:
rm -r ./* ./.*

Other:
rm -r $(ls -a)
rm -r $(ls -A)
rm -r .[^.]* *
rm -rf * .[^.]*
rm -rf ./* ./.*
rm -r * .[a-z]*
rm -r $(find .)
rm -rf ${pwd}/*
rm -rf .[^.]* *
```

## Task 11 (🐝):
Count the number of files in the current working directory. Print the number of files as a single integer.
```
Usage:
find . -type f | wc -l

Other:
echo $(ls -l|wc -l)
find . -type f | wc -l
find . -type f | wc -ll
ls -al | grep ^- | wc -l
ls -la | grep ^- | wc -l
find -L . -type f | wc -l
ls -a | expr $(wc -l) - 2
ls -l | grep -v ^d | wc -l
find . -mindepth 1 | wc -l
ls -l | grep -v ^l | wc -l
```

## Task 12 (🐍):
Print the contents of access.log sorted.
```
Usage:
cat  access.log | sort

Other:
sort access.log
cat access.log |sort
cat access.log | sort
sort access.log | cat
cat access.log | sort -s
cat access.log | sort -u
cat `find . -name access.log` | sort
find . -name "access.log" | sort access.log
find "access.log" -type f -exec cat {} + | sort
```

## Task 13 (🦠):
Print the number of lines in access.log that contain the string "GET".
```
Usage:
cat access.log | grep "GET" | wc -l

Other:
grep -c "GET" *
grep G a* | wc -l
grep -R GET | wc -l
grep GET access.log -c
grep GET access.log|wc -l
grep GET access.log |wc -l
grep -c 'GET' ./access.log
grep GET access.log | wc -l
grep --count GET access.log
grep access.log -e "GET" -c
grep GET access.log | wc -ll
grep -i get access.log|wc -l
cat access.log|grep GET|wc -l
cat access.log | grep -c "GET"
grep access.log -e GET | wc -l
grep -o GET access.log | wc -l
grep -n GET access.log | wc -l
cat access.log | grep "GET" -c
cat access.log| grep GET| wc -l
grep -io get access.log | wc -l
```

## Task 14 (🙈):
The file split-me.txt contains a list of numbers separated by a ; character.
Split the numbers on the ; character, one number per line.
```
Usage:
cat split-me.txt | tr ';' '\n'

Other:
cat split-me.txt| tr ':;' '\n'
cat split-me.txt|sed 's/;/\n/g'
cat split-me.txt | tr '\;' '\n'
cat ./split-me.txt | tr ';' '\n'
sed -E 's/;/\n/g' < split-me.txt
sed -nr 's/;/\n/gp' split-me.txt
cat split-me.txt | sed 's/;/\n/g'
cat split-me.txt | sed 's|;|\n|g'
cat split-me.txt | sed 's_;_\n_g'
cat split-me.txt | tr -s ";" "\n"
```

## Task 15 (🐶):
Print the numbers 1 to 100 separated by spaces.
```
Usage:
echo {1..100}

Other:
seq 1 100 | xargs
seq 100 | paste -sd' '
seq 1 100 | xargs echo
echo $(echo $(seq 1 100))
seq 1 100 | tr '\n' ' ' | xargs
seq 1 99 | tr '\n' ' ' && echo 100
set -- {1..100} ; printf '%s\n' "$*"
seq 1 100 | tr '\n' ' ' | sed 's, $,\n,'
echo $(for i in {1..100};do echo $i;done)
perl -E 'print(join(" ", (1..100)), "\n")'
for i in {1..100}; do a="$a $i"; done; echo $a
for i in {1..100}; do echo -n "$i "; done | xargs
for j in {1..99}; do echo -n "$j "; done; echo 100
for i in {1..99}; do echo -n "$i "; done ; echo 100
for i in {1..99}; do echo -n "$i "; done && echo "100"
for i in $(seq 1 99); do echo -n "$i "; done; echo 100
```


## Task 16 (🐺):
There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.
```
Usage:
find . -name "*.doc" -type f -delete

Other:
find -type f -name "*.doc" -exec rm -rf {} +
find ./ -type f -name '*.doc' -exec rm {} \;
find -type f -name "*.doc" -exec rm -rf {} \;
find . -type f -iname "*.doc" -exec rm -f {} \;
```

## Task 17 (🦊):
This challenge has text files (with a .txt extension) that contain the phrase "challenges are difficult". Delete this phrase recursively from all text files.

Note that some files are in subdirectories so you will need to search for them.
```
Usage:
sed -i 'challenge are difficult/d' **/*.txt


Other:
find -name \*.txt -exec sed -i '/challenges are difficult/d' {} \;
find **/*txt | xargs -d '\n' sed -i 's/challenges are difficult//g'
find -name '*.txt' -exec sed -i '/challenges are difficult/d' {} \;
find -iname '*.txt' -exec sed -i '/challenges are difficult/d' {} +
```

## Task 18 (🐱):
The file sum-me.txt has a list of numbers, one per line. Print the sum of these numbers.
```
Usage:
awk ' {s+=$1} END { print s }' sum-me.txt


Other:
perl -lne '$z+=$_; END { print $z }' sum-me.txt
cat sum-me.txt | xargs | sed -e 's/\ /+/g' | bc
awk 'BEGIN{a=0};{a+=$1};END{print a}' sum-me.txt
awk '{total += $1} END {print total}' sum-me.txt
```

## Task 19 (🦁):
Print all files in the current directory recursively without the leading directory path.
```
Usage:
find * -type f -printf '%f\n'

Other:
find * -type f -printf '%f\n'
find * -type f | sed 's,.*/,,'
find ./ -type f -printf "%f\n"
find -type f -exec basename {} \;
find . -type f|xargs -n1 basename
find . -type f -exec basename '{}' \;
find -type f | rev | cut -d/ -f1 | rev
find -type f -execdir basename '{}' ';'
find . -type f | awk -F / '{print $NF}'
```

## Task 20 (🐯):
Rename all files removing the extension from them in the current directory recursively.
```
Usage:
find $PWD -type f -exec rename 's/\..*$//' {} \;

Other:
find . -type f -exec rename 's/\.[a-z]+$//' {} \;
for f in $(find -type f); do mv "$f" ${f%.*}; done
for i in $(find . -type f );do mv $i "${i%.*}";done
find . -type f -exec rename 's/(.*)\..*/\1/' \{} \;
find -type f -exec bash -c 'mv "$0" "${0%.*}"' {} \;
for i in `find . -type f`; do mv "$i" "${i%.*}"; done
for i in $(find . -type f); do mv ${i} ${i%.*}; done; ls
find . -type f | while read i; do mv $i "${i%.*}"; done;
```

## Task 21 (🐴):
The files in this challenge contain spaces. List all of the files (filenames only) in the current directory but replace all spaces with a '.' character.
```
Usage:
find * -type f | tr ' ' '.'

Other:
find * -type f | sed 's| |\.|g'
ls | awk '{gsub(" ", "."); print}'
find -type f| sed ' s|.*/|| ; s/ /./g '
find -type f -printf "%f\n" | tr ' ' '.'
find . -type f -printf "%f\n" | tr ' ' '.'
find . -type f -printf '%f\n' | sed 's/ /./g'
for f in *; do printf %s\\n "${f// /.}"; done
find ./ -type f -printf "%f\n" | sed 's/ /./g'
for i in *; do printf \%s\\n "${i// /.}"; done
```


## Task 22 (🦄):
In this challenge there are some directories containing files with different extensions. Print all directories, one per line without duplicates that contain one or more files with a ".tf" extension.
```
Usage:
find -name "*.tf" | xargs dirname | uniq

Other:
find -name '*.tf' -exec dirname '{}' \; | uniq
find -name '*.tf' -printf '%h\n' | sort | uniq
find -type f -name "*.tf" -printf "%h\n" | uniq
find . -name '*.tf' -printf '%h\n' | sort | uniq
find -iname '*.tf' -type f -printf '%h\n' | uniq
find . -name *.tf -type f | xargs dirname | uniq
find . -iname "*.tf" -exec dirname '{}' \; | uniq
find . -iname '*.tf' -printf '%h\n' | sort | uniq
find . -type f -name '*.tf' -printf '%h\n' | uniq
find -type f -name "*.tf" -printf "%h\n" | sort -u
find ./ -type f -name "*.tf" -printf "%h\n" | uniq
```




## Task 23 (🐮):
There are a mix of files in this directory that start with letters and numbers. Print the filenames (just the filenames) of all files that start with a number recursively in the current directory.
```
Usage:
find . -type f -name "[0-9]*" -printf '%f\n'

Other:
find . -type f -printf '%f\n' | grep '^[0-9]'
find ./ -name "[0-9]*" -type f -printf "%f\n"
find * -type f -name '[0-9]*' | sed 's|.*\/||'
find ./ -name "[0-9]?*" -type f -printf "%f\n"
find -type f -printf '%f\n' | grep -P '^[0-9]'
find . -type f -name '[0-9]*' | sed "s#^.*/##g"
find -type f -name '[0-9]*' -exec basename {} \;
find . -type f -printf "%f\n" | grep -E "^[0-9]"
find ./ -type f -printf "%f\n" | grep -e "^[0-9]"
find . -type f -name '[[:digit:]]*' -printf '%f\n'
find . -type f -name "[0-9]*" -exec basename {} \;
find . -type f -printf '%f\n' | grep -P '^[0-9].*'
find -type f -name '[0-9]*' -exec basename -a {} +
```


## task 24 (🐷):
Print the 25th line of the file faces.txt
```
Usage:
cat faces.txt | head -n 25 | tail -n -1

Other:
head -n 25 faces.txt|tail -n 1
head -n 25 faces.txt | tail -1
head -n 25 faces.txt |tail -n 1
head -n 25 faces.txt | tail -n 1
head -n25 < faces.txt | tail -n1
tail -n +25 faces.txt | head -n 1
cat faces.txt | head -n 25 | tail -1
cat faces.txt | tail -n+25 | head -1
cat faces.txt | head -n25 | tail -n1
perl -lne 'print if $.== 25' faces.txt
cat faces.txt | awk '{if (NR == 25) print $0}'
awk 'BEGIN {nlines = 0} {nlines++; if (nlines == 25) print $0}' faces.txt
```


## Task 25 (🐭):
Print the lines of the file reverse-me.txt in this directory in reverse line order so that the last line is printed first and the first line is printed last.

In the future
Environmental destruction will be the norm
No longer can it be said that
My peers and I care about this earth
It will be evident that
My generation is apathetic and lethargic
It is foolish to presume that
There is hope

-Jonathan Reed "The Lost Generation"
```
Usage:
cat reverse-me.txt

Other:
tac -r reverse-me.txt
cat reverse-me.txt |tac
cat reverse-me.txt | tac
sed '1!G;h;$!d' reverse-me.txt
sed -n '1!G;h;$p' reverse-me.txt
perl -e 'print reverse <>' reverse-me.txt
awk '{a[i++]=$0} END {for (j=i-1; j>=0;) print a[j--] }' reverse-me.txt
awk '{lines[NR]=$0;} END{for (i=NR; i>0; i-=1) print lines[i]}' reverse-me.txt
awk '{print NR , $0}' < reverse-me.txt | sort -rn | awk '{print substr($0,length($1)+2)}'
```

## Task 26 (🐹):
Print the file faces.txt, but only print the first instance of each duplicate line, even if the duplicates don't appear next to each other.

Note that order matters so don't sort the lines before removing duplicates.
```
Usage:
awk '!x[$0]++' faces.txt

Other:
cat faces.txt | awk '!x[$0]++'
awk '!visited[$0]++' faces.txt
cat faces.txt | awk '!seen[$0]++'
awk '{if (!a[$0]) print;a[$0]=1}' faces.txt
cat -n faces.txt|sort -uk2|sort -nk1| cut -f2-
cat -n faces.txt | sort -uk2 | sort -n | cut -f2
```
