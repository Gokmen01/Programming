def birthState(presidents):
    states = {'Barack Hussein Obama II':'Hawaii', 'George Walker Bush':'Connecticut',
         'William Jefferson Clinton':'Arkansas',
         'George Herbert Walker Bush':'Massachussetts',
         'Ronald Wilson Reagan':'Illinois',
         'James Earl Carter, Jr':'Georgia'}
    return states[presidents]



print(birthState('James Earl Carter, Jr'))
