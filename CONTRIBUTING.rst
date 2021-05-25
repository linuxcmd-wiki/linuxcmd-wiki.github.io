如何贡献
========

本项目使用 sphinx 构建。

所有文档使用 rst 文件格式编写，最后通过 sphinx 工具构建成 html 文档。


项目结构
--------

``source/``
    存放 rst 格式源文件的目录，所有的文档都在这里面编辑。

``build/``
    用于 sphinx 构建目标文件的目录，可以是 html、xml 等。此项目只需构建成 html
    文件即可。

``build/html``
    是一个软链接，对应下面的 ``doc`` 目录。sphinx 构建最终生成的所有 html 文件
    都保存在这里。

``doc/``
    sphinx 构建最终生成的所有 html 文件都保存在这里；也是 Git Page 的根目录。


安装 sphinx 构建工具
--------------------

.. code-block:: console

    $ pip install -r requirements.txt

或者：

.. code-block:: console

    $ pip install sphinx cloud_sptheme


编辑 rst 文档
-------------

使用任意你喜欢的编辑器，新建或者修改 ``src`` 目录下的 rst 文档。


构建 html 文档
--------------

在项目根目录使用如下命令将 rst 文档构建成 html 文档：

.. code-block:: console

    $ make html


查看 html 页面
--------------

切换到 doc 目录下，使用如下命令启动一个简单的 http server：

.. code-block:: console

    $ python -m http.server

然后访问本地的 http://127.0.0.1:8000 进行查看。
