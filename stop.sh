ps aux |grep "[p]ython ./manage.py runfcgi" |grep -E "^([a-z0-9]{1,}[^0-9]+)([0-9]+)" -o |grep -E "[0-9]+$" -o |head -n 1 > kill.pid
kill -KILL `cat kill.pid`
echo>kill.pid 
ps aux | grep "[p]ython ./manage.py runfcgi"
