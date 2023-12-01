calibration_file = open('2.txt', 'r')

DIGIT_STRINGS=["one","two","three","four", "five","six","seven","eight","nine"]

calibration_values = []

while True:
    calibration_line = calibration_file.readline().strip()
    if not calibration_line:
        break
    # replace string digit by their numerical values
    for num_value,str_digit in enumerate( DIGIT_STRINGS,1):
        position = calibration_line.find(str_digit)
        while position != -1:
            calibration_line = calibration_line[:position+2] + str(num_value) + calibration_line[position+2:]
            position = calibration_line.find(str_digit, position+2)


    calibration_value = [ car for car in calibration_line if car.isdigit()]
    calibration_values.append(int(calibration_value[0]+calibration_value[-1]))

print(f"Calibration values: {calibration_values}, Sum: {sum(calibration_values)}")
