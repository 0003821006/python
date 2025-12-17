#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

def squarify(fig):
    w, h = fig.get_size_inches()
    if w > h:
        t = fig.subplotpars.top
        b = fig.subplotpars.bottom
        axs = h*(t-b)
        l = (1.-axs/w)/2
        fig.subplots_adjust(left=l, right=1-l)
    else:
        t = fig.subplotpars.right
        b = fig.subplotpars.left
        axs = w*(t-b)
        l = (1.-axs/h)/2
        fig.subplots_adjust(bottom=l, top=1-l)

def sv(rho: double, c44: double, c66: double, theta: double) -> double:
    return np.sqrt((c66*np.cos(theta)*np.cos(theta)+c44*np.sin(theta)*np.sin(theta))/rho)

def v1(rho: double, c11: double, c33: double, c13: double, c44: double, theta: double) -> double:
    g1 = c11*np.cos(theta)*np.cos(theta)+c44*np.sin(theta)*np.sin(theta)
    g3 = c44*np.cos(theta)*np.cos(theta)+c33*np.sin(theta)*np.sin(theta)
    g13 = (c13+c44)*np.sin(2*theta)/2.0
    x = g1+g3+np.sqrt((g1-g3)*(g1-g3)+4.0*g13*g13)
    return np.sqrt(x/(2.0*rho))

def v2(rho: double, c11: double, c33: double, c13: double, c44: double, theta: double) -> double:
    g1 = c11*np.cos(theta)*np.cos(theta)+c44*np.sin(theta)*np.sin(theta)
    g3 = c44*np.cos(theta)*np.cos(theta)+c33*np.sin(theta)*np.sin(theta)
    g13 = (c13+c44)*np.sin(2*theta)/2.0
    x = g1+g3-np.sqrt((g1-g3)*(g1-g3)+4.0*g13*g13)
    return np.sqrt(x/(2.0*rho))

def main():
    # default設定の変更
    plt.rcParams['lines.linewidth'] = 1 # 線幅
    plt.rcParams['font.size'] = 18
    fig = plt.figure(figsize=(10,7)) # figsizeを設定
    ax = fig.add_subplot((111),projection='polar') # figureで設定したエリア全域にaxを設定

    rho = 8.1e3
    c11 = 261.0e9
    c66 = 60.0e9
    c33 = 223.0e9
    c44 = 81.7e9
    c13 = 141.0e9
    c13 = 70.0e9

    # for i in np.arange(5):
    #     theta = np.deg2rad(i*22.5)
    #     v_s = sv(rho, c44, c66, theta)
    #     v_p = v1(rho, c11, c33, c13, c44, theta)
    #     v_r = 0.0
    #     # 方程式の定義
    #     def equation(v_r):
    #         term1 = np.sqrt(1 - (v_r / v_s)**2)
    #         term2 = np.sqrt(1 - (v_r / v_p)**2)
    #         term3 = (2 - (v_r / v_s)**2)**2
    #         return 4 * term1 * term2 - term3
    #     try:
    #         # v_r の探索範囲（0.1 から v_s の少し下まで）
    #         result = root_scalar(equation, bracket=[v_s*0.1, v_s * 0.99], method='brentq')
    #         v_r = result.root if result.converged else np.nan
    #     except Exception:
    #         v_r= np.nan
    #     print(f'q = {np.rad2deg(theta):.1f}, sv = {v_s:.2f}, v1 = {v_p:.2f}, v2 = {v2(rho, c11, c33, c13, c44, theta):.2f}, vr={v_r:.2f}')
    # return

    theta = np.deg2rad(np.arange(361))
    rsv = sv(rho, c44, c66, theta)
    rv1 = v1(rho, c11, c33, c13, c44, theta)
    rv2 = v2(rho, c11, c33, c13, c44, theta)

    v_r = np.empty(len(theta))
    for i, (v_s, v_p) in enumerate(zip(rsv,rv1)):
        # 方程式の定義
        def equation(v_r):
            term1 = np.sqrt(1 - (v_r / v_s)**2)
            term2 = np.sqrt(1 - (v_r / v_p)**2)
            term3 = (2 - (v_r / v_s)**2)**2
            return 4 * term1 * term2 - term3
        try:
            # v_r の探索範囲（0.1 から v_s の少し下まで）
            result = root_scalar(equation, bracket=[v_s*0.1, v_s * 0.99], method='brentq')
            v_r[i] = result.root if result.converged else np.nan
        except Exception:
            v_r[i]= np.nan

#    ax.plot(theta, 1.0e6/rsv, label='SV')
#    ax.plot(theta, 1.0e6/rv2, label='QuasiSH')
#    ax.plot(theta, 1.0e6/rv1, label='Quasilongitudinal')
#    ax.plot(theta, 1.0e6/v_r, label='Rayleigh')
#    ax.set_rlim(0,500)
    ax.plot(theta, rsv, label='SV')
    ax.plot(theta, rv2, label='QuasiSH')
    ax.plot(theta, rv1, label='Quasilongitudinal')
    ax.plot(theta, v_r, label='Rayleigh')
    ax.set_rlim(0,6000)
    ax.set_theta_zero_location('E')
    ax.set_theta_direction(1)
    ax.set_rlabel_position(90+45+22.5)
    ax.legend(loc='lower right')
    
    data = np.loadtxt('velos70.txt', delimiter=',', comments='#')
    ax.scatter(np.deg2rad(data[:,0]),data[:,1])
    ax.scatter(np.deg2rad(data[:,0]),data[:,2])
    ax.scatter(np.deg2rad(data[:,0]),data[:,3])

    squarify(fig)
    # 余白を消してファイルに出力
    plt.savefig("result.pdf", transparent=True, bbox_inches='tight', pad_inches=0)
    plt.show()

if __name__ == '__main__':
    main()