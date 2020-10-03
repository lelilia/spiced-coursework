## Spices

1. Create a new directory fruit/
```bash
$ mkdir spices
$ cd spices
$ mkdir fruit
````
2. Create 7 empty text files like apple, banana, etc.
```bash
$ cd fruit
$ touch apple banana cherry kiwi pineapple strawberry melone
```
3. Store all file names in a text file
```bash
$ touch ../all_names.txt
$ ls -1 * > ../all_names.txt
````
4. List all file names that contain the letter a
```bash 
$ ls *a*
````
5. Store the names with a in a text file
```bash
$ touch ../names_with_a.txt
$ ls -1 *a* > ../names_with_a.txt
````
6. Use diff to find all file names not containing an a
```bash
$ diff ../all_names.txt ../names_with_a.txt
```
