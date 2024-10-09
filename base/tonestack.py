from scipy import signal

def toneResponse(t, m, l, C1, C2, C3, R1, R2, R3, R4):


  b1 = t * C1 * R1 + m * C3 * R3 + l * (C1 * R2 + C2 * R2) + (C1 * R3 + C2 * R3)

  b2 = (t * (C1 * C2 * R1 * R4 + C1 * C3 * R1 * R4) -
        m**2 * (C1 * C3 * R3**2 + C2 * C3 * R3**2) +
        m * (C1 * C3 * R1 * R3 + C1 * C3 * R3**2 + C2 * C3 * R3**2) +
        l * (C1 * C2 * R1 * R2 + C1 * C2 * R2 * R4 + C1 * C3 * R2 * R4) +
        l * m * (C1 * C3 * R2 * R3 + C2 * C3 * R2 * R3) +
        (C1 * C2 * R1 * R3 + C1 * C2 * R3 * R4 + C1 * C3 * R3 * R4))

  b3 = (l * m * (C1 * C2 * C3 * R1 * R2 * R3 + C1 * C2 * C3 * R2 * R3 * R4) -
        m**2 * (C1 * C2 * C3 * R1 * R3**2 + C1 * C2 * C3 * R3**2 * R4) +
        m * (C1 * C2 * C3 * R1 * R3**2 + C1 * C2 * C3 * R3**2 * R4) +
        t * C1 * C2 * C3 * R1 * R3 * R4 -
        t * m * C1 * C2 * C3 * R1 * R3 * R4 +
        t * l * C1 * C2 * C3 * R1 * R2 * R4)

  a0 =1

  a1 = (C1 * R1 + C1 * R3 + C2 * R3 + C2 * R4 + C3 * R4) + m * C3 * R3 + l * (C1 * R2 + C2 * R2)

  a2 = (m * (C1 * C3 * R1 * R3 - C2 * C3 * R3 * R4 + C1 * C3 * R3**2 + C2 * C3 * R3**2) +
        l * m * (C1 * C3 * R2 * R3 + C2 * C3 * R2 * R3) -
        m**2 * (C1 * C3 * R3**2 + C2 * C3 * R3**2) +
        l * (C1 * C2 * R2 * R4 + C1 * C2 * R1 * R2 + C1 * C3 * R2 * R4 + C2 * C3 * R2 * R4) +
        (C1 * C2 * R1 * R4 + C1 * C3 * R1 * R4 + C1 * C2 * R3 * R4 +
        C1 * C2 * R1 * R3 + C1 * C3 * R3 * R4 + C2 * C3 * R3 * R4))

  a3 = (l * m * (C1 * C2 * C3 * R1 * R2 * R3 + C1 * C2 * C3 * R2 * R3 * R4) -
        m**2 * (C1 * C2 * C3 * R1 * R3**2 + C1 * C2 * C3 * R3**2 * R4) +
        m * (C1 * C2 * C3 * R3**2 * R4 + C1 * C2 * C3 * R1 * R3**2 - C1 * C2 * C3 * R1 * R3 * R4) +
        l * C1 * C2 * C3 * R1 * R2 * R4 +
        C1 * C2 * C3 * R1 * R3 * R4)


  num = [b3, b2, b1, 0]
  den = [a3,a2,a1,a0]

  sys = signal.TransferFunction(num, den)
  w, mag, phase = signal.bode(sys,n=1000)

  return(w,mag,phase)
