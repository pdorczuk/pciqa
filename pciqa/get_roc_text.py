import docx2txt
import globals as g

for word_doc in g.WORKDIR.glob('*.docx'):
    with open(f"{g.WORKDIR}\\{word_doc.stem}.txt", 'w', encoding='utf8') as f:
        f.write(docx2txt.process(word_doc))