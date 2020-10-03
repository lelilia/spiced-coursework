
1. Create a new directory secret_chamber/
```bash
$ mkdir secret_chamber
$ cd secret_chamber
```
2. Create an empty text file chest inside it
```bash
$ touch chest.txt
```
3. Store the word *treasure* inside the chest file
```bash
$ echo 'treasure' > chest.txt
```
4. Lock the chest: remove read/write permission for everybody
    ([found here](https://www.macinstruct.com/node/415))
```bash
$ chmod 000 chest.txt
```
5. Step out of the chamber to the parent directory
```bash
$ cd ..
````
6. Hide the chamber by renaming it to .secret_chamber/
```bash
$ mv secret_chamber .secret_chamber
````
7. Read the contents of the ches
```bash
$ cat .secret_chamber/chest.txt
```
