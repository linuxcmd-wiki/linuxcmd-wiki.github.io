.. index:: dig

.. meta::
    :description: Linux dig 命令使用详解。dig 命令可以从指定的目录中列出匹配
        的文件。


dig
===

dig 是域名查询工具，属于 ISC `BIND`_ 项目中的一员。

.. _BIND: https://www.isc.org/bind/

语法
^^^^

dig 基本语法如下：

.. code-block:: none

    dig name [@server] [type]

name
    要解析的域名，例如 www.example.com 。

server
    解析域名的服务器，例如 114.114.114.114 (114 DNS), 8.8.8.8 (Google DNS),
    1.1.1.1 (Cloudflare DNS) 等。

    server 是可选参数，如果不指定的话，默认会读取系统本地的
    ``/etc/resolv.conf`` 文件中设定的 nameserver 的值，将域名解析请求发送给它。

type
    域名解析请求的类型，例如 A, TXT, MX 等。

    type 是可选参数，如果不指定的话，默认解析请求 A 类型的记录。

案例
^^^^
