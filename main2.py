#! /usr/bin/python
import os
import regex
import sys
import json
import platform

if len(sys.argv) != 3:
    exit('script <diretorio> <extensao>')

# diretorio = sys.argv[1]
# extensao = sys.argv[2]
diretorio = '/var/log/'
extensao = 'gz'

print(platform.sys())
exit()
pattern = '.*\s.*\s.*\s[0-9]+\s+([0-9]+)\s+([0-9]+)\s(.*)'


def getDirList(dire, exte):
    final = []
    comando = "ls {} -ltr --time-style='+%s' | grep {}".format(dire, exte)

    print(comando)

    res = os.popen(comando).read()

    for row in res.split('\n'):
        if row:
            iSplited = (regex.split(pattern, row))
            print(iSplited)
            """ final.append({
                '{#SIZE}': iSplited[1],
                '{#UPTIME}': iSplited[2],
                '{#NAME}': iSplited[3],
            }) """
    return final


def main():
    print(getDirList(diretorio, extensao))


if __name__ == "__main__":
    main()
