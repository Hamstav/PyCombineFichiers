# coding: utf8
import os
import codecs
import sys
os.chdir('D:\Hamstav\Projetbus')
with open("out.txt", "a", encoding="utf-8") as out:
    for dirname, dirnames, filenames in os.walk('.'):
        for filename in filenames:   
            if '.html' in filename:
                with open(os.path.join(dirname, filename), "rt", encoding="utf-8") as html:
                    contenu = "<fichier>"+os.path.join(dirname, filename)+"<contenu>"+html.read()+"<fin>"
                    contenu2 = contenu.encode('utf-8')
                #print(os.path.join(dirname, filename))
                #sys.stdout.buffer.write(contenu2)
                out.write(contenu + '\n')
                html.close()
out.close()
