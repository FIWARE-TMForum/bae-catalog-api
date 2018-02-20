#!/bin/bash

# USAGE: test_all URL

# flush db to keep integrity in tests
echo 'Flushing database...'
python3 ../django/catalogapi/manage.py flush --no-input

echo 'Database flushed!'
# set default URL, localhost by default
URL=$1/catalogManagement

if [ -n $1 ]; then
    URL=http://127.0.0.1:8000/catalogManagement
fi

# remove backup files (hi emacs users! :D)
find . -name '*~' | xargs rm -f
echo '----------------------- CATEGORY TESTS -----------------------'
echo 'Category POST success:'
for i in $(ls category/post/success/); do
    echo $i
    cat $PWD/category/post/success/$i
    http POST $URL/category/ < $PWD/category/post/success/$i
done

echo 'Category POST failure:'
for i in $(ls category/post/failure/); do
    echo $i
    cat $PWD/category/post/failure/$i
    http POST $URL/category/ < $PWD/category/post/failure/$i
done

echo 'Category GET:'
http GET $URL/category/

echo '----------------------- CATALOG TESTS -----------------------'
echo 'Catalog POST success:'
for i in $(ls catalog/post/success/); do
    echo $i
    cat $PWD/catalog/post/success/$i
    http POST $URL/catalog/ < $PWD/catalog/post/success/$i
done
echo 'Catalog POST failure'
for i in $(ls catalog/post/failure/); do
    echo $i
    cat $PWD/catalog/post/failure/$i
    http POST $URL/catalog/ < $PWD/catalog/post/failure/$i
done

echo 'Catalog GET:'
http GET $URL/catalog/
