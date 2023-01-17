import json
import argparse
import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
c = conn.cursor()
with open("bugs.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_sql('bugs', conn)

domain_map = {
'dbms' : 'Database Management Systems'
}


print('<div class="container">')

for domain, count in c.execute('SELECT domain, COUNT(*) FROM bugs GROUP BY domain;').fetchall():
    print('\t<h2>%s (%d bugs)</h2>' % (domain_map[domain], count))
    for system, count in c.execute(("SELECT system, COUNT(*) FROM bugs WHERE domain = '%s' GROUP BY system") % (domain,)).fetchall():
        print('\t<h3>%s (%d bugs)</h3>' % (system, count))
        for title, url, found_by in c.execute(("SELECT title, url, reported_by FROM bugs WHERE domain='%s' AND system='%s';") % (domain, system)).fetchall():
            print('\t\t<details>')
            print('\t\t\t<summary>%s</summary>'% (title, ))
            print('\t\t\tLink: <a href="%s">%s</a> <br />' % (url, url))
            print('\t\t</details>')

print('</div>')