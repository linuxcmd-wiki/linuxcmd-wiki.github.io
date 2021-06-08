.. index:: find

.. meta::
    :description: Linux find 命令使用详解。find 命令可以从指定的目录中列出匹配
        的文件。


find
====

find 命令是 GNU `Findutils`_ 项目中的一员，其可以从指定的目录中列出匹配的文件。

.. _Findutils: https://www.gnu.org/software/findutils/

语法
----

find 命令的基本语法如下：

.. code-block:: none

    find [PATH...] [EXPRESSION]

PATH
    即在哪个或者哪些文件夹下搜索文件。

    下面的命令会列出 ``/usr/lib`` 和 ``/usr/lib64`` 这两个文件夹中所有的文件：

    .. code-block:: bash

        $ find /usr/lib /usr/lib64

EXPRESSION（表达式）
    即匹配文件的规则，有这么几种类型：

    ``Global options``
        全局选项表达式，例如 ``-depth``, ``-maxdepth``, ``-mindepth`` 等参数构成的
        表达式。

        .. Warning::
            全局参数建议放在所有其它参数的前面，因为它影响的是整个表达式。否则
            会出现警告提示：

            .. code-block:: bash

                $ find / -type d -maxdepth 2 
                find: warning: you have specified the global option -maxdepth after the argument -type, but global options are not positional, i.e., -maxdepth affects tests specified before it as well as those specified after it.  Please specify global options before other arguments.

            上面的命令正确的写法应该是把全局参数 ``-maxdepth 2`` 放在 ``--type
            d`` 之前。

    ``Operators``
        运算符表达式，例如 ``-a`` , ``-o``, ``-not`` 等逻辑运算相关参数构成的表
        达式。

        通常我们使用 find 的时候会连续使用多个表达式，用空格分隔，其实这种情况
        表达式之间暗含了 ``-a`` 参数（代表 and 运算），例如：
        
        .. code-block:: bash

            $ find / -type f -perm 755
            
        上面例子中的 ``-type f`` 与 ``-perm 755`` 之间有个隐藏的 ``-a`` 参数，
        所以它也等效于下面的形式：

        .. code-block:: bash

            $ find / -type f -a -perm 755

    ``Tests``
        条件表达式，例如 ``-type``, ``-name``, ``-perm`` 等参数构成的表达式。

    ``Actions``
        操作表达式，例如 ``-delete``, ``-printf``, ``-exec`` 等参数构成的表达式
        。

    ``Positional options``
        位置选项表达式，这个不太常用，所以这里就不探究了，有兴趣可以参看 ``man
        find`` 。

通过匹配文件名来查找文件
------------------------

查询某个目录下所有 .txt 后缀的文件：

.. code-block:: bash

    $ find /path/to/dir -type f -name '*.txt'

``-type f``
    表示匹配文本类型文件。其它常用的还有 d（表示文件夹），l（表示软链接）。

``-name '*.txt'``
    表示匹配以 .txt 为后缀的文件。 

    .. Note::
        :class: block-title

        ``-name`` 参数中的 ``?``, ``*``, ``[]`` 有特殊的含义：

        - ``?``: 匹配单个任意字符。
        - ``*``: 匹配任意个字符。
        - ``[]``: 匹配括号中包含的任意一个字符。

        什么意思呢？例如有三个文件 ``.txt``, ``a.txt``, ``abc.txt``, 使用
        ``*.txt`` 可以把这三个都匹配上，而使用 ``?.txt`` 和 ``[abc].txt`` 都只
        能匹配上 ``a.txt`` 。

    .. Caution::
        :class: block-title

        ``*.txt`` 务必要用单引号包起来（ ``'*.txt'`` ）才能作为 ``-name`` 参数
        的值被正确使用。因为 ``*`` 在 bash 中被作为特殊字符对待，所以加上单引号
        转义避免 bash 截胡。

通过匹配文件大小来查找文件
--------------------------

在 stackexchange 上看到有人 `提问`_ ，想要删除某个目录下所有空文件：

.. _提问: https://unix.stackexchange.com/q/31771

.. code-block:: bash

    $ find /path/to/dir -type f -empty -delete

``-empty``
    表示匹配大小为 0 的文件。

``-delete``
    表示删除匹配的文件。

    .. Caution::
        :class: block-title

        老版本的 find 不支持 ``-delete`` 参数，则可以使用 ``-exec rm {} +`` 来
        替代。

``-empty`` 只能用来匹配空文件，find 有一个更加灵活的参数用来匹配文件大小的范围
—— ``-size`` ：

- ``-size 4k`` ：匹配大小为 4KiB 的文件。
- ``-size +5M`` ：匹配大于 5Mib 的文件。
- ``-size -6G`` ：匹配小于 6GiB 的文件。

通过匹配文件日期来查找文件
--------------------------

我在 stackexchange 有一个 `回答`_ ，将过去 10 分钟内没有被修改过的文件移动到另
一个文件夹中：

.. _回答: https://unix.stackexchange.com/a/652653/474814

.. code-block:: bash

    $ find /path/to/dir1 -type f ! -mmin -10 -exec mv {} /path/to/dir2 \;

``-mmin -10``
    表示过去 10 分钟内，内容被修改过的文件。

``!``
    表示逻辑非，扭转上面的含义变成过去 10 分钟内，内容没有被修改过的文件。

``-exec mv {} /path/to/dir2 \;``
    表示将匹配的文件移动到 dir2 文件夹中。

    .. Note::
        :class: block-title

        ``-exec`` 后面跟上其它任意命令，其将匹配到的文件替换到 ``{}`` 的位置交
        由其它命令继续操作。 其后面的命令有两种形式：

        1. ``-exec command ;`` ： 迭代匹配到的文件，将其替换到 ``{}`` 的位置，
           逐个执行命令。``{}`` 可以置于命令中的任意位置。
        2. ``-exec command  {} +`` ： 将匹配到的所有文件都一次性替换到 ``{}`` 
           位置。``{}`` 只能置于命令中的最后位置。

    .. Caution::
        :class: block-title

        注意到 ``;`` 前面有个斜杠（``\;``），因为 ``;`` 在 bash 中被作为特殊字
        符对待，所以加上斜杠转义避免 bash 截胡。

