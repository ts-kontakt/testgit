import sqlitehelper as sqh
#example commits

con, cur = sqh.get_con_cur('c:\\1dane\\baza_sprzed.sdb')
def get_km():
    outdict = {}
    for row in cur.execute('select * from klienci_km'):
        id, logo, odl =  row
        outdict[id] = odl
    return outdict
    
if __name__ == '__main__': 
    print 1
    print get_km()
    

    