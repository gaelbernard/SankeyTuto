import pandas as pd

# Load Tabular format
df = pd.read_csv('grades.csv')

# Add the cumulative semester  in the name
df['Status'] = df['Status'] + ' (' + df['CumulativeSemester'].astype(str) + ')'

# We add a column with previous status. If empty we fill a default value 'start'
df['previousStatus'] = df.groupby('StudentID')['Status'].shift(1).fillna('start')

# We rename the columns because this is what the Sankey JS library is expecting (Sankey)
df['from'] = df['previousStatus']
df['to'] = df['Status']

# Count the number of students that went from one status to another
# (no need to group by cumulative semester because the information is in the name)
df = df.groupby(['from', 'to'])['StudentID'].count().rename('value').reset_index()

# Export to json
df.to_json('grades.json', orient='records')


