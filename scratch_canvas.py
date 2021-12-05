side = int(input(''))
peri_sq = 4 * side
area_sq = side ** 2
area_cube = 6 * side ** 2
vol_cube = side ** 3
print(peri_sq)
print(area_sq)
print(area_cube)
print(vol_cube)

radius = int(input(''))
peri_cir = (2 * (22 / 7)) * radius
area_cir = (22 / 7) * radius ** 2
area_sph = (4 * (22 / 7)) * radius ** 2
vol_sph = ((4 / 3) * (22 / 7)) * radius ** 3
print(peri_cir)
print(area_cir)
print(area_sph)
print(vol_sph)

area_cone = ((22 / 7) * side) * radius
print(area_cone)
