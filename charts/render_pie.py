import pandas as pd
from PyQt5 import QtCore


from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig


CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/npm/echarts@5.0.0/dist/"


class RenderPie(QtCore.QThread):
    finished_signal = QtCore.pyqtSignal(str)
    error_signal = QtCore.pyqtSignal(str)
    result_signal = QtCore.pyqtSignal(str)
    charts_data_signal = QtCore.pyqtSignal(list)
    progress_signal = QtCore.pyqtSignal(str)

    def __init__(self,
                 df, col_name,
                 is_donut, is_rose,
                 show_legend,
                 title,
                 label_position,
                 label_formatter,
                 color_scheme,
                 ):
        super(RenderPie, self).__init__()
        self.df = df
        self.col_name = col_name
        self.is_donut = is_donut
        self.is_rose = is_rose
        self.show_legend = show_legend
        self.title = title
        if self.title == "":
            self.title = col_name
        self.label_position = label_position
        if self.label_position:
            self.label_position_value = "inside"
        else:
            self.label_position_value = "outside"
        self.label_formatter = label_formatter
        print(self.label_formatter)
        self.color_scheme = color_scheme


    def run(self):
        # 拉取云端数据
        if self.df is not None:
            # 读取配置项

            if self.is_donut:
                radius = ["40%", "75%"]
            else:
                radius = None
            if self.is_rose:
                rosetype = "area",
            else:
                rosetype = None
            s = self.df[self.col_name].value_counts()
            attrs = [x for x in s.keys()]
            values = [float(y) for y in s.values]
            data_lst = [list(z) for z in zip(attrs, values)]

            self.charts_data_signal.emit(data_lst)
            c = (
                Pie()
                    .add(
                    "",
                    data_lst,
                    radius=radius,
                    rosetype=rosetype
                )
                    .set_colors(self.color_scheme)
                    .set_global_opts(
                    title_opts=opts.TitleOpts(
                        title=self.title,
                        pos_left="center",
                        pos_top="top"
                    ),
                    legend_opts=opts.LegendOpts(
                        # 是否显示图例组件
                        is_show=self.show_legend,

                        # 图例的类型。可选值：
                        # 'plain'：普通图例。缺省就是普通图例。
                        # 'scroll'：可滚动翻页的图例。当图例数量较多时可以使用。
                        type_='scroll',

                        # 图例选择的模式，控制是否可以通过点击图例改变系列的显示状态。默认开启图例选择，可以设成 false 关闭
                        # 除此之外也可以设成 'single' 或者 'multiple' 使用单选或者多选模式。
                        # selected_mode = False,
                        selected_mode=True,
                        # selected_mode = 'multiple',

                        # 图例组件离容器左侧的距离。
                        # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，

                        # 也可以是 'left', 'center', 'right'。
                        # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
                        # pos_left = 50,
                        pos_left='right',
                        # pos_left = 'left',

                        # 图例组件离容器右侧的距离（同上）。
                        # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
                        pos_right=None,

                        # 图例组件离容器上侧的距离（同上）。
                        # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
                        # 也可以是 'top', 'middle', 'bottom'。
                        # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。
                        pos_top='top',

                        # 图例组件离容器下侧的距离（同上）。
                        # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
                        pos_bottom=None,

                        # 图例列表的布局朝向。可选：'horizontal', 'vertical'
                        orient='vertical',

                        # 图例标记和文本的对齐。默认自动（auto）
                        # 根据组件的位置和 orient 决定
                        # 当组件的 left 值为 'right' 以及纵向布局（orient 为 'vertical'）的时候为右对齐，即为 'right'。
                        # 可选参数: `auto`, `left`, `right`
                        align=None,

                        # 图例内边距，单位px，默认各方向内边距为5
                        padding=5,

                        # 图例每项之间的间隔。横向布局时为水平间隔，纵向布局时为纵向间隔。
                        # 默认间隔为 10
                        item_gap=20,

                        # 图例标记的图形宽度。默认宽度为 25
                        item_width=50,

                        # 图例标记的图形高度。默认高度为 14
                        item_height=14,

                        # 图例关闭时的颜色。默认是 #ccc
                        inactive_color='#E6E61A',

                        # 图例组件字体样式，参考 `series_options.TextStyleOpts`
                        textstyle_opts=None,

                        # 图例项的 icon。
                        # ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
                        # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。
                        # 可以通过 'path://' 将图标设置为任意的矢量路径。
                        legend_icon='pin',

                    )

                )
                    .set_series_opts(label_opts=opts.LabelOpts(
                    # is_show=True 是否显示标签
                    is_show=True,

                    # position 标签的位置 可选 'top'，'left'，'right'，'bottom'，'inside'，'insideLeft'，'insideRight'.....
                    position=self.label_position_value,

                    # font_size 文字的字体大小
                    # font_size=10,

                    # color 文字的颜色

                    # font_style 文字字体的风格，可选 'normal'，'italic'，'oblique'

                    # font_weight 文字字体的粗细  'normal'，'bold'，'bolder'，'lighter'
                    font_weight='normal',

                    # font_family 字体 'Arial', 'Courier New', 'Microsoft YaHei（微软雅黑）' ....
                    font_family=None,

                    # rotate 标签旋转 从 -90 度到 90 度。正值是逆时针

                    # margin 刻度标签与轴线之间的距离
                    margin=20,

                    # 坐标轴刻度标签的显示间隔，在类目轴中有效。Union[Numeric, str, None]
                    # 默认会采用标签不重叠的策略间隔显示标签。
                    # 可以设置成 0 强制显示所有标签。
                    # 如果设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推。
                    # 可以用数值表示间隔的数据，也可以通过回调函数控制。回调函数格式如下：
                    # (index:number, value: string) => boolean
                    # 第一个参数是类目的 index，第二个值是类目名称，如果跳过则返回 false。
                    interval=None,

                    # horizontal_align 文字水平对齐方式，默认自动。可选：'left'，'center'，'right'

                    # vertical_align 文字垂直对齐方式，默认自动。可选：'top'，'middle'，'bottom'
                    # 其中变量a、b、c在不同图表类型下代表数据含义为：
                    # 折线（区域）图、柱状（条形）图: a（系列名称），b（类目值），c（数值）, d（无）
                    # 散点图（气泡）图: a（系列名称），b（数据名称），c（数值数组）, d（无）
                    # 饼图、雷达图: a（系列名称），b（数据项名称），c（数值）, d（百分比）
                    formatter=self.label_formatter
                ))
            )
            self.result_signal.emit(c.render_embed())

        else:
            self.show_progress("你还没有导入文件哦！")
