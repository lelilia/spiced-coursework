### Bash Scripting

1. Write a bash script hello.sh that prints 'Hello World'
```bash
$ mkdir bash_scripting
$ cd bash_scripting
$ touch hello.sh
$ echo 'echo "hello world"' > hello.sh
```
2. Execute the program with source hello.sh
```bash
$ source hello.sh
````
3. Modify hello.sh to print a message given as an command-line argument (accessible via $1)
```bash
$ echo 'echo $1' > hello.sh
```
4. Test the script with source hello.sh 'Hello World'
```bash
$ source hello.sh 'Hello World'
````
5. Write another bash script that launches hello.sh 10 times with different messages
```bash
$ touch call_other_bash.sh
$ echo 'for i in {1..10}\ndo\tsh hello.sh "test $i"\ndone' > call_other_bash.sh
```
6. Execute everything
```bash
$ sh call_other_bash.sh
```
