# Table of Contents
- [bash](#bash)
- [git](#git)
- [jupyter notebooks](#jupyter)
- [pandas](#pandas)
- [matplot](#matplot)
- [seaborn](#seaborn)

# <a name = 'bash'></a>bash commands

command | description
:--- | :---
`mkdir <folder>` | creates a new folder
`cd <folder>`| goes into the folder
`ls`| shows the files in your current folder
`ls <path>` | shows the files at path
`ls -l`| shows files with more detail
`mv <file/folder> <path>` | moves file or folder to the path 
`source <file.sh>`| runs bash script
`nano <file>` | opens file with bash text editor nano
`cat <file>`| shows content of the file in the terminal
`touch <file>`| creates empty file or updates the time stamp on an existing file
`rm <file>`| deletes file
`rm -r <folder>`| deletes empty folder
`rm -rf <folder>`| deletes folder


# <a name = 'git'></a>git commands
command | description
:--- | :---
`git clone <url>`| creates a local copy of the GitHub repository
`git status`| shows information about the status
`git add <file/folder> / . / --all`| stages specific files, or folders , the current directory or everything for commiting
`git commit -m 'message'`| commits changes to the local repo
`git pull origin main`| updates from the online repo
`git push origin main`| uploads commits to the online repo
`git log`| shows history on current branch
`git branch <branch>`| creates new branch
`git checkout -b` <branch> | creats new branch and switches to it 
`git checkout main`| switches to branch main
`git branch`| shows a list of all branches



# <a name = 'jupyter'></a>Jupyter Shortcuts

shortcut | description
:--- | :---
shift + Enter | runs cell
tab | shows attributes
shift + tab | shows info for function
Esc | exit editing, able to run commands
a | insert cell above
b | insert cell below
m | convert to markdown
y | convert to code
shift + m | merge cells
o | toggles output of selected cell

# <a name = 'pandas'></a>Pandas

### import 
`import pandas as pd`

### create a DataFrame from list
```python
data = [[1,2,3],
        [3,4,5]]
df = pd.DataFrame(data,
                  columns = ['col1', 'col2', 'col3'],
                  index = ['row1', 'row2])
```

command | description
:--- | :---
`pd.DataFrame`| basic data type in pandas
`df = pandas.DataFrame`| short for the future 
`df.head(x)`| shows the first x rows (default 5 when called without argument)
`df.tail(x)`| shows the last x rows
`df.info()`| lists columns and their types
`df.count()`| calculates number of non-empty rows
`df.sum()`| calculates the sum of each column
`df.shape()`| number of rows and columns
`df.to_numpy()`| creates a numpy array 
`df.columns`|list with column names
`df.index`|list with row names 
`df.index.name = 'new_name'`|renames the heading of the index column 

### Reading and Writing DataFrames
- `pd.read_csv('<file_path/file.csv>')`
- `pd.read_excel(<file_path/file.xlsx>)`
- `df.to_csv(df, '<file_path/file.csv>')`
- `df.to_excel(df, '<file_path/file.csv>')`
- `df.to_json(df, '<file_path/file.csv>')`

#### cleaning the read data
`df.columns = df.columns.asytpe(int)            # makes integer out of the column names`


### Selecting Rows and Columns

command | description
:--- | :---
`df[col]`| select 1 col as a pandas.Series
`df[[col]]`| selects 1 col as a DataFrame
`df[[col1, col2]]`| 2+ cols as DataFrame
`df.loc[row]`| select one row as Series by row name (index)
`df.loc[[row1, row2]]`| selects 1+ rows as a DataFrame by index
`df.loc[[row(s)], [col(s)]]`| selects sepcific row(s) and col(s) as a dataFrame
`df.iloc[a:b, c:d]`| selects by integer-index => numeric position of rows and cols 
`df.loc[df.col > x]`| select rows by logical condition
`df.loc[df.col.str.contains('a')]`| 
`df[col].str.lower()`| apply string function
`df[col] = x`| assign to existing or new column


### math operations on pandas Series (single columns)
```python
df.col.mean()               # calculates arithmetic mean of column
df.col.median()
df.col.val()                # calculates the variance of a column                 
df.col.max()
df.col.min()
df.col.std()
df.col.value_counts()       # create a relative frequency for a column
#df.col.count()
df.col.quantile(.25)
df.describe()               # calculates various descriptive statistics for each column
df.col1.corr(col2)          # calculates correlation between two columns
df.mode()
```


pandas.crosstab()	calculates a (relative) contingency/cross table for two columns

### plot forms

command |description
:--- | :---
df.plot() | line plot of each column
df.plot.bar() | one bar for each column
df.plot.scatter() | single scatterplot
df.hist() | histogram for each column
df.boxplot() | draws a boxplot for each column
pd.plotting.scatter_matrix() | draws a scatterplot matrix


# <a name = 'matplot'></a>MatPlotLib

### import 
```python 
import matplotlib.pyplot as plt
```
### save in file 
```python
df.hist()
plt.savefig('filename.png' [, dpi=value])
```

function | description
:--- | :---
plt.figure() |	creates an empty plot
plt.plot(x, y)|	creates a line or scatter plot
plt.bar(x, y)	|creates a bar plot
plt.pie(x)	|creates a pie chart
plt.axis((xmin, xmax, ymin, ymax))|	sets the x/y boundaries
plt.title('text')|	sets the title ==> it is possible to add latex in titles via r"$<latex>$"
plt.xlabel('text')|	sets the x-axis label
plt.ylabel('text')|	sets the y-axis label
plt.xticks(rotation = -45)   |     rotates the ticks for the x axis
plt.grid() | shows a grid 
plt.legend() | customizes the legend 


### plot arguments
```python
color = 'green'
alpha = 0.75                    # sets the solidness of the plot
figsize = (4,5)
orient = 'h'
marker = 'o'
linestyle = 'dashed'
linewidth = 2
markersize = 2
```
#### histograms
```python 
bins = 25               # number of bins 
histtype = 'bar' 
facecolor = 'green'
```

### legend
```python
plt.legend(loc = 'lower left'
```

# <a name = 'seaborn'></a>Seaborn 
```python 
import seaborn as sns
sns.boxplot(data = <data>)

```
### plot types
- sns.displot()  
*only for 0.11.0 and higher! might need to update seaborn*
- sns.boxplot()
- sns.countplot()
- sns.kdeplot()  
*kernel density estimation*
- sns.heatmap()
- sns.pairplot()

### plot arguments
```python
orient = 'h'            # orientation horizontal. by default vertical 
hue = '<column>'
col = '<column>'        # separats by column in different plots next to each other
multiple = 'stack'      # stacks the values on top of each other (good when the culminative total is important)
multiple = 'dodge'      # makes the bars smaller and next to each other
stat = 'density'        # normalizing
common_norm = False     # gives each subset its own normaization 
kind = 'kde'            # kernel density estimation
rug = True              # gives a small distribution on the side 
```

### pairplot
```python 
g = sns.PairGrid(penguins)
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot, fill = True)
g.map_diag(sns.histplot, kde = True)
```
