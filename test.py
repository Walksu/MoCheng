import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from douyin_crawler import *
from bilibili_crawler import *

class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        '''
        :param:第一列按钮垂直布局
        :return:
        '''
        # 工具按钮新建
        self.tb9 = QToolButton(self)
        # self.tb9.setText("")
        self.tb9.setIconSize(QSize(65, 65))
        # 悬停文本
        self.tb9.setToolTip("个人中心")

        self.tb1 = QToolButton(self)
        self.tb1.setText("新建")
        # 添加菜单
        self.customAct = QAction("自定义工作", self)
        self.modeAct = QAction("模板工作", self)
        self.downloadAct = QAction("导入工作", self)
        self.createAct = QAction("新建工作组", self)
        self.tb1_menu = QMenu(self)
        self.tb1_menu.addAction(self.customAct)
        self.tb1_menu.addSeparator()
        self.tb1_menu.addAction(self.modeAct)
        self.tb1_menu.addSeparator()
        self.tb1_menu.addAction(self.downloadAct)
        self.tb1_menu.addSeparator()
        self.tb1_menu.addAction(self.createAct)
        self.tb1.setMenu(self.tb1_menu)
        # 添加悬停事件
        # self.tb1.enterEvent = self.showMenu
        # 监控菜单的离开事件
        # self.tb1_menu.installEventFilter(self)
        # 位置设定
        # self.tb1.move(16, 120)

        # 工具按钮任务
        self.tb2 = QToolButton(self)
        self.tb2.setText("任务")
        self.tb2.setAutoRaise(True)
        # 悬停文本
        self.tb2.setToolTip("任务")
        #位置设定
        # self.tb2.move(16, 210)

        # 工具按钮模板
        self.tb3 = QToolButton(self)
        self.tb3.setText("模板")
        self.tb3.setIconSize(QSize(65, 65))
        self.tb3.setAutoRaise(True)
        self.tb3.setArrowType(Qt.ArrowType.NoArrow)
        # 悬停文本
        self.tb3.setToolTip("模板")
        # 位置设定
        # self.tb3.move(16, 305)

        # 工具按钮工具
        self.tb4 = QToolButton(self)
        self.tb4.setText("工具")
        self.tb4.setIconSize(QSize(57, 57))
        # 悬停文本
        self.tb4.setToolTip("工具")
        # 位置设定
        # self.tb4.move(12, 395)

        # 工具按钮会员
        self.tb10 = QToolButton(self)
        self.tb10.setText("会员")
        self.tb10.setIconSize(QSize(65, 65))
        # 悬停文本
        self.tb10.setToolTip("会员")

        # 工具按钮墨城RPA
        self.tb5 = QToolButton(self)
        self.tb5.setText("墨城RPA")
        self.tb5.setIconSize(QSize(60, 60))
        # 悬停文本
        self.tb5.setToolTip("墨城RPA")

        # 工具按钮消息
        self.tb6 = QToolButton(self)
        self.tb6.setText("消息")
        self.tb6.setIconSize(QSize(65, 65))
        # 悬停文本
        self.tb6.setToolTip("消息")

        # 工具按钮帮助
        self.tb7 = QToolButton(self)
        self.tb7.setText("帮助")
        self.tb7.setIconSize(QSize(65, 65))
        # 悬停文本
        self.tb7.setToolTip("帮助")

        # 工具按钮设置
        self.tb8 = QToolButton(self)
        self.tb8.setText("设置")
        self.tb8.setIconSize(QSize(65, 65))
        # 悬停文本
        self.tb8.setToolTip("设置")

        # 布局
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.tb9)
        vbox1.addWidget(self.tb1)
        vbox1.addWidget(self.tb2)
        vbox1.addWidget(self.tb3)
        vbox1.addWidget(self.tb4)
        vbox1.addStretch()
        vbox1.addWidget(self.tb10)
        vbox1.addWidget(self.tb5)
        vbox1.addStretch()
        vbox1.addWidget(self.tb6)
        vbox1.addWidget(self.tb7)
        vbox1.addWidget(self.tb8)
        # self.setLayout(vbox1)

        '''
        :param:首页水平布局
        :return:
        '''
        # 创建标签页容器-首页
        tab1_widget = QTabWidget(self)
        tab1 = QWidget()
        tab1_hbox = QHBoxLayout()
        # 子布局1
        son_vbox1 = QVBoxLayout()
        # 子布局1-1
        son_son_hbox1 = QHBoxLayout()
        tab1_label1 = QLabel("您好，欢迎使用墨城数据分析！")
        # 子布局1-2
        son_son_hbox2 = QHBoxLayout()
        text_input = QLineEdit()
        text_input.setPlaceholderText("输入要采集的网站名称或网址......")
        search_btn = QPushButton("->开始采集")
        son_son_hbox2.addWidget(text_input)
        son_son_hbox2.addWidget(search_btn)
        # 子布局1-3
        son_son_hbox3 = QHBoxLayout()
        tab2_widget = QTabWidget(self)
        tab2 = QWidget()
        tab2_widget.addTab(tab2, "热门模板")
        tab2.setLayout(son_son_hbox3)
        son_son_hbox1.addWidget(tab1_label1)
        son_vbox1.addLayout(son_son_hbox1, 1)
        son_vbox1.addLayout(son_son_hbox2, 2)
        son_vbox1.addWidget(tab2_widget, 5)
        # 子布局2
        son_vbox2 = QVBoxLayout()
        # 子布局2-1
        son_son_vbox1 = QVBoxLayout()
        tab3_widget = QTabWidget(self)
        tab3 = QWidget()
        tab3_widget.addTab(tab3, "热门资讯")
        tab3.setLayout(son_son_vbox1)
        # 子布局2-2
        son_son_vbox2 = QVBoxLayout()
        tab4_widget = QTabWidget(self)
        tab4 = QWidget()
        tab4_widget.addTab(tab4, "每日福利")
        tab4.setLayout(son_son_vbox2)
        son_vbox2.addWidget(tab3_widget, 3)
        son_vbox2.addWidget(tab4_widget, 4)
        # 首页主布局
        tab1_hbox.addLayout(son_vbox1, 2)
        tab1_hbox.addLayout(son_vbox2, 1)
        tab1.setLayout(tab1_hbox)
        tab1_widget.addTab(tab1, "首页")

        # 主布局
        hbox1 = QHBoxLayout()
        hbox1.addLayout(vbox1)
        hbox1.addWidget(tab1_widget)
        self.setLayout(hbox1)

        # 窗口
        self.setGeometry(240, 150, 1200, 800)
        self.setWindowTitle("墨城数据分析")

    # def showMenu(self, event):
    #     self.tb1_menu.popup(self.tb1.mapToGlobal(QPoint(0, self.tb1.height())))
    #
    # def eventFilter(self, obj, event):
    #     if obj == self.tb1_menu and event.type() == QEvent.Leave:
    #         self.tb1_menu.hide()
    #     return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = main_window()
    # app.setStyleSheet()
    sys.exit(app.exec())