def pokemon(lil):
    mini=lil[0]
    maxi=lil[0]
    for i in lil:
        mini=min(mini,i)
        maxi=max(maxi,i)
        print(f'{mini} {maxi}')

lil=list(map(int,input().split()))
pokemon(lil)
