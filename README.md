# Monitoramento de arquivos e diretórios como Zabbix

---

## Como usar?

```sh
mkdir /home/scripts
cd /home/scripts
wget https://raw.githubusercontent.com/saulotarsobc/zabbix-monitoramento-diretorios-arquivos/main/folder_files
chmod +x folder_files
```

> /home/scripts/folder_files <'/home/folder_name'> <'regex'>

```sh
/home/scripts/folder_files /var/www/zbxtlg/ *
```

![exemplos](img/ex1.png)

```sh
/home/scripts/folder_files /var/www/zbxtlg/ .png
```

![exemplos](img/ex2.png)

```sh
/home/scripts/folder_files /var/www/ login
```

![exemplos](img/ex3.png)

---

## UserParameter

```sh
nano /etc/zabbix/zabbix_agentd.conf -l
```

> UserParameter=folder_files[*],/home/scripts/folder_files $1 $2

![user parameters](img/user%20param.png)

```sh
zabbix_agentd -t folder_files[<folder>,<regex>]
```

> Ex: zabbix_agentd -t folder_files[/var/www/bkp,ixc]

---

## Script

```sh
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
```
