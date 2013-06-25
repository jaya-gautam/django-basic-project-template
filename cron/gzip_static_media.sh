#!/bin/bash

set -u -e

PROJ_DIR="`dirname $0`/.."
PROJECT=`grep -E -o '(\w+)\.settings' $PROJ_DIR/manage.py | awk -F . '{print $1}'`
STATIC_DIR=$PROJ_DIR/$PROJECT/media/static

for F in `find $STATIC_DIR -type f -size +1k -regextype posix-extended -regex ".*\.[a-f0-9]{12}\.(css|js|json|ttf|otf|eot|svg|txt|htm|html|xml)"`
do
	if [[ $F.gz -ot $F ]]; then
		gzip -c -3 $F > $F.gz
	fi
done
