# 导入虚拟电机和可视化模块
from .motor_control import VirtualMotor

class LegController:
    """腿部控制模块（预演未来SDK使用）"""
    def __init__(self, visualizer=None):
        # 模拟人形机器人的6个腿部电机
        self.joints = {
            'hip_yaw': VirtualMotor(101),
            'hip_roll': VirtualMotor(102),
            'hip_pitch': VirtualMotor(103),
            'knee': VirtualMotor(104),
            'ankle_pitch': VirtualMotor(105),
            'ankle_roll': VirtualMotor(106)
        }
        
        # 设置可视化器
        self.visualizer = visualizer
    
    def stand_position(self):
        """站立姿态控制"""
        print("\n=== 进入站立姿态 ===")
        self.joints['hip_pitch'].set_angle(0)
        self.joints['knee'].set_angle(0)
        self.joints['ankle_pitch'].set_angle(0)
        self._check_status()
        self._update_visualization()
        
    def walk_step(self, step_size=30):
        """行走步态控制"""
        print(f"\n=== 迈步 {step_size}° ===")
        # 简化步态算法
        self.joints['hip_pitch'].set_angle(step_size)
        self.joints['knee'].set_angle(-20)
        self.joints['ankle_pitch'].set_angle(-10)
        self._check_status()
        self._update_visualization()
        
    def _check_status(self):
        """检查关节状态（模拟SDK监控）"""
        for name, motor in self.joints.items():
            status = motor.read_status()
            if status['status'] != "OK":
                print(f"⚠️ 警告！{name}电机温度异常: {status['temp']}°C")
    
    def _update_visualization(self):
        """更新可视化显示"""
        if self.visualizer:
            # 提取关节角度数据
            joint_angles = {}
            for name, motor in self.joints.items():
                joint_angles[name] = motor.position
            # 更新可视化器
            self.visualizer.update_joint_angles(joint_angles)