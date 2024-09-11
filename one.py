import curses
import time
import random
def draw_border(win):
    win.border(0)  # 画边框
def display_info(win, counter):
    win.addstr(1, 2, "Dynamic Counter: ", curses.color_pair(2))
    win.addstr(1, 20, str(counter), curses.color_pair(1))
    win.addstr(3, 2, "Press 'q' to exit", curses.color_pair(2))
def main(stdscr):
    # 清空屏幕
    stdscr.clear()
    # 初始化颜色
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # 绿色文本
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)   # 青色文本
    # 创建多个窗口
    height, width = 10, 40
    win_main = curses.newwin(height, width, 5, 5)
    # 初始化变量
    counter = 0
    # 主循环
    while True:
        counter += random.randint(-1, 1)  # 随机更新计数器
        # 绘制窗口边框
        draw_border(win_main)
        # 显示信息
        display_info(win_main, counter)
        # 刷新窗口
        win_main.refresh()
        # 每隔一段时间更新
        time.sleep(0.5)
        # 检测用户按键
# 运行 curses 应用
curses.wrapper(main)
