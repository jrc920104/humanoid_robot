import math

hip_angle_deg = 90.0 #髋关节
knee_angle_deg = 12.0 #膝关节

def deg_to_rad(degress):
    """角度转换为弧度"""
    return degress * math.pi / 180.0

def rad_to_deg(radians):
    """弧度转换为角度"""
    return radians * 180.0 / math.pi

print(f"髋关节角度{hip_angle_deg}度转换为弧度为{deg_to_rad(hip_angle_deg)}")
print(f"膝关节角度{knee_angle_deg}度转换为弧度为{deg_to_rad(knee_angle_deg)}")
