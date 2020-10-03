# Pandas

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


# MatPlotLib

### import 
```python 
import matplotlib.pyplot as plt
```
### save in file 
```python
df.hist()
plt.savefig('filename.png')
```
