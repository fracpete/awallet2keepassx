import os
import sys
import csv
import datetime

"""
Expects parameters:
- directory with awallet CSV export files
- output keepass XML file
"""

input_dir = sys.argv[1]
output_xml = sys.argv[2]

try:
    ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    print("saving XML to: " + str(output_xml))
    output_file = open(output_xml, 'w')
    output_file.write('<!DOCTYPE KEEPASSX_DATABASE>\n')
    output_file.write('<database>\n')
    for input_file in os.listdir(input_dir):
        if not input_file.lower().endswith(".csv"):
            continue
        print("loading: " + input_file)
        group = input_file[0:-4]
        output_file.write(' <group>\n')
        output_file.write('  <title>' + group + '</title>\n')
        group = group.lower()
        if group.find('web') > -1:
            icon = '1'
        elif group.find('e-shop') > -1:
            icon = '1'
        elif group.find('credit') > -1:
            icon = '66'
        elif group.find('banking') > -1:
            icon = '66'
        elif group.find('email') > -1:
            icon = '19'
        else:
            icon = '0'
        output_file.write('  <icon>' + icon + '</icon>\n')
        with open(input_dir + os.path.sep + input_file) as in_file:
            reader = csv.reader(in_file, delimiter=',', quotechar='"')
            header = None
            for row in reader:
                if header is None:
                    header = row
                    bank = False
                    cc = False
                    if 'Bank' in header:
                        bank = True
                    elif 'Card name' in header:
                        cc = True
                    continue

                output_file.write('  <entry>\n')

                if bank:
                    print("bank")
                    icon = '66'
                    output_file.write('   <title>' + row[header.index('Bank')] + '</title>\n')
                    output_file.write('   <username>' + row[header.index('Name')] + '</username>\n')
                    output_file.write('   <password>' + row[header.index('Password')] + '</password>\n')
                    output_file.write('   <comment>' + row[header.index('Note')] + '</comment>\n')

                elif cc:
                    print("cc")
                    icon = '66'
                    output_file.write('   <title>' + row[header.index('Card name')] + '</title>\n')
                    output_file.write('   <username>' + row[header.index('Card Number')] + '</username>\n')
                    output_file.write('   <password>' + row[header.index('Pin')] + '</password>\n')
                    comment = ""
                    fields = ['Holder', 'Security Code', 'Expiration']
                    for field in fields:
                        if len(row[header.index(field)]) > 0:
                            comment += '\n' + field + ': ' + row[header.index(field)]
                    output_file.write('   <comment>' + comment.strip() + '</comment>\n')
                    
                else:
                    print("other")
                    icon = '0'
                    output_file.write('   <title>' + row[0] + '</title>\n')
                    output_file.write('   <username>' + row[1] + '</username>\n')
                    output_file.write('   <password>' + row[2] + '</password>\n')
                    if 'Note' in header:
                        output_file.write('   <comment>' + row[header.index('Note')] + '</comment>\n')

                if 'Web Site' in header:
                    output_file.write('   <url>' + row[header.index('Web Site')] + '</url>\n')
                output_file.write('   <icon>' + icon + '</icon>\n')
                output_file.write('   <creation>' + ts + '</creation>\n')
                output_file.write('   <lastaccess>' + ts + '</lastaccess>\n')
                output_file.write('   <lastmod>' + ts + '</lastmod>\n')
                output_file.write('   <expire>never</expire>\n')
                output_file.write('  </entry>\n')
                
        output_file.write(' </group>\n')
    output_file.write('</database>\n')
finally:
    output_file.close()

