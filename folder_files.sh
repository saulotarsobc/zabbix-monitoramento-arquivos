#! /bin/bash
alert(){
    echo -e "./SCRIPT_NAME <DIRECTORY> <['FILE_EXTENSION'(mp3 | mp4 | ixc) | '*'(for all extensions)]>";
    echo -e "Ex: ./SCRIPT_NAME /home/musics mp3";
    echo -e "Ex: ./SCRIPT_NAME /home/downloads *";
    exit 0;
}

if [ "$1" = "" ]; then alert; fi;
if [ "$2" = "" ]; then alert; fi;

names=($(ls $1 -ltr --time-style='+%s' |grep ".$2" |sed -r -e 's/.*\s[0-9]+\s[0-9]+\s(.*)/\1/'));
sizes=($(ls $1 -ltr --time-style='+%s' |grep ".$2" |sed -r -e 's/.*\s([0-9]+)\s[0-9]+\s.*/\1/'));
dates=($(ls $1 -ltr --time-style='+%s' |grep ".$2" |sed -r -e 's/.*\s[0-9]+\s([0-9]+)\s.*/\1/'));

ID=0;
timestamp=$(date '+%s');

echo "id|nome|size|uptime";
for i in "${names[@]}";

do
    uptime=$(( timestamp - ${dates[$ID]} ));
    echo "$ID|${names[$ID]}|${sizes[$ID]}|$uptime";
    let ID=ID+1;
done;