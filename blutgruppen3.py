import numpy as np

eskimo = np.array([0.2914, 0.000, 0.0316, 0.6770])
bantu = np.array([0.1034, 0.0866, 0.1200, 0.6900])
englaender = np.array([0.2090, 0.0696, 0.0612, 0.6602])
koreaner = np.array([0.2208, 0.0000, 0.2069, 0.5723])

# länge der vektoren

norm_eskimo = np.linalg.norm(eskimo)
norm_bantu = np.linalg.norm(bantu)
norm_englaender = np.linalg.norm(englaender)
norm_koreaner = np.linalg.norm(koreaner)

# einheitsvektoren

unity_eskimo = eskimo / norm_eskimo
unity_bantu = bantu / norm_bantu
unity_englaender = englaender / norm_englaender
unity_koreaner = koreaner / norm_koreaner

# überprüfung der einheitsvektoren

# print(f" Ausgabe der Einheitsvekoren: \n"
#       f" Eskimo = {unity_eskimo},\n"
#       f" Bantu = {unity_bantu},\n"
#       f" Engländer = {unity_englaender},\n"
#       f" Koreaner = {unity_koreaner}")
#
# print(f" Länge der Einheitsvekoren: \n"
#       f" Eskimo = {np.linalg.norm(unity_eskimo)},\n"
#       f" Bantu = {np.linalg.norm(unity_bantu)},\n"
#       f" Engländer = {np.linalg.norm(unity_englaender)},\n"
#       f" Koreaner = {np.linalg.norm(unity_koreaner)}")


# skalarprodukte aus vektoren

skalar_eskimo_bantu = np.dot(unity_eskimo, unity_bantu)
skalar_eskimo_englaender = np.dot(unity_eskimo, unity_englaender)
skalar_eskimo_koreaner = np.dot(unity_eskimo, unity_koreaner)
skalar_bantu_englaender = np.dot(unity_bantu, unity_englaender)
skalar_bantu_koreaner = np.dot(unity_bantu, unity_koreaner)
skalar_englaender_koreaner = np.dot(unity_englaender, unity_koreaner)

# Ausgabe der Winkel zwischen den Vektoren

print(f" Winkel zwischen \n"
      f" Eskimo_Bantu = {np.degrees(np.arccos(skalar_eskimo_bantu))},\n"
      f" Eskimo_Engländer = {np.degrees(np.arccos(skalar_eskimo_englaender))},\n"
      f" Eskimo_Koreaner = {np.degrees(np.arccos(skalar_eskimo_koreaner))},\n"
      f" Bantu_Engländer = {np.degrees(np.arccos(skalar_bantu_englaender))},\n"
      f" Bantu_Koreaner = {np.degrees(np.arccos(skalar_bantu_koreaner))},\n"
      f" Engländer_Koreaner = {np.degrees(np.arccos(skalar_englaender_koreaner))}")