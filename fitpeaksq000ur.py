#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from datetime import date
import os

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
        
def gaussian(x, a, x0, sigma, b):
    return a * np.exp(-(x - x0)*(x - x0) / (2 * sigma*sigma))-b # -bにしてあるのは、全てのパラメーターの範囲を正の値にするため。

# メイン関数
def main():
# csvファイルからデータを取得する
# data[:,0]に1列目(時刻)、data[:,1]に2列目(電圧)のデータが入る。
    filename = 'peaksq004uy.txt'
    data = np.loadtxt(filename, delimiter=',', comments='#')
#print(data)

# default設定の変更
    plt.rcParams['lines.linewidth'] = 1 # 線幅
    plt.rcParams['font.size'] = 18
#plt.rcParams["font.family"] = "Times"

# オブジェクト表記を使うやり方
# figureの中にsubplotでグラフを描く数や場所を指定する。
    fig = plt.figure(figsize=(7,6)) # figsizeの設定
    ax = fig.add_subplot((111)) # figureで設定したエリア全域にaxを設定
# ax.axvline(x=2.621275e-06*1e6,linestyle='dashed',color='tab:blue')
# ax.axvline(x=2.619117451891136,linestyle='dashed',color='tab:orange')
# ax.axvline(x=1.1495235861989304,linestyle='dashed',color='tab:green')
    data[:,0] = (data[:,0]+1.3e-3)*1e3 # mm
    data[:,1] *= 1e6 # us
    ax.scatter(data[:,0],data[:,1],label='$x=0$')

# gaussian fit
# ix1 = 656
# ix2 = 668
# x = data[ix1:ix2,0]*1e6
# y = (data[ix1:ix2,1]-a)*25
# ax.scatter(x,y,color='tab:green')
# pars, cov = curve_fit(f=gaussian, xdata=x, ydata=y, p0=[0.2, 1.3, 0.2,0.013], bounds=(0, np.inf)) # p0は初期値で、初期値を設定するときは関数のx以外の引数分必要, boundsは全てのパラメーターの範囲
# print(pars, cov)
# print(pars[1])
# x = np.arange(x[0],x[np.size(x)-1],(x[1]-x[0])/10)
# plt.plot(x, gaussian(x,pars[0],pars[1],pars[2],pars[3]), label='d=1',color='tab:green')

# poly fit
    x = data[:,0]
    y = data[:,1]
# ax.scatter(x,y,color='tab:orange')
    fit = np.polyfit(x, y,1)
# x = np.arange(-19.500,-16.900,0.100)
    plt.plot(x, np.poly1d(fit)(x), label='d=1')
    print(fit)
    print(1/fit[0])
#print(2*1e3/fit[0])
# poly fit
# x = data[0:np.size(x)-1,0]
# y = data[0:np.size(y)-1,1]
# ax.scatter(x,y)
# fit = np.polyfit(x, y,1)
# # x = np.arange(-19.500,-16.900,0.100)
# plt.plot(x, np.poly1d(fit)(x), label='d=1')
# print(fit)

    ax.set_xlabel(r'Position $\it{r}$ (mm)')
    ax.set_ylabel(r'Time $\it{t}$ ($\mu$s)')
    ax.set_xlim(1,3.1)
# ax.set_ylim(-0.01,0.01)
    ax.grid(linestyle='dashed')
# ax.legend()
    ax.set_title(filename+' '+str(date.today())+' '+os.path.join(os.path.basename(os.path.dirname(__file__)),os.path.basename(__file__)),loc='right',fontsize=12)
#ax.text(2.5,-0.02,'$y=0$ mm',color='tab:blue')
#ax.text(2.5,0.02,'$y=1$ mm',color='tab:orange')
    ax.text(2,0.05,f'$v={1e3/fit[0]:.3f}$ m/s')
#     ax.set_aspect((ax.get_xlim()[1]-ax.get_xlim()[0])/(ax.get_ylim()[1]-ax.get_ylim()[0])) # plot範囲を正方形にする。
    squarify(fig)
# plt.savefig('resultfitpeaks.svg', transparent=True, bbox_inches='tight') # 余白を消してファイルに出力
#     plt.savefig('resultfitpeaks2.eps', transparent=True, bbox_inches='tight') # 余白を消してファイルに出力
    plt.savefig('result.pdf', transparent=True, bbox_inches='tight') # 余白を消してファイルに出力
    plt.show()

if __name__ == '__main__':
    main()