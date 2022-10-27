complex_num = complex(input("Enter a complex number: "))
real_part = complex_num.real
img_part = complex_num.imag
print(real_part, img_part)
if real_part > img_part:
    print("Real part is greater")
else:
    print("Imaginary part is greater")