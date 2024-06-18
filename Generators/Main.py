import matplotlib.pyplot as plt
import subprocess
import os

import secrets

with open('RandomData/PythonSecret.txt', 'w') as file:
    for i in range(2000000):
        bits = bin(secrets.randbits(1))
        file.writelines(bits[2:])

def list_files_in_directory(directory):
    try:
        files_and_directories = os.listdir(directory)
        files = [f for f in files_and_directories if os.path.isfile(os.path.join(directory, f))]
        
        return files
    except FileNotFoundError:
        return f"Error: The directory '{directory}' does not exist."
    except PermissionError:
        return f"Error: You do not have permission to access the directory '{directory}'."

def getDat(test):
    path = 'sts-2.1.2/experiments/AlgorithmTesting/'+test+'/results.txt'
    ok = True
    with open(path, 'r') as file:
        i = 0
        sum = 0
        line = file.readline()
        while line:
            float_value = float(line.strip())
            if float_value < 0.01:
                ok = False
            sum = sum + float_value
            line = file.readline()
            i+=1
    return [sum/i,ok]
    
def create_monogram(s):
    monogram = []
    for char in s:
        if char.isupper():
            monogram.append(char)
    return ''.join(monogram)

executable_path = './assess'

args = ["2000000"]

files = list_files_in_directory('RandomData')

for i in range(len(files)):
    print("["+str(i)+"] "+files[i][:len(files[i])-4])

rType = input("Enter The Tyepe: ")

rType = files[int(rType)]

input_data = "0\n../RandomData/"+rType+"\n1\n0\n1\n0"
working_directory = './sts-2.1.2' 

result = subprocess.run([executable_path]+args,cwd=working_directory,input=input_data, capture_output=True, text=True)
    
tests = ['Frequency','BlockFrequency','CumulativeSums','Runs','LongestRun','Rank','FFT','NonOverlappingTemplate',
         'OverlappingTemplate','Universal','ApproximateEntropy','RandomExcursions','RandomExcursionsVariant','Serial','LinearComplexity']

data = []
names = []
passes = []


for test in tests:
    names.append(create_monogram(test))
    tmp = getDat(test)
    data.append(tmp[0])
    passes.append(tmp[1])

plt.figure(figsize=(12, 6))
for i in range(len(data)):
    color = 'red' if not passes[i] else 'skyblue'
    plt.bar(i, data[i], color=color)

plt.xlabel('Index')
plt.ylabel('Value')
plt.title(rType[:len(rType)-4])
plt.xticks(range(len(data)),names)
plt.axhline(y=0.01, color='red', linestyle='--', linewidth=1)
plt.savefig('test.png')

#-------------------------------------------------------------------------------------------------------------

folder_path = 'sts-2.1.2/experiments/AlgorithmTesting/NonOverlappingTemplate'
float_numbers = []
filenames = []
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            try:
                # Read the float number from the file
                number = float(file.read().strip())
                float_numbers.append(number)
                filenames.append(filename)
            except ValueError:
                a=1

plt.figure(figsize=(12, 6))
plt.bar(range(len(float_numbers)), float_numbers, color='blue', edgecolor='black')
plt.xlabel('Files')
plt.ylabel('Value')
plt.title('Non Overlapping Template Test Results')
plt.xticks(rotation=90)
plt.axhline(y=0.01, color='red', linestyle='--', linewidth=1)
plt.tight_layout()
plt.savefig('NOT.png')
