
#KEYWORD ARGUEMENTS

def marks(**data):
    with open('marks.txt','a') as f:
            for n,m in data.items():
                f.write(f'{n}:{m}\n')

marks(rajesh=200, brijesh=124)
marks(raj=130, ajay=150, suraj=128, jai=90)
marks()
