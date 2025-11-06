import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

class RobotVisualizer:
    """机器人可视化模块"""
    def __init__(self):
        # 创建图形和坐标系
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
        
        # 初始化机器人关节角度
        self.joint_angles = {
            'hip_yaw': 0,
            'hip_roll': 0,
            'hip_pitch': 0,
            'knee': 0,
            'ankle_pitch': 0,
            'ankle_roll': 0
        }
        
        # 机器人尺寸参数
        self.upper_leg_length = 1.0  # 大腿长度
        self.lower_leg_length = 1.0  # 小腿长度
        
        # 设置坐标系范围
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-0.5, 3)
        self.ax.set_aspect('equal')
        self.ax.set_title('人形机器人模拟器')
        self.ax.set_xlabel('X 坐标')
        self.ax.set_ylabel('Y 坐标')
        self.ax.grid(True)
        
        # 初始化机器人各部分的图形对象
        (self.hip_marker,) = self.ax.plot([], [], 'o', markersize=10, color='red')
        (self.upper_leg_line,) = self.ax.plot([], [], '-', linewidth=4, color='blue')
        (self.knee_marker,) = self.ax.plot([], [], 'o', markersize=8, color='green')
        (self.lower_leg_line,) = self.ax.plot([], [], '-', linewidth=4, color='blue')
        (self.ankle_marker,) = self.ax.plot([], [], 'o', markersize=8, color='green')
        (self.foot_line,) = self.ax.plot([], [], '-', linewidth=2, color='brown')
        
        # 初始化动画
        self.animation = None
        self.running = False
        
    def update_joint_angles(self, joint_angles):
        """更新机器人关节角度"""
        self.joint_angles.update(joint_angles)
        self._update_robot_pose()
    
    def _update_robot_pose(self):
        """根据关节角度更新机器人姿态"""
        # 计算各个关节点的位置
        # 髋关节位置
        hip_x = 0
        hip_y = 2.0
        
        # 考虑髋关节俯仰角计算膝关节位置
        hip_pitch = np.radians(self.joint_angles['hip_pitch'])
        knee_x = hip_x + self.upper_leg_length * np.sin(hip_pitch)
        knee_y = hip_y - self.upper_leg_length * np.cos(hip_pitch)
        
        # 考虑膝关节角度计算踝关节位置
        knee_angle = np.radians(self.joint_angles['knee'])
        ankle_x = knee_x + self.lower_leg_length * np.sin(hip_pitch + knee_angle)
        ankle_y = knee_y - self.lower_leg_length * np.cos(hip_pitch + knee_angle)
        
        # 简化的脚的表示
        foot_length = 0.3
        foot_x1 = ankle_x - foot_length * np.cos(hip_pitch + knee_angle)
        foot_y1 = ankle_y - foot_length * np.sin(hip_pitch + knee_angle)
        foot_x2 = ankle_x + foot_length * np.cos(hip_pitch + knee_angle)
        foot_y2 = ankle_y + foot_length * np.sin(hip_pitch + knee_angle)
        
        # 更新图形对象
        self.hip_marker.set_data([hip_x], [hip_y])
        self.upper_leg_line.set_data([hip_x, knee_x], [hip_y, knee_y])
        self.knee_marker.set_data([knee_x], [knee_y])
        self.lower_leg_line.set_data([knee_x, ankle_x], [knee_y, ankle_y])
        self.ankle_marker.set_data([ankle_x], [ankle_y])
        self.foot_line.set_data([foot_x1, foot_x2], [foot_y1, foot_y2])
    
    def start_animation(self, update_func=None, interval=100):
        """开始动画显示"""
        self.running = True
        
        if update_func is None:
            # 默认更新函数
            def default_update(frame):
                return (self.hip_marker, self.upper_leg_line, self.knee_marker, 
                        self.lower_leg_line, self.ankle_marker, self.foot_line)
            update_func = default_update
        
        self.animation = FuncAnimation(
            self.fig, update_func,
            interval=interval,
            blit=True,
            cache_frame_data=False
        )
    
    def show(self):
        """显示图形"""
        plt.show()
    
    def close(self):
        """关闭图形"""
        self.running = False
        if self.animation:
            self.animation.event_source.stop()
        plt.close(self.fig)