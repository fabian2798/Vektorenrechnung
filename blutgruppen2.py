import numpy as np
import math


eskimo = np.array([0.2914, 0.000, 0.0316, 0.6770])
bantu = np.array([0.1034, 0.0866, 0.1200, 0.6900])
englaender = np.array([0.2090, 0.0696, 0.0612, 0.6602])
koreaner = np.array([0.2208, 0.0000, 0.2069, 0.5723])


# einheitsvektor
# vektor durch länge des vektors
# länge des vektors = wurzel aus sum von vektorkomponenten hoch 2

unit_eskimo = np.sqrt(eskimo)
unit_bantu = np.sqrt(bantu)
unit_englaender = np.sqrt(englaender)
unit_koreaner = np.sqrt(koreaner)

print(np.sqrt(sum(np.square(unit_koreaner))))


# skalarprodukt aus einheitsvektoren

unit_eskimo_bantu = ((unit_eskimo[0]*unit_bantu[0]) + (unit_eskimo[1]*unit_bantu[1]) +
                (unit_eskimo[2]*unit_bantu[2]) + (unit_eskimo[3]*unit_bantu[3]))

unit_eskimo_englaender = ((unit_eskimo[0]*unit_englaender[0]) + (unit_eskimo[1]*unit_englaender[1]) +
                     (unit_eskimo[2]*unit_englaender[2]) + (unit_eskimo[3]*unit_englaender[3]))

unit_eskimo_koreaner = ((unit_eskimo[0]*unit_koreaner[0]) + (unit_eskimo[1]*unit_koreaner[1]) +
                   (unit_eskimo[2]*unit_koreaner[2]) + (unit_eskimo[3]*unit_koreaner[3]))

unit_bantu_englaender = ((unit_englaender[0]*unit_bantu[0]) + (unit_englaender[1]*unit_bantu[1]) +
                    (unit_englaender[2]*unit_bantu[2]) + (unit_englaender[3]*unit_bantu[3]))

unit_bantu_koreaner = ((unit_koreaner[0]*unit_bantu[0]) + (unit_koreaner[1]*unit_bantu[1]) +
                  (unit_koreaner[2]*unit_bantu[2]) + (unit_koreaner[3]*unit_bantu[3]))

unit_englaender_koreaner = ((unit_koreaner[0]*unit_englaender[0]) + (unit_koreaner[1]*unit_englaender[1]) +
                       (unit_koreaner[2]*unit_englaender[2]) + (unit_koreaner[3]*unit_englaender[3]))



# Ähnlichkeitswinkel

print(f" Enfernungswinkel von \n"
      f" Eskimo_Bantu = {math.degrees(math.acos(unit_eskimo_bantu))},\n"
      f" Eskimo_Engländer = {math.degrees(math.acos(unit_eskimo_englaender))},\n"
      f" Eskimo_Koreaner = {math.degrees(math.acos(unit_eskimo_koreaner))},\n"
      f" Bantu_Engländer = {math.degrees(math.acos(unit_bantu_englaender))},\n"
      f" Bantu_Koreaner = {math.degrees(math.acos(unit_bantu_koreaner))},\n"
      f" Engländer_Koreaner = {math.degrees(math.acos(unit_englaender_koreaner))}")