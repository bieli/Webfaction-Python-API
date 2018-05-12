Webfaction-Python-API 
---------------------

[![Build Status](https://travis-ci.org/bieli/Webfaction-Python-API.svg?branch=master)](http://travis-ci.org/bieli/Webfaction-Python-API)

[![codecov](https://codecov.io/gh/bieli/Webfaction-Python-API/branch/master/graph/badge.svg)](https://codecov.io/gh/bieli/Webfaction-Python-API)


Webfaction API client with command line tool for calling API methods.
Python 2 and 3 API is supported.


How to run
----------
1) checkout source
```bash
git clone https://github.com/bieli/Webfaction-Python-API.git
```

2) create configuration file ~/.webfrc with your Webfaction's username and password
```bash
cat << 'EOF' > ~/.webfrc1
username="username"
password="strong_password"

EOF

```

2) use command line with webfaction in place (without installing in OS)
```bash
cd Webfaction-Python-API
cp bin/webfaction ./webfaction-cli
chmod +x ./webfaction-cli
./webfaction-cli --system="uname -a"
Linux web616.webfaction.com 3.10.0-693.17.1.el7.x86_64 #1 SMP Thu Jan 25 20:13:58 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

```

3) enjoy with Webfaction API commands
```bash
./webfaction-cli --help
Usage: webfaction-cli [options]

Options:
  -h, --help            show this help message and exit
  --version             Show this program's version and exit.
  --debug               Show debugging information

  WebFaction Commands:
    Options for calling WebFaction XML-RPC API methods

    --create-app=NAME TYPE AUTOSTART EXTRA_INFO
                        Create application
    --delete-app=NAME   Delete application
    --create-cronjob=CRONJOB
                        Create cronjob
    --delete-cronjob=CRONJOB
                        Delete cronjob
    --create-db=NAME DB_TYPE PASSWORD
                        Create Database
    --delete-db=NAME DB_TYPE
                        Delete Database
    --create-domain=DOMAIN SUBDOMAIN
                        Create domain
    --create-website=NAME IP HTTPS SUBDOMAINS *SITE_APPS
                        Create website
    --create-dns-override=DOMAIN A_IP CNAME MX_NAME MX_PRIORITY SPF_RECORD
                        Create DNS override
    --delete-dns-override=DOMAIN A_IP CNAME MX_NAME MX_PRIORITY SPF_RECORD
                        Delete DNS override
    --create-email=EMAIL_ADDRESS TARGETS AR_ON AR_SUBJECT AR_MSG AR_FROM
                        Create email address
    --delete-email=EMAIL_ADDRESS
                        Delete email address
    --create-mailbox=MBOX_NAME SPAM_PROT SHARE SPAM_LEARN HAM_LEARN
                        Create mailbox
    --delete-mailbox=MBOX_NAME
                        Delete mailbox
    --list-disk-usage=LIST_DISK_USAGE
                        List disk usage
    --list-bandwidth-usage=LIST_BANDWIDTH_USAGE
                        List bandwidth usage
    --list-machines=LIST_MACHINES
                        List machines
    --set-apache-acl=PATHS PERMS RECURSIVE
                        Set Apache ACL
    --system=CMD        Run system command.
    --write-file=FILENAME STRING MODE
                        Write file

```



TODO
-----
- (X) support for Pytohn 3
- (X) implement support for list usage disks and bandwidth
- (X) adding Travis CI build in multiple Python versions
- (X) some unit tests
- (_) verify compatibility for Python 2 and Python 3



Original README description (from forked repository)
--------------
This is a port of https://pypi.python.org/pypi/webf/ -- the repo exists because

A. There doesn't seem to be a good source listing anymore (original site is dead)
B. I wanted to modify it to accept passed-in credentials instead of having one config file

Original post: http://forum.webfaction.com/viewtopic.php?id=1513 [dead]
WebFaction API Docs: https://docs.webfaction.com/xmlrpc-api/
