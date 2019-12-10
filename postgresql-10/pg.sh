#!/bin/bash

mv pgdg-10-centos.repo /etc/yum.repos.d
yum install pgdg-centos10-10-2.noarch.rpm >/dev/null 2>&1
yum install postgresql10-server.x86_64 >/dev/null 2>&1
sed  /var/lib   /etc/rc.d/init.d/postgresql-10
sed -i 's/var\/lib/home\/bymiao\/lib/' /etc/rc.d/init.d/postgresql-10
service postgresql-10 initdb >/dev/null 2>&1
service postgresql-10 start >/dev/null 2>&1
yum install postgresql10-plpython.x86_64 >/dev/null 2>&1
mv -f pg_hba.conf /home/bymiao/lib/pgsql/10/data
mv -f postgresql.conf /home/bymiao/lib/pgsql/10/data


#-----------------------------------------------------------------------------------------------#

sed -i "/home/bymiao/trade/bin" /etc/ld.so.conf
ldconfig -v

#-----------------------------------------------------------------------------------------------#
# 在安装glibc-2.14.tar glibc-ports-2.14.tar
SOFT_PATH=$(pwd)
cd $SOFT_PATH

# 01-----安装 glibc-2.14
tar -xf  glibc-ports-2.14.tar.gz
tar xf glibc-2.14.tar.gz
mv glibc-ports-2.14 glibc-2.14/ports
mkdir glibc-2.14/build && cd glibc-2.14/build >/dev/null 2>&1
../configure  --prefix=/usr --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin >>$SOFT_PATH/sh.log 2>&1
make &&  make install >>$SOFT_PATH/sh.log 2>&1

echo -e "\e[1;32m glibc have been installed to complete...\e[0m"