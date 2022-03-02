#! /usr/bin/python3
#
import os
import regex
import sys
import platform
import json

if len(sys.argv) != 3:
    exit('script <diretorio> <extensao>')

if platform.system() == "Linux":
    pattern = '.*\s.*\s.*\s+.*\s+([0-9]+)\s+([0-9]+)\s(.*)'
else:
    pattern = '.*\s.*\s.*\s[0-9]+\s+([0-9]+)\s([0-9]+)\s(.*)'

diretorio = sys.argv[1]
extensao = sys.argv[2]


def getDirList(dire, exte):
    final = []
    comando = "ls {} -ltr --time-style='+%s' | grep {}".format(dire, exte)
    res = os.popen(comando).read()

    for row in res.split('\n'):
        if row:
            iSplited = (regex.split(pattern, row))
            final.append({
                '{#SIZE}': iSplited[1],
                '{#UPTIME}': iSplited[2],
                '{#NAME}': iSplited[3],
            })
    return final


def main():
    print(json.dumps(getDirList(diretorio, extensao)))


if __name__ == "__main__":
    main()
