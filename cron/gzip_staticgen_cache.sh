#!/bin/bash

set -u -e

PROJ_DIR="`dirname $0`/.."
PROJECT=`grep -E -o '(\w+)\.settings' $PROJ_DIR/manage.py | awk -F . '{print $1}'`
CACHE_DIR=$PROJ_DIR/$PROJECT/media/cache/fresh

for F in `find $CACHE_DIR -type f -name "*.html%3F*" -mtime +23`
do
	rm $F
done

for F in `find $CACHE_DIR -type f -size +1k -name "*.html%3F*" -not -name "*.gz"`
do
	if [[ $F.gz -ot $F ]]; then
		gzip -c -3 $F > $F.gz
	fi
done
