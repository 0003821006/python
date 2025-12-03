#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

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

def main():
    # default設定の変更
    plt.rcParams['lines.linewidth'] = 1 # 線幅
    plt.rcParams['font.size'] = 18
    fig = plt.figure(figsize=(10,7)) # figsizeを設定
    ax = fig.add_subplot((111),projection='polar') # figureで設定したエリア全域にaxを設定
    for i in range(0,370,10):
        if i == 0:
            data1 = np.loadtxt('theta0.txt', delimiter=',', comments='#')
            ny = data1[:,0].size
            data2 = np.zeros(ny)
            data2 += 0.0
        elif i == 10:
            data1 = np.loadtxt('theta10.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(10.0)
        elif i == 20:
            data1 = np.loadtxt('theta20.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(20.0)
        elif i == 30:
            data1 = np.loadtxt('theta30.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(30.0)
        elif i == 40:
            data1 = np.loadtxt('theta40.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(40.0)
        elif i == 50:
            data1 = np.loadtxt('theta50.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(50.0)
        elif i == 60:
            data1 = np.loadtxt('theta60.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(60.0)
        elif i == 70:
            data1 = np.loadtxt('theta70.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(70.0)
        elif i == 80:
            data1 = np.loadtxt('theta80.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(80.0)
        elif i == 90:
            data1 = np.loadtxt('theta90.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(90.0)
        elif i == 100:
            data1 = np.loadtxt('theta100.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(100.0)
        elif i == 110:
            data1 = np.loadtxt('theta100.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(110.0)
        elif i == 120:
            data1 = np.loadtxt('theta120.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(120.0)
        elif i == 130:
            data1 = np.loadtxt('theta130.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(130.0)
        elif i == 140:
            data1 = np.loadtxt('theta140.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(140.0)
        elif i == 150:
            data1 = np.loadtxt('theta150.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(150.0)
        elif i == 160:
            data1 = np.loadtxt('theta160.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(160.0)
        elif i == 170:
            data1 = np.loadtxt('theta170.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(170.0)
        elif i == 180:
            data1 = np.loadtxt('theta180.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(180.0)
        elif i == 190:
            data1 = np.loadtxt('theta190.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(190.0)
        elif i == 200:
            data1 = np.loadtxt('theta200.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(200.0)
        elif i == 210:
            data1 = np.loadtxt('theta210.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(210.0)
        elif i == 220:
            data1 = np.loadtxt('theta220.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(220.0)
        elif i == 230:
            data1 = np.loadtxt('theta230.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(230.0)
        elif i == 240:
            data1 = np.loadtxt('theta240.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(240.0)
        elif i == 250:
            data1 = np.loadtxt('theta250.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(250.0)
        elif i == 260:
            data1 = np.loadtxt('theta260.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(260.0)
        elif i == 270:
            data1 = np.loadtxt('theta270.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(270.0)
        elif i == 280:
            data1 = np.loadtxt('theta280.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(280.0)
        elif i == 290:
            data1 = np.loadtxt('theta290.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(290.0)
        elif i == 300:
            data1 = np.loadtxt('theta300.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(300.0)
        elif i == 310:
            data1 = np.loadtxt('theta310.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(310.0)
        elif i == 320:
            data1 = np.loadtxt('theta320.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(320.0)
        elif i == 330:
            data1 = np.loadtxt('theta330.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(330.0)
        elif i == 340:
            data1 = np.loadtxt('theta340.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(340.0)
        elif i == 350:
            data1 = np.loadtxt('theta350.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(350.0)
        elif i == 360:
            data1 = np.loadtxt('theta0.txt', delimiter=',', comments='#')
            data2 = np.zeros(ny)
            data2 += np.radians(360.0)
        a = np.average(data1[0:int(np.size(data1)*0.09),1])
        data1[:,1] -= a
        data3 = np.vstack([data2,data1[:,0],data1[:,1]]) # 配列をtheta, time, zの順に横に結合
        if i ==0:
            data = np.copy(data3)
        else:
            data = np.hstack([data,data3]) # 配列を縦に結合 (継ぎ足していく)
    theta = data[0,:].reshape(data[0,:].size//ny,ny)
    r = data[1,:].reshape(data[1,:].size//ny,ny)*1e6
    z = data[2,:].reshape(data[2,:].size//ny,ny)
#     azimuths = np.radians(np.linspace(0, 350, 36))
#     print(np.linspace(0, 360, 37))
#     zeniths = np.arange(0, 70, 10)
#     r, theta = np.meshgrid(zeniths, azimuths)
#     valuesa = np.random.random((azimuths.size, zeniths.size))
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_rlim(0,0.6)
    cs = ax.contourf(theta, r, z,cmap='jet',levels=np.linspace(-0.5, 0.5, num = 21),extend='both')
    cbar = fig.colorbar(cs,label='Potential (V)')
    # cbarの長さを合わせるための設定
    ax_pos = ax.get_position()
    cbar_pos0 = cbar.ax.get_position()
    cbar_pos1 = [cbar_pos0.x0, ax_pos.y0, cbar_pos0.x1 - cbar_pos0.x0, ax_pos.y1 - ax_pos.y0]
    cbar.ax.set_position(cbar_pos1)
    squarify(fig)
    # 余白を消してファイルに出力
#     plt.savefig("polar.png", bbox_inches='tight', pad_inches=0)
    plt.show()

if __name__ == '__main__':
    main()