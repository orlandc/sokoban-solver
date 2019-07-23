#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
FILE="${DIR}/mapa/map.txt"
RUNA="${DIR}/main.py"

echo -n >$FILE

while read line
do 
    echo "$line" >> $FILE
done

/usr/bin/python $RUNA $1