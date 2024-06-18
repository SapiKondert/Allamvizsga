import cv2
import time
import matplotlib.pyplot as plt
import numpy as np
from nistrng import *  
from nistrng.sp800_22r1a import *

cam = cv2.VideoCapture(1)



result, image = cam.read()
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.equalizeHist(image)
height, width = image.shape
center_y = height // 2
center_x = width // 2
quarter_y = center_y // 2
quarter_x = center_x // 2
eight_y = quarter_y // 2
eight_x = quarter_x // 2

xcords = [quarter_x,quarter_x+eight_x,center_x,center_x+eight_x,center_x+quarter_x,center_x+quarter_x+eight_x]
ycords = [quarter_y,quarter_y+eight_y,center_y,center_y+eight_y,center_y+quarter_y]
print( len(xcords))
print(len(ycords))
points = 10
for j in range(0,points):
        for k in range(0,points):
            cv2.circle(image, (width//(points-1)*j, height//(points-1)*k), radius=5, color=(255), thickness=-1)

cv2.imshow("1", image) 

cv2.waitKey()

start_time = time.time()
i = 0
medianArray = []
r = [106,233]
pixels = []
zeros = [0] * (r[1]-r[0])
matrix = [[] for _ in range(points*points)]
while i < 10000:
# for i in range(100):
    result, image = cam.read()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.equalizeHist(image)
    for j in range(0,points):
        for k in range(0,points):
            p = image[height//(points-1)*k-1, width//(points-1)*j-1]
            if (p > r[0] and p < r[1]):
                # if len(matrix[j*points+k]) == 0 or abs(p-r[0]-matrix[j*points+k][-1])>15:
                    pixels.append(p)
                    zeros[p-r[0]]+=1
                    matrix[j*points+k].append(p-r[0]+127)
                    # print(bin(p))
                    i+=2
    print(i)
print(matrix)
f_matrix = [element for row in matrix for element in row]
print(f_matrix)
print("Pixels",pixels)
print("Distr",zeros)
print("Max",max(pixels))
print("Min",min(pixels))
print("Avg",sum(pixels) / len(pixels))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
lines = [f"{pixel}\n" for pixel in pixels]

data_array = np.array(pixels)
median = np.median(data_array)

print(median)
medianArray.append(median)
i=0
print(medianArray)




with open('pixels.txt', 'w') as file:
    file.writelines(lines)

lines = [f"{zero}\n" for zero in zeros]

with open('pixels.txt', 'w') as file:
    file.writelines(lines)
bits = []
one = 0
zero = 0
for i in range(0,len(f_matrix)):
    binary_str = bin(f_matrix[i])[2:]
    binary_array = [int(digit) for digit in binary_str]
    bits.append(binary_array[-1])
    bits.append(binary_array[-2])
one = bits.count(1)
zero = bits.count(0)

# Split the binary string into individual digits and store them in an array
binary_array = [int(digit) for digit in binary_str]
print(bits,zero,one,len(bits))
print(f"Elapsed time: {elapsed_time:.2f} seconds")
SP800_22R1A_BATTERY: dict = {
                                "monobit": MonobitTest(),
                                "frequency_within_block": FrequencyWithinBlockTest(),
                                "runs": RunsTest(),
                                "longest_run_ones_in_a_block": LongestRunOnesInABlockTest(),
                                "binary_matrix_rank": BinaryMatrixRankTest(),
                                "dft": DiscreteFourierTransformTest(),
                                "non_overlapping_template_matching": NonOverlappingTemplateMatchingTest(),
                                "overlapping_template_matching": OverlappingTemplateMatchingTest(),#fl
                                "maurers_universal": MaurersUniversalTest(),
                                "linear_complexity": LinearComplexityTest(),#fll
                                "serial": SerialTest(),#fl
                                "approximate_entropy": ApproximateEntropyTest(),
                                "cumulative sums": CumulativeSumsTest(),
                                "random_excursion": RandomExcursionTest(),#fl
                                "random_excursion_variant": RandomExcursionVariantTest()
                            }

a = []
bits_s = np.array(bits)
eligible_battery: dict = check_eligibility_all_battery(bits_s, SP800_22R1A_BATTERY)
print("Eligible test from NIST-SP800-22r1a:")
for name in eligible_battery.keys():
    print("-" + name)
results = run_all_battery(bits_s, eligible_battery, False)
print("Test results:")
for result, elapsed_time in results:
    if result.passed:
        a.append(result.score)
        print("- \033[32mPASSED\033[0m - score: " + str(np.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")
    else:
        a.append(result.score)
        print("- \033[31mFAILED\033[0m - score: " + str(np.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(elapsed_time) + " ms")


plt.figure(figsize=(15, 5))
plt.bar(range(len(zeros)), zeros, color='blue', edgecolor='black')
plt.title('Histogram of Array Values')
plt.xlabel('Position in Array')
plt.ylabel('Value')
plt.show()

# x = range(len(f_matrix))
# plt.figure(figsize=(15, 5))
# plt.plot(x, f_matrix, marker='o')
# plt.title('Number Plot')
# plt.xlabel('Position (Index)')
# plt.ylabel('Number Value')
# plt.show()