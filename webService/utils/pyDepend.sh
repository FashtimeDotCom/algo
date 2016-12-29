#! /bin/sh

yum -y install vim gcc gcc-c++ gcc-gfortran wget
yum -y install lrzsz dos2unix unix2dos bzip2* bzip2-devel
yum -y install flex byacc libpcap ncurses ncurses-devel 
yum -y install readline-devel
yum -y install MySQL-python mysql-devel
yum -y install lapack lapack-devel blas blas-devel
yum -y install openssl openssl-devel
yum -y install libxml2 libxml2-devel libxslt libxslt-devel libffi-devel libjpeg-turbo-devel libpcap-devel libpng-devel freetype-devel
yum -y install python27-devel  python-devel python-setuptools  python-tools python-matplotlib python-pandas

echo "=== finish ==="

