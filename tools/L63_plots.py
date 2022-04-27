# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:10:17 2017
@author: jamezcua
"""
import numpy as np
import matplotlib.pyplot as plt


##############################################################################
def plotL63(t,xt,plot3d):
 plt.figure().suptitle('Truth')
 for i in range(3):
  plt.subplot(3,1,i+1)
  plt.plot(t,xt[:,i],'k')
  plt.ylabel('x['+str(i)+']')
  plt.xlabel('time')
  plt.grid(True)
  plt.subplots_adjust(hspace=0.3)

 if plot3d == True:
    fig = plt.figure()
    fig.suptitle('Truth')
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xt[:,0],xt[:,1],xt[:,2],'k')
    ax.set_xlabel('x[0]')
    ax.set_ylabel('x[1]')
    ax.set_zlabel('x[2]')
    ax.grid(True)


##############################################################################
def plotL63obs(t,xt,tobs,y,observed_vars):
 plt.figure().suptitle('Truth and Observations')
 for i in range(3):
  plt.subplot(3,1,i+1)
  plt.plot(t,xt[:,i],'k')
  if i in observed_vars:
   #plt.autoscale(False) # prevent scatter() from rescaling axes
   plt.scatter(tobs,y[:,observed_vars.index(i)],20,'r')
  plt.ylabel('x['+str(i)+']')
  plt.xlabel('time')
  plt.grid(True)
  plt.subplots_adjust(hspace=0.3)
        
        
#############################################################################        
def plotL63DA_kf(t,xt,tobs,y,observed_vars,Xb,xb,Xa,xa):
 plt.figure().suptitle('Truth, Observations, Background Ensemble and Analysis Ensemble')
 for i in range(3):
  plt.subplot(3,1,i+1)
  plt.plot(t,xt[:,i],'k')
  plt.plot(t,Xb[:,i,:],'--b')
  plt.plot(t,Xa[:,i,:],'--m')
  if i in observed_vars:
   #plt.autoscale(False) # prevent scatter() from rescaling axes
   plt.scatter(tobs,y[:,observed_vars.index(i)],20,'r')
  plt.ylabel('x['+str(i)+']')
  plt.xlabel('time')
  plt.grid(True)
  plt.subplots_adjust(hspace=0.3)
 del i
 
 plt.figure().suptitle('Truth, Observations, Background and Analysis Mean')
 for i in range(3):
  plt.subplot(3,1,i+1)
  plt.plot(t,xt[:,i],'k')
  if i in observed_vars:
   #plt.autoscale(False) # prevent scatter() from rescaling axes
   plt.scatter(tobs,y[:,observed_vars.index(i)],20,'r')
  plt.plot(t,xb[:,i],'b')
  plt.plot(t,xa[:,i],'m')
  plt.ylabel('x['+str(i)+']')
  plt.xlabel('time')
  plt.grid(True)
  plt.subplots_adjust(hspace=0.3)
 del i 


#############################################################################
def plotL63DA_var(t,xt,tobs,y,observed_vars,xb,xa):
 plt.figure().suptitle('Truth, Observations, Background, and Analysis')
 for i in range(3):
  plt.subplot(3,1,i+1)
  plt.plot(t,xt[:,i],'k')
  if i in observed_vars:
   #plt.autoscale(False) # prevent scatter() from rescaling axes
   plt.scatter(tobs,y[:,observed_vars.index(i)],20,'r')
  plt.plot(t,xb[:,i],'b')
  plt.plot(t,xa[:,i],'m')
  plt.ylabel('x['+str(i)+']')
  plt.xlabel('time')
  plt.grid(True)
 del i           
 plt.subplots_adjust(hspace=0.3)


#####################################################
def plotL63DA_pf(t,xt,tobs,y,observed_vars,xpf,x_m):
 plt.figure().suptitle('Truth, Observations and Ensemble')
 for i in range(3):
  plt.subplot(3,1,i+1)
  plt.plot(t,xpf[:,i,:],'--m')
  plt.plot(t,xt[:,i],'-k',linewidth=2.0)
  plt.plot(t,x_m[:,i],'-m',linewidth=2)
  if i in observed_vars:
   #plt.autoscale(False) # prevent scatter() from rescaling axes
   plt.scatter(tobs,y[:,observed_vars.index(i)],20,'r')
  plt.ylabel('x['+str(i)+']')
  plt.xlabel('time')
  plt.grid(True)
  plt.subplots_adjust(hspace=0.3)



#############################################################################
def plotpar(Nparam,tobs,paramt_time,Parama,parama):
 plt.figure().suptitle('True Parameters and Estimated Parameters')
 for i in range(Nparam):
  plt.subplot(Nparam,1,i+1)
  plt.plot(tobs,paramt_time[:,i],'k')
  plt.plot(tobs,Parama[:,i,:],'--m')
  plt.plot(tobs,parama[:,i],'-m',linewidth=2)
  plt.ylabel('parameter['+str(i)+']')
  plt.xlabel('time')
  plt.grid(True)
 del i 
 plt.subplots_adjust(hspace=0.3)
        

#############################################################################
def plotRH(M,tobs,xt,xpf,rank):
 nbins = M+1
 plt.figure().suptitle('Rank histogram')
 for i in range(3):
  plt.subplot(1,3,i+1)
  plt.hist(rank[:,i],bins=nbins)
  plt.xlabel('x['+str(i)+']')
  plt.axis('tight')
 plt.subplots_adjust(hspace=0.3)
        
        
        
