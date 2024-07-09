import string


def NbCMin(mot_de_passe):
    minuscule_max = 0
    for i in mot_de_passe:
        if i in string.ascii_lowercase:
            minuscule_max += 1
    return minuscule_max


def NbCMaj(mot_de_passe):
    majuscule_max=0
    for i in mot_de_passe:
        if i in string.ascii_uppercase:
            majuscule_max+=1
    return majuscule_max


def NbCAlpha(mot_de_passe):
    return len(mot_de_passe)


def LongMaj(mot_de_passe):
    sequences_maj=[]
    longue_sequence_maj=""
    qte_longue_sequence_maj=0
    mot=""
    for i in mot_de_passe:
        if i in string.ascii_uppercase:
                mot+=i
        else:
            if mot !="":
                sequences_maj.append(mot)
            mot=""
    for i in sequences_maj:
        if len(i)>qte_longue_sequence_maj:
            longue_sequence_maj = i

    return len(longue_sequence_maj)



def LongMin(mot_de_passe):
    sequences_min=[]
    longue_sequence_min=""
    qte_longue_sequence_min=0
    mot=""
    for i in mot_de_passe:
        if i in string.ascii_lowercase:
                mot+=i
        else:
            if mot !="":
                sequences_min.append(mot)
            mot=""
    for i in sequences_min:
        if len(i)>qte_longue_sequence_min:
            longue_sequence_min = i

    return len(longue_sequence_min)

def NbCNonAlpha(mot_de_passe):
    nonAlpha_max = 0
    for i in mot_de_passe:
        if i not in string.ascii_letters:
            nonAlpha_max+=1
    return nonAlpha_max


def Score(mot_de_passe):
    bonus = (NbCAlpha(mot_de_passe)*4)+((NbCAlpha(mot_de_passe)-NbCMaj(mot_de_passe))*2)+((NbCAlpha(mot_de_passe)-NbCMin(mot_de_passe))*3)+(NbCNonAlpha(mot_de_passe)*5)
    penalite = (LongMaj(mot_de_passe)*2)+(LongMin(mot_de_passe)*3)

    score = bonus-penalite
    if score<20:
        return "\nLa force du mot de passe est ‘Très faible’\n"
    elif score<40:
        return "\nLa force d’un mot de passe est ‘Faible’\n"
    elif score<80:
        return "\nLa force du mot de passe est ‘Fort’\n"
    else:
        return "\nLa force du mot de passe est ‘Très fort’\n"

print(Score("P@cSI_promo2017"))
# print(NbCNonAlpha("P@cSI_promo2017"))
# print(LongMin("LUcienKANANi"))
# print(LongCNonAlpha("Lucien12Kan6"))