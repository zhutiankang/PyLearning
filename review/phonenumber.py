

CN_mobile = [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
CN_union = [130,131,132,155,156,185,186,145,176,1709]
CN_telecom = [133,153,180,181,189,177,1700]

def check_phone():
    while True:
        phone_number = input('Enter Your number :')
        prefix = int(phone_number[:3])
        if len(phone_number) != 11:
            print('Invalid length,your number should be in 11 digits')
        elif prefix in CN_mobile :
            print('Operator: China Mobile','We\'re sending verification code',sep='\n')
            break
        elif prefix in CN_union:
            print('Operator: China Union','We\'re sending verification code',sep='\n')
            break
        elif prefix in CN_telecom:
            print('Operator: China Telecom','We\'re sending verification code',sep='\n')
            break
        else:
            print('No such operator')

check_phone()