import matplotlib.pyplot as plt

def acoustic_simulation(Ma, Ra, Ca, U0, V0, W0, dt):
    t = 0
    
    U = U0
    V = V0
    W = W0
    
    R = [U]
    T = [t]

    while t < 20:
        W = (-Ra/Ma)*V - (Ca/Ma)*U
        U += dt*V
        R.append(U)
        V += dt*W
        t += dt
        T.append(t)

    plt.plot(T,R)
    plt.show()