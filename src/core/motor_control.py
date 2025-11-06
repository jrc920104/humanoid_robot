class VirtualMotor:
    """虚拟电机控制器（模拟未来真实SDK）"""
    def __init__(self, motor_id):
        self.motor_id = motor_id
        self.position = 0.0
        self.temperature = 25.0
        
    def set_angle(self, angle, speed=50.0):
        """设置电机角度（模拟真实SDK方法）"""
        if not -180 <= angle <= 180:
            raise ValueError(f"电机{self.motor_id}角度超限: {angle}°")
            
        # 模拟物理运动过程
        print(f"♻️ 电机{self.motor_id}: {self.position}° → {angle}° (速度{speed}%/s)")
        # 先计算温度变化，再更新位置
        temp_change = 0.5 * abs(angle - self.position)
        self.temperature += temp_change
        self.position = angle
            
    def read_status(self):
        """读取电机状态（模拟SDK数据反馈）"""
        return {
            "motor_id": self.motor_id,
            "position": self.position,
            "temp": round(self.temperature, 1),
            "status": "OK" if self.temperature < 70 else "OVERHEAT"
        }