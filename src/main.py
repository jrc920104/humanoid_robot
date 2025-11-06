import time
# 导入必要的模块
from core.leg_controller import LegController
from utils.visualization import RobotVisualizer

def robot_greeting():
    """机器人问候函数"""
    print("\n  ____  ")
    print(" |  o|  Hello! 我是你的机器人助手")
    print(" /___\\ ")
    print("   |   ")
    print("  / \\  Ready to learn robotics!")

# 定义动画更新函数
def animation_update(frame):
    global leg, step_count, total_steps
    
    # 执行步进动作
    if step_count < total_steps:
        import random
        random_step = random.randint(20, 60)  # 生成20到60之间的随机步长
        leg.walk_step(step_size=random_step)
        print(f"执行随机步长行走: {random_step}")
        step_count += 1
        # 短暂暂停以观察动作
        time.sleep(0.5)
    
    # 返回所有需要更新的图形对象
    return leg.visualizer.hip_marker, leg.visualizer.upper_leg_line, leg.visualizer.knee_marker, \
           leg.visualizer.lower_leg_line, leg.visualizer.ankle_marker, leg.visualizer.foot_line

if __name__ == "__main__":
    robot_greeting()
    
    # 创建可视化器实例
    visualizer = RobotVisualizer()
    
    # 创建腿部控制器实例，并关联可视化器
    print("\n=== 初始化腿部控制器 ===")
    leg = LegController(visualizer=visualizer)
    
    # 设置动画参数
    step_count = 0
    total_steps = 20
    
    # 测试站立姿态
    leg.stand_position()
    time.sleep(1)
    
    # 启动动画
    visualizer.start_animation(update_func=animation_update, interval=500)
    
    # 显示图形
    visualizer.show()