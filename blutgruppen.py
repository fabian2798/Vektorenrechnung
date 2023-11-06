import numpy as np
import math

eskimo = np.array([0.2914, 0.000, 0.0316, 0.6770])
bantu = np.array([0.1034, 0.0866, 0.1200, 0.6900])
englaender = np.array([0.2090, 0.0696, 0.0612, 0.6602])
koreaner = np.array([0.2208, 0.0000, 0.2069, 0.5723])

# ekulische norm
# länge der vektoren
# wurzel aus sum von vektorkomponenten hoch 2
# ||eskimo|| = bezeichnung#
# np.linalg.norm(vektor)


euk_eskimo = np.sqrt(sum(np.square(eskimo)))
euk_bantu = np.sqrt(sum(np.square(bantu)))
euk_englaender = np.sqrt(sum(np.square(englaender)))
euk_koreaner = np.sqrt(sum(np.square(koreaner)))

print(f" Euklische Norm von \n"
      f" Eskimo = {euk_eskimo},\n"
      f" Bantu = {euk_bantu},\n"
      f" Engländer = {euk_englaender},\n"
      f" Koreaner = {euk_koreaner}")


#skalarprodukte
# a11*a12 + a21*a22 + a31*32 + a41*a42
# [a11,a21,a31,a41]
# [a12,a22,a32,a42]
# np.dot(vektor1, vektor2)

eskimo_bantu = (eskimo[0]*bantu[0]) + (eskimo[1]*bantu[1]) + (eskimo[2]*bantu[2]) + (eskimo[3]*bantu[3])
eskimo_englaender = (eskimo[0]*englaender[0]) + (eskimo[1]*englaender[1]) + (eskimo[2]*englaender[2]) + (eskimo[3]*englaender[3])
eskimo_koreaner = (eskimo[0]*koreaner[0]) + (eskimo[1]*koreaner[1]) + (eskimo[2]*koreaner[2]) + (eskimo[3]*koreaner[3])
bantu_englaender = (englaender[0]*bantu[0]) + (englaender[1]*bantu[1]) + (englaender[2]*bantu[2]) + (englaender[3]*bantu[3])
bantu_koreaner = (koreaner[0]*bantu[0]) + (koreaner[1]*bantu[1]) + (koreaner[2]*bantu[2]) + (koreaner[3]*bantu[3])
englaender_koreaner = (koreaner[0]*englaender[0]) + (koreaner[1]*englaender[1]) + (koreaner[2]*englaender[2]) + (koreaner[3]*englaender[3])


# print(f" Skalarprodukt von Eskimo_Bantu = {euk_eskimo},"
#       f" Eskimo_Engländer = {eskimo_englaender},"
#       f" Eskimo_Koreaner = {eskimo_koreaner}, "
#       f" Bantu_Engländer = {euk_bantu}, "
#       f" Bantu_Koreaner = {euk_englaender},"
#       f" Engländer_Koreaner = {euk_koreaner}")


# kosinus ähnlichkeit
# skalarprodukt / (||eskimo||*||bantu||)

cos_similar_eskimo_bantu = eskimo_bantu / (euk_eskimo*euk_bantu)
cos_similar_eskimo_englaender = eskimo_englaender / (euk_eskimo*euk_englaender)
cos_similar_eskimo_koreaner = eskimo_koreaner / (euk_eskimo*euk_koreaner)
cos_similar_bantu_englaender = bantu_englaender / (euk_bantu*euk_englaender)
cos_similar_bantu_koreaner = bantu_koreaner / (euk_bantu*euk_koreaner)
cos_similar_englaender_koreaner = englaender_koreaner / (euk_englaender*euk_koreaner)


# print(f" Kosinus-Ähnlichkeit von Eskimo_Bantu = {cos_similar_eskimo_bantu},"
#       f" Eskimo_Engländer = {cos_similar_eskimo_englaender},"
#       f" Eskimo_Koreaner = {cos_similar_eskimo_koreaner}, "
#       f" Bantu_Engländer = {cos_similar_bantu_englaender}, "
#       f" Bantu_Koreaner = {cos_similar_bantu_koreaner},"
#       f" Engländer_Koreaner = {cos_similar_englaender_koreaner}")


# Entfernungswinkel (Teta)
# ArcKosinus (cos hoch -1) von der Kosinus-Ähnlichkeit

print(f" Entfernungswinkel von \n"
      f" Eskimo_Bantu = {math.degrees(math.acos(cos_similar_eskimo_bantu))},\n"
      f" Eskimo_Engländer = {math.degrees(math.acos(cos_similar_eskimo_englaender))},\n"
      f" Eskimo_Koreaner = {math.degrees(math.acos(cos_similar_eskimo_koreaner))},\n"
      f" Bantu_Engländer = {math.degrees(math.acos(cos_similar_bantu_englaender))},\n"
      f" Bantu_Koreaner = {math.degrees(math.acos(cos_similar_bantu_koreaner))},\n"
      f" Engländer_Koreaner = {math.degrees(math.acos(cos_similar_englaender_koreaner))}")

# euklische distanz
# länge zwischen zwei vektoren
# np.linalg.norm

print(f" Euklische Distanz von Eskimo_Bantu = {np.linalg.norm(eskimo - bantu)},"
      f" Eskimo_Engländer = {np.linalg.norm(eskimo - englaender)},"
      f" Eskimo_Koreaner = {np.linalg.norm(eskimo - koreaner)}, "
      f" Bantu_Engländer = {np.linalg.norm(bantu - englaender)}, "
      f" Bantu_Koreaner = {np.linalg.norm(bantu - koreaner)},"
      f" Engländer_Koreaner = {np.linalg.norm(englaender - koreaner)}")


