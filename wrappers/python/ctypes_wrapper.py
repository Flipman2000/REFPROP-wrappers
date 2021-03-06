from __future__ import print_function
import ctypes as ct

class REFPROPFunctionLibrary():
    def __init__(self, name):
        self.dll = ct.WinDLL(name)

        self._SETUPdll = getattr(self.dll, 'SETUPdll')
        self._LIMITSdll = getattr(self.dll, 'LIMITSdll')
        self._MELTTdll = getattr(self.dll, 'MELTTdll')
        self._TDFLSHdll = getattr(self.dll, 'TDFLSHdll')
        self._PEFLSHdll = getattr(self.dll, 'PEFLSHdll')
        self._CRTPNTdll = getattr(self.dll, 'CRTPNTdll')
        self._CRITPdll = getattr(self.dll, 'CRITPdll')
        self._SATTdll = getattr(self.dll, 'SATTdll')
        self._SATTPdll = getattr(self.dll, 'SATTPdll')
        self._TQFLSHdll = getattr(self.dll, 'TQFLSHdll')

    def SETUPdll(self, nc, fld, hmx, ref):
        nc = ct.c_long(nc)
        hfld = ct.create_string_buffer(fld, 10001)
        hhmx = ct.create_string_buffer(hmx, 256)
        href = ct.create_string_buffer(ref, 4)
        ierr = ct.c_long(0)
        herr = ct.create_string_buffer(255)

        self._SETUPdll(ct.byref(nc), hfld, hhmx, href, ct.byref(ierr), herr, 10000, 255, 3, 255)
        return ierr.value, str(herr.raw)

    def LIMITSdll(self, typ, z):
        htyp = ct.create_string_buffer(typ, 4)
        Tmin, Tmax, Dmax, Pmax = ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double()
        z = (len(z)*ct.c_double)(*z)

        self._LIMITSdll(htyp, z, ct.byref(Tmin), ct.byref(Tmax), ct.byref(Dmax), ct.byref(Pmax), 3)
        return Tmin.value, Tmax.value, Dmax.value, Pmax.value

    def MELTTdll(self, T, z):
        T = ct.c_double(T)
        z = (len(z)*ct.c_double)(*z)
        Pmelt = ct.c_double()
        ierr = ct.c_long(0)
        herr = ct.create_string_buffer(255)

        self._MELTTdll(ct.byref(T), z, ct.byref(Pmelt), ct.byref(ierr), herr, 255)
        return Pmelt.value, ierr.value, str(herr.raw)

    def CRTPNTdll(self, z, Tc, pc, rhoc_mol_L):
        z = (len(z)*ct.c_double)(*z)
        Tc = ct.c_double(Tc)
        Pc = ct.c_double(pc)
        Dc = ct.c_double(rhoc_mol_L)
        ierr = ct.c_long(0)
        herr = ct.create_string_buffer(255)

        self._CRTPNTdll(z, ct.byref(Tc), ct.byref(Pc), ct.byref(Dc), ct.byref(ierr), herr, 255)
        return Tc.value, Pc.value, Dc.value, ierr, herr

    def CRITPdll(self, z, Tc, pc, rhoc_mol_L):
        z = (len(z)*ct.c_double)(*z)
        Tc = ct.c_double(Tc)
        Pc = ct.c_double(pc)
        Dc = ct.c_double(rhoc_mol_L)
        ierr = ct.c_long(0)
        herr = ct.create_string_buffer(255)

        self._CRITPdll(z, ct.byref(Tc), ct.byref(Pc), ct.byref(Dc), ct.byref(ierr), herr, 255)
        return Tc.value, Pc.value, Dc.value, ierr, herr

    def TDFLSHdll(self, T, rho_mol_L, z):
        p, Dl, Dv, q, e, h, s, Cv, Cp, w = ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double()
        T = ct.c_double(T)
        rho_mol_L = ct.c_double(rho_mol_L)
        z = (len(z)*ct.c_double)(*z)
        x = (len(z)*ct.c_double)()
        y = (len(z)*ct.c_double)()
        ierr = ct.c_long(0)
        herr = ct.create_string_buffer(255)

        self._TDFLSHdll(ct.byref(T), ct.byref(rho_mol_L), z, 
                        ct.byref(p), ct.byref(Dl), ct.byref(Dv), x, y, 
                        ct.byref(q), ct.byref(e), ct.byref(h), ct.byref(s), ct.byref(Cv), ct.byref(Cp), ct.byref(w), 
                        ct.byref(ierr), herr, 255)
        return p.value, Dl.value, Dv.value, list(x), list(y), q.value, e.value, h.value, s.value, Cv.value, Cp.value, w.value, ierr.value, str(herr.raw)

    def PEFLSHdll(self, p, u_J_mol, z):
        D, T, Dl, Dv, q, e, h, s, Cv, Cp, w = ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double()
        p = ct.c_double(p)
        u_J_mol = ct.c_double(u_J_mol)
        z = (len(z)*ct.c_double)(*z)
        x = (len(z)*ct.c_double)()
        y = (len(z)*ct.c_double)()
        ierr = ct.c_long(0)
        herr = ct.create_string_buffer(255)

        self._PEFLSHdll(ct.byref(p), ct.byref(u_J_mol), z, ct.byref(T), ct.byref(D), 
                        ct.byref(Dl), ct.byref(Dv), x, y, 
                        ct.byref(q), ct.byref(h), ct.byref(s), ct.byref(Cv), ct.byref(Cp), ct.byref(w), 
                        ct.byref(ierr), herr, 255)
        return T.value, D.value, Dl.value, Dv.value, list(x), list(y), q.value, h.value, s.value, Cv.value, Cp.value, w.value, ierr.value, str(herr.raw)

    def SATTdll(self, T, z, q):
        T = ct.c_double(T)
        z = (len(z)*ct.c_double)(*z)
        if (abs(q) < 1e-10):
            kph = ct.c_long(1)
        elif (abs(q-1) < 1e-10):
            kph = ct.c_long(2)
        else:
            raise ValueError()
        p, dl, dv = ct.c_double(),ct.c_double(),ct.c_double()
        x = (len(z)*ct.c_double)()
        y = (len(z)*ct.c_double)()
        ierr = ct.c_long(0)
        herr = ct.create_string_buffer(255)

        # SATTdll (T,z,kph,P,Dl,Dv,x,y,ierr,herr)
        self._SATTdll(ct.byref(T), z, ct.byref(kph), ct.byref(p), 
                      ct.byref(dl), ct.byref(dv), x, y, 
                      ct.byref(ierr), herr, 255)
        return p, dl.value, dv.value, list(x), list(y), ierr.value, str(herr.raw)

    def SATTPdll(self, T, p, z, kph, iguess, d):
        T = ct.c_double(T)
        p = ct.c_double(p)
        z = (len(z)*ct.c_double)(*z)
        kph = ct.c_long(kph)
        iguess = ct.c_long(iguess)
        d, dl, dv = ct.c_double(d), ct.c_double(), ct.c_double()
        x = (len(z)*ct.c_double)()
        y = (len(z)*ct.c_double)()
        q = ct.c_double()
        ierr = ct.c_long(0)
        herr = ct.create_string_buffer(255)

        # SATTPdll(t, p, z, kph, iguess, d, dl, dv, x, y, q, ierr, herr, herr_length)
        self._SATTPdll(ct.byref(T), ct.byref(p), z, ct.byref(kph), ct.byref(iguess), 
                       ct.byref(d), ct.byref(dl), ct.byref(dv), x, y, ct.byref(q),
                       ct.byref(ierr), herr, 255)

        return T.value, p.value, d.value, dl.value, dv.value, list(x), list(y), q.value, ierr.value, str(herr.raw)

    def TQFLSHdll(self, T, q, z, kq = 1):
        T = ct.c_double(T)
        q = ct.c_double(q)
        z = (len(z)*ct.c_double)(*z)
        kq = ct.c_long(kq)
        p, d, dl, dv = ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double()
        x = (len(z)*ct.c_double)()
        y = (len(z)*ct.c_double)()
        e, h, s, Cv, Cp, w  = ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double(),ct.c_double()
        ierr = ct.c_long(0)
        herr = ct.create_string_buffer(255)

        # TQFLSHdll(T,q,z,kq,P,D,Dl,Dv,x,y,e,h,s,Cv,Cp,w,i,herr)
        self._TQFLSHdll(ct.byref(T), ct.byref(q), z, ct.byref(kq),
                        ct.byref(p), ct.byref(d), ct.byref(dl), ct.byref(dv), x, y, ct.byref(e), ct.byref(h), ct.byref(s), ct.byref(Cv), ct.byref(Cp), ct.byref(w), 
                        ct.byref(ierr), herr, 255)
        return p.value, d.value, dl.value, dv.value, list(x), list(y), e.value, h.value, s.value, Cv.value, Cp.value, w.value, ierr.value, str(herr.raw)

