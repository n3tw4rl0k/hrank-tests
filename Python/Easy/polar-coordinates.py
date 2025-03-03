import cmath

# test case 1
# input_sample = "1+2j"

complex_num = complex(input().strip())

modulus = abs(complex_num)
phase = cmath.phase(complex_num)

print(modulus)
print(phase)