.. index:: find

.. meta::
    :description: Linux find 命令使用详解。find 命令可以从指定的目录中列出匹配
        的文件。


find
====

find 命令可以从指定的目录中列出匹配的文件。

使用方式
--------

find 命令的基本语法如下：

.. code-block:: none

    find [PATH...] [EXPRESSION]

其中 ``PATH`` 可以一次有多个； ``EXPRESSION`` （表达式）有这么几种类型：

``Global options``
    全局选项表达式，例如 ``-depth``, ``-maxdepth``, ``-mindepth`` 等。

    **注意** ：全局参数建议放在所有其它参数的前面，因为它影响的是整个表达式。否
    则会出现警告提示：

    .. code-block:: bash

        $ find / -type d -maxdepth 2 
        find: warning: you have specified the global option -maxdepth after the argument -type, but global options are not positional, i.e., -maxdepth affects tests specified before it as well as those specified after it.  Please specify global options before other arguments.

    上面的 find 命令正确的写法应该是把全局参数 ``-maxdepth 2`` 需要放在
    ``--type d`` 之前。

``Operators``
    运算符表达式，例如 ``-a`` , ``-o``, ``-not`` 等逻辑运算相关参数。

    通常我们使用 find 的时候会连续使用多个表达式，用空格分隔，其实这种情况表达
    式之间暗含了 ``-a`` 参数（代表 and 运算），例如：
    
    .. code-block:: bash

        $ find / -type f -perm 755
        
    上面例子中的 ``-type f`` 与 ``-perm 755`` 之间有个隐藏的 ``-a`` 参数，所以
    它也等效于下面的形式：

    .. code-block:: bash

        $ find / -type f -a -perm 755

``Tests``
    条件表达式，例如 ``-type``, ``-name``, ``-perm`` 等。

``Actions``
    操作表达式，例如 ``-delete``, ``-printf``, ``-exec`` 等。

``Positional options``
    位置选项表达式，这个不太常用，所以这里就不探究了，有兴趣可以参看 ``man
    find`` 。

实践案例
--------

下面通过一些具体的案例来看下 find 的实际使用。

通过匹配文件名来查找文件
^^^^^^^^^^^^^^^^^^^^^^^^

这是 find 最常用的方式之一， 该方式通过 ``-name`` 参数（属于上述 ``Tests`` 类型
表达式）来匹配文件名：

.. code-block:: bash

    $ find . -type f -name '*.txt'

上面的命令是查询当前目录下所有 .txt 后缀的文件。其中 ``.`` 表示当前目录，也可以
是其他任意指定的目录，例如 ``/``, ``/home`` 等。

上面的命令中的 ``*.txt`` 是用来匹配所有 .txt 后缀文件的表达式。``-name`` 参数中
的 ``?``, ``*``, ``[]`` 有特殊的含义：

- ``?``: 匹配单个任意字符。

- ``*``: 匹配任意个字符。

- ``[]``: 匹配括号中包含的任意一个字符。

什么意思呢？例如有三个文件 ``.txt``, ``a.txt``, ``abc.txt``, 使用 ``*.txt`` 可
以把这三个都匹配上，而使用 ``?.txt`` 和 ``[abc].txt`` 都只能匹配上 ``a.txt`` 。

另外需要注意的是， ``*.txt`` 务必要用单引号包起来（ ``'*.txt'`` ）才能作为
``-name`` 参数的值使用。因为 ``*`` 在 bash 中也被作为特殊字符对待，所以加上单引
号可以避免 bash 截胡。
