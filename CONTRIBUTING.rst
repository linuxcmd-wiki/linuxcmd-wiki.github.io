如何贡献
========

本项目使用 sphinx 构建。

所有文档使用 rst 文件格式编写，最后通过 sphinx 工具构建成 html 文档。


项目结构
--------

``src``
    rst 格式源文件目录

``_site``
    构建后的 html 文件目录


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
