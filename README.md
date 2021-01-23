<h1 align="center">Easy Charts</h1>
<p align="center">
    <em>PyQt5 ❤️ pyecharts = EasyCharts</em>
</p>
<p align="center">

## 📣 简介

[Apache ECharts (incubating)](https://github.com/apache/incubator-echarts) 是一个由百度开源的数据可视化，凭借着良好的交互性，精巧的图表设计，得到了众多开发者的认可。而 Python 是一门富有表达力的语言，很适合用于数据处理。当数据分析遇上数据可视化时，[pyecharts](https://github.com/pyecharts/pyecharts) 诞生了。

但pyecharts在使用时还是有一定的门槛，要求使用者必须会用python，还需要懂一些HTML的基本知识，对于很多初级的数据分析师，或者只是偶尔做些报表的同学并不是很友好。

作为一个数据分析师出身的产品经理，一直都想做出一款简单易用的数据可视化工具，让数据分析回归分析的本质，而不用把时间浪费在数据处理和数据可视化报表的配置上。

于是便有了这个工具：[Easy Charts](https://github.com/soaringsoul/easycharts) ，让你更快、更简单地实现数据可视化。

## ✨ 特性

* 一键导入Excel文件，选择指定的列名，即可生成图表。
* 目前仅支持饼图，圆环图，南丁格尔图，更多图表正在开发中，喜欢的同学可以先关注一下。
* 支持主要的Echarts图表配置，如显示或者隐藏图例，设置标签显示样式，自定义标题、颜色等。
* 生成的图表可以直接右键复制图表，支持粘贴到word,excel，ppt中。
* 因为后续会持续添加更多图表，所以程序中添加了更新检测机制，如果有新的版本，在打开程序后会收到更新提醒。



## ⏳ 快速开始

![easychart_quick_start](D:\OneDrive\myGitHubProjects\easycharts\ui\screenshot\easychart_quick_start.gif)



## 🔰 安装

**pip 安装**

```shell
# 安装 v1 以上版本
$ pip install pyecharts -U

# 如果需要安装 0.5.11 版本的开发者，可以使用
# pip install pyecharts==0.5.11
```

**源码安装**
```shell
# 安装 v1 以上版本
$ git clone https://github.com/pyecharts/pyecharts.git
# 如果需要安装 0.5.11 版本，请使用 git clone https://github.com/pyecharts/pyecharts.git -b v05x
$ cd pyecharts
$ pip install -r requirements.txt
$ python setup.py install
```

## 📝 使用

### 本地环境

#### 生成 HTML
```python
from pyecharts.charts import Bar
from pyecharts import options as opts

# V1 版本开始支持链式调用
bar = (
    Bar()
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
)
bar.render()

# 不习惯链式调用的开发者依旧可以单独调用方法
bar = Bar()
bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
bar.render()
```
<p align="center">
<img src="https://user-images.githubusercontent.com/19553554/55270272-d6ff1b80-52d7-11e9-820f-30660a068e3e.gif"  width="85%" />
</p>

#### 生成图片
```python
from snapshot_selenium import snapshot as driver

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot


def bar_chart() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c

# 需要安装 snapshot-selenium 或者 snapshot-phantomjs
make_snapshot(driver, bar_chart().render(), "bar.png")
```
<p align="center">
<img src="https://user-images.githubusercontent.com/19553554/56089096-11fc7400-5ec0-11e9-9c21-551624036836.png"  width="85%" />
</p>

### Notebook 环境

#### Jupyter Notebook

![](https://user-images.githubusercontent.com/19553554/55270255-b3d46c00-52d7-11e9-8aa5-f7b3819a1e88.png)

#### JupyterLab

![](https://user-images.githubusercontent.com/19553554/55270259-c0f15b00-52d7-11e9-8811-93bfca1cc027.png)

#### Web 框架

![](https://user-images.githubusercontent.com/19553554/35081158-3faa7c34-fc4d-11e7-80c9-2de79371374f.gif)

## 🔖 Demo

> Demo 代码位于 example 文件夹下，欢迎参考 pyecharts 画廊 [pyecharts-gallery](https://github.com/pyecharts/pyecharts-gallery)。

<div align="center">
<img src="https://user-images.githubusercontent.com/19553554/52197440-843a5200-289a-11e9-8601-3ce8d945b04a.gif" width="33%" alt="bar"/>
<img src="https://user-images.githubusercontent.com/19553554/52360729-ad640980-2a77-11e9-84e2-feff7e11aea5.gif" width="33%" alt="boxplot"/>
<img src="https://user-images.githubusercontent.com/19553554/52535290-4b611800-2d87-11e9-8bf2-b43a54a3bda8.png" width="33%" alt="effectScatter"/>
<img src="https://user-images.githubusercontent.com/19553554/52332816-ac5eb800-2a36-11e9-8227-3538976f447d.gif" width="33%" alt="funnel"/>
<img src="https://user-images.githubusercontent.com/19553554/52332988-0b243180-2a37-11e9-9db8-eb6b8c86a0de.png" width="33%" alt="gague"/>
<img src="https://user-images.githubusercontent.com/19553554/52344575-133f9980-2a56-11e9-93e0-568e484936ce.gif" width="33%" alt="geo"/>
<img src="https://user-images.githubusercontent.com/19553554/35082102-fd8d884a-fc52-11e7-9e40-5f94098d4493.gif" width="33%" alt="geo"/>
<img src="https://user-images.githubusercontent.com/19553554/52727805-f7f20280-2ff0-11e9-91ab-cd99848e3127.gif" width="33%" alt="graph"/>
<img src="https://user-images.githubusercontent.com/19553554/52345115-6534ef00-2a57-11e9-80cd-9cbfed252139.gif" width="33%" alt="heatmap"/>
<img src="https://user-images.githubusercontent.com/19553554/52345490-4a16af00-2a58-11e9-9b43-7bbc86aa05b6.gif" width="33%" alt="kline"/>
<img src="https://user-images.githubusercontent.com/19553554/52346064-b7770f80-2a59-11e9-9e03-6dae3a8c637d.gif" width="33%" alt="line"/>
<img src="https://user-images.githubusercontent.com/19553554/52347117-248ba480-2a5c-11e9-8402-5a94054dca50.gif" width="33%" alt="liquid"/>
<img src="https://user-images.githubusercontent.com/19553554/52347915-0a52c600-2a5e-11e9-8039-41268238576c.gif" width="33%" alt="map"/>
<img src="https://user-images.githubusercontent.com/19553554/57545910-431c7700-738e-11e9-896b-e071b55115c7.png" width="33%" alt="bmap"/>
<img src="https://user-images.githubusercontent.com/19553554/52535013-e48e2f80-2d83-11e9-8886-ac0d2122d6af.png" width="33%" alt="parallel"/>
<img src="https://user-images.githubusercontent.com/19553554/52348202-bb596080-2a5e-11e9-84a7-60732be0743a.gif" width="33%" alt="pie"/>
<img src="https://user-images.githubusercontent.com/19553554/35090457-afc0658e-fc74-11e7-9c58-24c780436287.gif" width="33%" alt="ploar"/>
<img src="https://user-images.githubusercontent.com/19553554/52533994-932b7380-2d76-11e9-93b4-0de3132eb941.gif" width="33%" alt="radar"/>
<img src="https://user-images.githubusercontent.com/19553554/52348431-420e3d80-2a5f-11e9-8cab-7b415592dc77.gif" width="33%" alt="scatter"/>
<img src="https://user-images.githubusercontent.com/19553554/44004598-5636d74e-9e97-11e8-8a5c-92de6278880d.gif" width="33%" alt="tree"/>
<img src="https://user-images.githubusercontent.com/19553554/35082251-b9e23982-fc53-11e7-8341-e7da1842389f.gif" width="33%" alt="treemap"/>
<img src="https://user-images.githubusercontent.com/19553554/52348737-01fb8a80-2a60-11e9-94ac-dacbd7b58811.png" width="33%" alt="wordCloud"/>
<img src="https://user-images.githubusercontent.com/19553554/52433989-4f075b80-2b49-11e9-9979-ef32c2d17c96.gif" width="33%" alt="bar3D"/>
<img src="https://user-images.githubusercontent.com/19553554/52464826-4baab900-2bb7-11e9-8299-776f5ee43670.gif" width="33%" alt="line3D"/>
<img src="https://user-images.githubusercontent.com/19553554/52802261-8d0cfe00-30ba-11e9-8ae7-ae0773770a59.gif" width="33%" alt="sankey"/>
<img src="https://user-images.githubusercontent.com/19553554/52464647-aee81b80-2bb6-11e9-864e-c544392e523a.gif" width="33%" alt="scatter3D"/>
<img src="https://user-images.githubusercontent.com/19553554/52465183-a55fb300-2bb8-11e9-8c10-4519c4e3f758.gif" width="33%" alt="surface3D"/>
<img src="https://user-images.githubusercontent.com/19553554/52798246-7ebae400-30b2-11e9-8489-6c10339c3429.gif" width="33%" alt="themeRiver"/>
<img src="https://user-images.githubusercontent.com/17564655/57567164-bdd5a880-7407-11e9-8d19-9be2776c57fa.png" width="33%" alt="sunburst"/>
<img src="https://user-images.githubusercontent.com/19553554/52349544-c2ce3900-2a61-11e9-82af-28aaaaae0d67.gif" width="33%" alt="overlap"/>
<img src="https://user-images.githubusercontent.com/19553554/35089737-ccc1c01c-fc72-11e7-874d-8ba8b89572eb.png" width="33%" alt="grid"/>
<img src="https://user-images.githubusercontent.com/19553554/56976071-b9f28c80-6ba4-11e9-8efd-603203c77619.png" width="33%" alt="grid">
<img src="https://user-images.githubusercontent.com/19553554/35082279-e111743c-fc53-11e7-9362-580160593715.gif" width="33%" alt="timeline"/>
</div>

更多详细文档，请访问

* [中文文档](http://pyecharts.org/#/zh-cn/)
* [English Documentation](http://pyecharts.org/#/en-us/)
* [示例 Example](https://gallery.pyecharts.org)

## ⛏ 代码质量

### 单元测试

```shell
$ pip install -r test/requirements.txt
$ make
```

### 集成测试

使用 [Travis CI](https://travis-ci.org/) 和 [AppVeyor](https://ci.appveyor.com/) 持续集成环境。

### 代码规范

使用 [flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/) 以及 [pylint](https://www.pylint.org/) 提升代码质量。

## 😉 Author

pyecharts 主要由以下几位开发者开发维护

* [@chenjiandongx](https://github.com/chenjiandongx)
* [@chfw](https://github.com/chfw)
* [@kinegratii](https://github.com/kinegratii)
* [@sunhailin-Leo](https://github.com/sunhailin-Leo)

更多贡献者信息可以访问 [pyecharts/graphs/contributors](https://github.com/pyecharts/pyecharts/graphs/contributors)

## 💌 捐赠

开发和维护 pyecharts 花费了我巨大的心力，如果你觉得项目帮助到您，请认真考虑请作者喝一杯咖啡 😄

| 微信二维码 | 支付宝二维码 |
| -------- | ---------- |
| <img src="https://assets.pyecharts.org/images/wechat-code.png" width=220px alt="wechat-code"> | <img src="https://assets.pyecharts.org/images/alipay-code.png" width=220px alt="alipay-code"> |

如果其他开发者帮助到了您，也可以请他们喝咖啡 [捐赠通道](http://pyecharts.org/#/zh-cn/donate)

## 💡 贡献

期待能有更多的开发者参与到 pyecharts 的开发中来，我们会保证尽快 Reivew PR 并且及时回复。但提交 PR 请确保

1. 通过所有单元测试，如若是新功能，请为其新增单元测试
2. 遵守开发规范，使用 black 以及 isort 格式化代码（$ pip install -r requirements-dev.txt）
3. 如若需要，请更新相对应的文档

我们也非常欢迎开发者能为 pyecharts 提供更多的示例，共同来完善文档，文档项目位于 [pyecharts/website](https://github.com/pyecharts/website)

## 📃 License

MIT [©chenjiandongx](https://github.com/chenjiandongx)
