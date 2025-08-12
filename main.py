from motor_control import p_control_multi

if __name__ == "__main__":
    TARGET_PULSE = 49   # 0.1초간 목표 펄스 (속도)
    KP = 50             # P 상수 조절

    print("3모터 P 제어 시작. Ctrl+C로 종료")
    p_control_multi(TARGET_PULSE, KP)
