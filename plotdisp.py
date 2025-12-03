#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
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

# メイン関数
def main():
    filename = 'q004r000.txt'
# csvファイルからデータを取得する
# data[:,0]に1列目(時刻)、data[:,1]に2列目(電圧)のデータが入る。
    data = np.loadtxt(filename, delimiter=',', comments='#')
    data2 = np.loadtxt('q004r002.txt', delimiter=',', comments='#')
    data3 = np.loadtxt('q004r004.txt', delimiter=',', comments='#')
    data4 = np.loadtxt('q004r006.txt', delimiter=',', comments='#')
    data5 = np.loadtxt('q004r008.txt', delimiter=',', comments='#')
    data6 = np.loadtxt('q004r010.txt', delimiter=',', comments='#')
##    data7 = np.loadtxt('y1868.txt', delimiter=',', comments='#')
#print(data)
##data2 = np.loadtxt('../200707/x001y001.txt', delimiter=',', comments='#')

# default設定の変更
    plt.rcParams['lines.linewidth'] = 1 # 線幅
    plt.rcParams['font.size'] = 18
#plt.rcParams["font.family"] = "Times"

# グラフの描き方には関数だけで押し通すやり方とオブジェクト表記を使うやり方があるが、細かい調整が可能なオブジェクト型を選択した。
#plt.figure(figsize=(7,7))
#plt.plot(data[:,0]*1e6,data[:,1]*25,linewidth=1)
#plt.plot(data2[:,0]*1e6,data2[:,1]*25+0.04,linewidth=1)
#plt.xlabel('Time $\it{t}$ ($\mu$s)')
#plt.ylabel('Displacement $\it{u_z}$ (nm)')
#plt.xlim(-0.5,4.5)
#plt.title('Displacement')
#plt.grid(linestyle='dashed')
#plt.show()

# オブジェクト表記を使うやり方
# figureの中にsubplotでグラフを描く数や場所を指定する。
    fig = plt.figure(figsize=(8,6)) # figsizeの設定
    ax = fig.add_subplot((111)) # figureで設定したエリア全域にaxを設定
    b = 10.0
    a = 0.0
#    a = np.average(data[0:int(np.size(data[:,0])*0.09),1])
    ax.plot(data[:,0]*1e6,(data[:,2]-a)*1e9,label='z')
    # ax.plot(data[:,0]*1e6,(data[:,5]-a)*1e9,label='z',ls='dashed')
#    vmin = min(data[:,1]-a)
#    vmax = max(data[:,1]-a)
#    a = np.average(data2[0:int(np.size(data2[:,0])*0.09),1])
    ax.plot(data2[:,0]*1e6,(data2[:,2]-a)*1e9+b,label='xy SH')
    # ax.plot(data2[:,0]*1e6,(data2[:,5]-a)*1e9+b,label='xy SH',ls='dashed')
#    a = np.average(data3[0:int(np.size(data3[:,0])*0.09),1])
    ax.plot(data3[:,0]*1e6,(data3[:,2]-a)*1e9+b*2,label='xy SV')
    # ax.plot(data3[:,0]*1e6,(data3[:,5]-a)*1e9+b*2,label='xy SV', ls='dashed')
##    a = np.average(data4[0:int(np.size(data4[:,0])*0.09),1])
    ax.plot(data4[:,0]*1e6,(data4[:,2]-a)*1e9+b*3,label='(0,0)')
##    a = np.average(data5[0:int(np.size(data5[:,0])*0.09),1])
    ax.plot(data5[:,0]*1e6,(data5[:,2]-a)*1e9+b*4,label='(0,0)')
##    a = np.average(data6[0:int(np.size(data6[:,0])*0.09),1])
    ax.plot(data6[:,0]*1e6,(data6[:,2]-a)*1e9+b*5,label='(0,0)')
##    a = np.average(data7[0:int(np.size(data7[:,0])*0.09),1])
##    ax.plot(data7[:,0]*1e6,data7[:,1]-a+b*6,label='(0,0)')
##ax.plot(data2[:,0]*1e6,data2[:,1]*25+0.04,label='(1,1)')
    ax.set_xlabel(r'Time $\it{t}$ ($\mu$s)')
    ax.set_ylabel(r'y-displacement $\it{u_y}$ (nm)')
#    ax.set_xlim(-0.2,1.8)
#     ax.set_ylim(vmin,vmax)
#    ax.set_ylim(-0.01,0.05)
    ax.grid(linestyle='dashed')
#     ax.set_title('S50C')
    ax.set_title(' '+filename+' '+str(date.today())+' '+os.path.join(os.path.basename(os.path.dirname(__file__)),os.path.basename(__file__)),loc='right',fontsize=12)
#     ax.legend()
##ax.text(1,-0.04,'(0,0)')
##ax.text(1,0.035,'(1,1)')
##ax.set_aspect((ax.get_xlim()[1]-ax.get_xlim()[0])/(ax.get_ylim()[1]-ax.get_ylim()[0])) # plot範囲を正方形にする。
    squarify(fig)
##    plt.savefig('result.svg', transparent=True, bbox_inches='tight') # 余白を消してファイルに出力
#     plt.savefig('result.eps', transparent=True, bbox_inches='tight') # 余白を消してファイルに出力
    plt.savefig('result.pdf', transparent=True, bbox_inches='tight') # 余白を消してファイルに出力
    plt.show()

if __name__ == '__main__':
    main()
