def republic():
    domen_name = []
    key = []
    emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
      	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
    domen = list(emails)
    mgu = list(emails['mgu.edu'])
    gm = list(emails['gmail.com'])
    msu = list(emails['msu.edu'])
    yad = list(emails['yandex.ru'])
    hr = list(emails['harvard.edu'])
    ml = list(emails['mail.ru'])
    print(domen)
    new = [domen[]+'@' for domens in domen]
    print(new)



def main():
    republic()



if __name__ == "__main__":
    main()
