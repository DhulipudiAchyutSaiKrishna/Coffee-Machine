spin=input()
electric=input()
if spin=='1/2':
    if electric=='-1/3':
        print('Strange Quark')
    elif electric=='2/3':
        print('Charm Quark')
    elif electric=='-1':
        print('Electron Lepton')
    else:
        print('Muon Lepton')
else:
    print('Photon Boson')
