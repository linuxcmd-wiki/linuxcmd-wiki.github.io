.. index:: dig

.. meta::
    :description: Linux dig 命令使用详解。dig 命令可以从指定的目录中列出匹配
        的文件。


dig
===

dig 是域名查询工具，属于 ISC `BIND`_ 项目中的一员。

.. _BIND: https://www.isc.org/bind/

语法
----

dig 基本语法如下：

.. code-block:: none

    dig name [@server] [type]

name
    要查询的域名，例如 www.example.com 。

server
    解析域名的服务器（nameserver），例如 114.114.114.114（114 DNS），8.8.8.8
    （Google DNS），1.1.1.1 （Cloudflare DNS）等。

    server 是可选参数，如果不指定的话，默认会读取系统本地的
    ``/etc/resolv.conf`` 文件中设定的 nameserver 的值，将域名解析请求发送给它。

type
    域名查询请求的类型，例如 A, TXT, MX 等。

    type 是可选参数，如果不指定的话，默认查询的是 A 类型的记录。

返回内容解读
------------

.. code-block:: bash

    $ dig linuxcmd.wiki

    ; <<>> DiG 9.11.4 <<>> linuxcmd.wiki
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 23305
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0

    ;; QUESTION SECTION:
    ;linuxcmd.wiki.                 IN      A

    ;; ANSWER SECTION:
    linuxcmd.wiki.          300     IN      A       104.21.42.57
    linuxcmd.wiki.          300     IN      A       172.67.201.88

    ;; Query time: 302 msec
    ;; SERVER: 183.60.83.19#53(183.60.83.19)
    ;; WHEN: Fri Jun 04 17:17:29 CST 2021
    ;; MSG SIZE  rcvd: 63
    
上面是一个完整的 dig 命令返回结果的内容，下面我通过注释的方式来解读它们都表示什
么含义：

.. code-block:: bash

    $ dig linuxcmd.wiki

    dig 的版本
    ; <<>> DiG 9.11.4 <<>> linuxcmd.wiki
    dig 命令中的全局参数设定
    ;; global options: +cmd
    ;; Got answer:
    域名查询的请求头
    opcode 表示请求的类型，这里的 QUERY 是指标准查询请求，其它的类型有 IQUERY (反向查询请求），STATUS（服务器状态查询请求）
    status 表示返回的状态，0 (NO ERROR) 表示没有问题，其它的返回状态还有 1 (FORMAT ERROR)，2 (SERVER FAILURE)，3 (NAME ERROR)，4 (NOT IMPLEMENTED)，5 (REFUSED)
    id 是一个 16 bit 长度的识别号，由 dig 发送请求的时候随机产生，在收到返回结果的时候会校验是否一致
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 23305
    返回结果有 1 个 QUESTION SECTION，两个 ANSWER SECTION，没有 AUTHORITY SECTION 和 ADDITIONAL SECTION
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0

    请求部分
    ;; QUESTION SECTION:
    查询的域名是 linuxcmd.wiki，CLASS 是 IN (Internet)，TYPE 是 A
    ;linuxcmd.wiki.                 IN      A

    返回部分，有两条记录
    ;; ANSWER SECTION:
    第一条记录，TTL 是 300，CLASS 是 IN (Internet)，TYPE 是 A，结果是 104.21.42.57
    linuxcmd.wiki.          300     IN      A       104.21.42.57
    第二条记录，TTL 是 300，CLASS 是 IN (Internet)，TYPE 是 A，结果是 172.67.201.88
    linuxcmd.wiki.          300     IN      A       172.67.201.88

    ;; Query time: 302 msec
    ;; SERVER: 183.60.83.19#53(183.60.83.19)
    ;; WHEN: Fri Jun 04 17:17:29 CST 2021
    ;; MSG SIZE  rcvd: 63


通过指定的 nameserver 解析域名
------------------------------

通过加上 ``@server`` 参数指定 nameserver，否则默认将解析请求发送给系统本地
``/etc/resolv.conf`` 文件中设定的 nameserver。

下面的命令将解析 ``linuxcmd.wiki`` 的请求发送给 ``8.8.8.8`` 这个 nameserver 来处
理：

.. code-block:: bash

    $ dig linuxcmd.wiki @8.8.8.8
