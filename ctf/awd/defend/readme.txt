gcc monitor2.c md5.c -o filemonitor
./filemonitor /var/www/html /tmp ���Ը����Ŀ¼


./filemonitor /tmp `find /var/www/html -type d -print | xargs echo` 
����Ŀ¼  ��ǰĿ¼�µ�bak  
./bak/var/www/html
./bak/tmp

---------------------------------------------------------------------------------------------------------
dir='/var/www/html'
rm -rf bak && mkdir bak  && mkdir -p ./bak$dir && cp -a $dir/* ./bak$dir &&  mkdir newfile
gcc monitor2.c md5.c -o filemonitor &&./filemonitor `find $dir -type d -print | xargs echo`


----------summary-----------------------------
# add waf
find /var/www/html -type f -name "*.php" |xargs sed -i "1 i<?php include_once('/var/www/html/waf2.php');?>"


#FileMoniter
#copy file to /var/tmp

dir='/var/www/test123'
cd /var/tmp/
rm -rf bak && mkdir bak  && mkdir -p ./bak$dir && cp -a $dir/* ./bak$dir &&  mkdir newfile
./filemonitor `find $dir -type d -print | xargs echo`


#gcc monitorv4.c md5.c -o filemonitor &&./filemonitor `find $dir -type d -print | xargs echo`