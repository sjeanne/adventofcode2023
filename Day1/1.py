calibration_file = open('1.txt', 'r')

calibration_values = []

while True:
    calibration_line = calibration_file.readline().strip()
    if not calibration_line:
        break
    calibration_value = [ car for car in calibration_line if car.isdigit()]
    calibration_values.append(int(calibration_value[0]+calibration_value[-1]))

print(f"Calibration values: {calibration_values}, Sum: {sum(calibration_values)}")
