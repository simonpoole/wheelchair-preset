import polib
import re
import sys

data = {}

po = polib.pofile('i8n/preset_pt-rBR.po')
for entry in po.translated_entries():
    
    print(entry.msgid, entry.msgstr)
    if entry.msgid == 'translator-credits':
        continue
    for occurrence in entry.occurrences:
        occurrence = occurrence[0]
        result = re.search('[^:]*:([0-9]*)\(([^|]*)|.*', occurrence)
        line = int(result.group(1))
        tag , attr = result.group(2).split(':')
        print(" ", line, tag, attr)
        print(" ", occurrence)
        
        if line not in data:
            data[line] = []

        data[line].append({ 'tag': tag , 'attr': attr , 'msgid': entry.msgid , 'msgstr': entry.msgstr })

#print(data)
#print(data[20])
#sys.exit(0)

with open("wheelchair_master_preset.xml") as in_file:
    with open("wheelchair_master_preset_grafted.xml", "w") as out_file:
        for line, content in enumerate(in_file):
            line = line + 1
            if line in data:
                for entry in data[line]:
                    en = ' %s="%s"' % (entry['attr'], entry['msgid'])
                    z = '%s="%s"' % ('pt_BR.' + entry['attr'], entry['msgstr'])
                    content = content.replace(en, '%s %s' % (en, z))
            #out_file.write("%s\n" % content)
            out_file.write("%s" % content)

