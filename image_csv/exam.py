import cv2
import numpy as np
import csv

# 이미지 경로
image_path = "img4.png"

# 이미지 읽기
image = cv2.imread(image_path)

# 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 특정 색상을 강조
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# 외곽선 찾기
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(contours)

# CSV 데이터를 담을 리스트
csv_data = [["Label", "Bad", "Checkbox 1", "Checkbox 2", "Checkbox 3", "Checkbox 4", "Checkbox 5", "Good"]]

# 각 행의 정보를 추출하고 CSV 데이터에 추가
for i, contour in enumerate(contours):
    # 외곽선의 영역 계산
    area = cv2.contourArea(contour)
    print(i,":",area)

    # 일정 크기 이상의 외곽선만 처리
    if area > 1000:
        # 외곽선을 감싸는 최소 사각형 찾기
        x, y, w, h = cv2.boundingRect(contour)

        # "나쁨"과 "좋음" 영역의 중심 좌표 계산
        bad_x = x + w // 4
        good_x = x + 3 * w // 4
        center_y = y + h // 2

        # 각 체크박스의 중심 좌표 계산
        checkbox_centers = []
        for i in range(5):
            center_x = x + w // 10 + (2 * w // 5) * i
            checkbox_centers.append(center_x)

        # 각 영역에서 체크박스의 상태 확인 (색칠 여부)
        bad_state = "Filled" if binary[center_y, bad_x] == 0 else "Empty"
        checkbox_states = ["Filled" if binary[center_y, x] == 0 else "Empty" for x in checkbox_centers]
        good_state = "Filled" if binary[center_y, good_x] == 0 else "Empty"

        # CSV 데이터에 추가
        csv_data.append([f"Row {i + 1}", bad_state, *checkbox_states, good_state])

# CSV 파일 쓰기
csv_file_path = "output_data.csv"
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("CSV 파일이 생성되었습니다.")
