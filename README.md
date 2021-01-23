

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



## 🔰 windows下安装

下载windows安装文件，解压并安装：

> 链接：https://pan.baidu.com/s/1LVSstsp0Y_7PE95yfcpgvg 
> 提取码：1234 

![setup](/ui/screenshot/setup.png)

安装完成后桌面开始菜单里都会生成名为`Easy Charts`的快捷方式，点击即可打开。![image-20210123211418426](/C:/Users/soaringsoul/AppData/Roaming/Typora/typora-user-images/image-20210123211418426.png)



## 📝 使用

导入Excel文件，导入完成后选择需要可视化的列名，然后在图表配置项里按需要选择即可:

### 简单使用

#### 选择标签样式

* 仅显示数据项名称
* 仅显示数据项统计值
* 仅显示数据项统计的百分比
* 显示数据项的名称和数据值
* **显示数据项的名称和百分比（默认项）**

![label_style_select](/ui/screenshot/label_style_select.gif)

#### 切换环形图和南丁格尔图（又叫玫瑰图）

![switch_donut](/ui/screenshot/switch_donut.gif)

#### 自定义标题

![custom_title](/ui/screenshot/custom_title.gif)

#### 自定义颜色

自定义颜色可以参考[echarts的官方文档](https://echarts.apache.org/zh/option.html#color)

输入示例：

* ['#c23531','#2f4554']
* ['yellow','blue','green']

![custom_colors](/ui/screenshot/custom_colors.gif)

## 😉 Author

夜雨微寒，其他昵称：soaringsoul

如果你有一些的好的建议，或者在使用过程中遇到一些问题，欢迎在知乎上给我私信，几乎每天都会去看一下。

[我的知乎主页](https://www.zhihu.com/people/yywh)

## 💌 打赏

如果你觉得项目有帮助到你，可以考虑请作者喝一杯咖啡 😄

| 微信二维码 | 支付宝二维码 |
| -------- | ---------- |
| <img src="/ui/screenshot/wechat_pay.jpg" width = "300"  alt="图片名称" align=center /> | <img src="/ui/screenshot/alipay.jpg" width = "300"  alt="图片名称" align=center /> |
