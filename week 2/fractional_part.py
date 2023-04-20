def fractional_part(numerator,denominator):
    if denominator==0:
        return 0
    mod_r = numerator % denominator
    frac_r = mod_r / denominator
    if frac_r==0:
        return int(frac_r)
    return frac_r

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
