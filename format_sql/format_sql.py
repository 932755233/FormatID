
import fileinput

path = 'format_sql_txt'

for line in fileinput.input(path, openhook=fileinput.hook_encoded('utf-8')):
    if line[0:1]=='	':
        print('.append("'+line[1:-1]+'\\n")')
    else:
        print('.append("'+line[0:-1]+'\\n")')
