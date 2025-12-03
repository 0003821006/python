#!/usr/bin/env python3
# -*- Coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import date
import os

# csvファイルからデータを取得する
# contourfは2次元データを要求する。gnuplot用のcsvファイルは改行で2次元データを表現しているが、loadtxtは改行のみの行はなかったことにされ、2次元データとしては取得できない。そこで、1次元データとして取得してから2次元データに変換する。
# 具体的には、時間データからオシロスコープのデータ数を計算し、reshapeを使って2次元化する。
filename = 'tiwlt.txt'
data = np.loadtxt(filename, delimiter=',', comments='#')
# waveletgMapで作成したmapデータはdataに[周波数の数x時間の数,3]の二次元配列として格納される。
# waveletgMapで作成したmapデータ(*wlt.txt)は、1列目が周波数, 2列目が時間, 3列目がwavelet変換した結果で、かつ改行のみの行は無視されるので、
# data[:,0]は*map.txtの1列目のデータで周波数の1次元配列
# data[:,1]は*map.txtの2列目のデータで時間の1次元配列
# data[:,2]は*map.txtの3列目のデータでwavelet変換した結果の1次元配列となる。
# これをcontourfで表示するため, y, x, zの2D配列(行が周波数、列が時間)に変換する
nx = np.unique(data[:,0]).size # 時間の重複を無くしてから個数を数えてnxとする。
x = data[:,0].reshape(int(data[:,0].size/nx),nx)*1e6 # 一次元配列をint(data[:,0].size/nx)行nx列の配列に変換する。行が周波数を、列が時間を表す。
y = data[:,1].reshape(int(data[:,1].size/nx),nx)*1e-6
z = data[:,2].reshape(int(data[:,2].size/nx),nx)*1.0e3 # $\mu$ s$^{1/2}$$\cdot$nmに換算

# default設定の変更
plt.rcParams['lines.linewidth'] = 1 # 線幅
plt.rcParams['font.size'] = 18
#plt.rcParams["font.family"] = "Times"

# levelsを設定する関数。contourfとcolorbarを一致させるにはlevelsを設定するのが良さそう。
def callevels (z):
    if np.amin(z) < 0 and np.amax(z) > 0: # 表示するデータに正と負の値が含まれる時
        zmax = max(-np.amin(z),np.amax(z))
        zmin = -max
        return np.linspace(zmin, zmax, num = 22) # 線形に等間隔な数列を生成する
    else:
        zmin = np.amin(z)
        zmax = np.amax(z)
#        zmin = 0.0
# 有効数字2桁でzmaxを設定する。
#        iorder =int(np.log10(np.amax(z)))
#        zmax = np.ceil(np.amax(z)*10**(2-iorder))*10**(iorder-2)
        return np.linspace(zmin, zmax, num = 21)
        
#levels = callevels(z)
fig = plt.figure(figsize=(10,7)) # figsizeを設定
ax = fig.add_subplot((111)) # figureで設定したエリア全域にaxを設定
# colorbarのmax, minを設定する時はlevelsを設定するのが良さそう。
# extend='both'とすると上下の範囲外でも色を塗る。maxだと上だけ範囲外でも塗る。defaultはneither
#cs = ax.contourf(x,y,z,cmap='jet',levels=levels,extend='max')
cs = ax.contourf(x,y,z,levels=20,cmap='jet') # 塗りつぶした等高線を描画する
ax.set_xlabel(r'Time $\it{t}$ ($\mu$s)') # x軸のラベル
ax.set_ylabel(r'Frequency $\it{f}$ (MHz)') # y軸のラベル
#ax.set_xlim(-0.5,4.5) # x軸の上限と下限
ax.grid(linestyle='dashed') # gridを破線で表示
# plot範囲を正方形にする。
ax.set_aspect((np.amax(x)-np.amin(x))/(np.amax(y)-np.amin(y)))
# colorbarのlabelの向きは従来の逆
cbar = fig.colorbar(cs,label='Absolute value of wavelet transformation\n' r'of $u_z$ ($\mu$ s$^{1/2}$$\cdot$V)')
# set_ylabelならrotationで向きを変えられるが、数字と重なる不具合を直せなかった。
#cbar.ax.set_ylabel('Absolute value of wavelet transformation of $u_z$ ($\mu$ s$^{1/2}$$\cdot$nm)',rotation=-90)
# cbarの長さを合わせるための設定
ax_pos = ax.get_position()
cbar_pos0 = cbar.ax.get_position()
cbar_pos1 = [cbar_pos0.x0, ax_pos.y0, cbar_pos0.x1 - cbar_pos0.x0, ax_pos.y1 - ax_pos.y0]
cbar.ax.set_position(cbar_pos1)
ax.set_title('Ti-6Al-4V '+filename+' '+str(date.today())+' '+os.path.join(os.path.basename(os.path.dirname(__file__)),os.path.basename(__file__)),loc='right',fontsize=12)
# 余白を消してファイルに出力
plt.savefig("result.png", bbox_inches='tight', pad_inches=0)
plt.show()
