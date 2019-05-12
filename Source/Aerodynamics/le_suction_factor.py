# -*- coding: utf-8 -*-

import numpy as np

def le_suction_factor(cl,design_cl):
    dcl_0x = np.array([
        0.034456424	,
        0.059020683	,
        0.09911614	,
        0.1729079	,
        0.24945731	,
        0.3041011	,
        0.37572917	,
        0.45277354	,
        0.58096874	,
        0.69899946	,
        0.81602263	,
        0.9740817	,
        1.0255542])
    dcl_0y = np.array([ 
         0.93096286 ,
         0.89291465 ,
         0.8317541  ,
         0.72297704 ,
         0.6195177  ,
         0.5540566  ,
         0.4721678  ,
         0.3955467  ,
         0.28037775 ,
         0.19090497 ,
         0.11890206 ,
         0.0367313  ,
         0.01562829])
    dcl_01x = np.array([
        0.043853633 ,
        0.076450415 ,
        0.11517412  ,
        0.15881917  ,
        0.20834364  ,
        0.2837122   ,
        0.38229096  ,
        0.49433622  ,
        0.5765494   ,
        0.6694467   ,
        0.7730529   ,
        0.84133637  ,
        0.9373873   ,
        1.0427682])
    dcl_01y = np.array([
        0.86366737  ,
        0.9006413   ,
        0.9093102   ,
        0.8964086   ,
        0.84178275  ,
        0.7463999   ,
        0.6116518   ,
        0.48604733  ,
        0.40127483  ,
        0.3189863   ,
        0.24052364  ,
        0.1935995   ,
        0.13809927  ,
        0.083766066])
    dcl_03x = np.array([
        0.09180485  ,
        0.11862118  ,
        0.15486653  ,
        0.20568499  ,
        0.25339934  ,
        0.29232103  ,
        0.33215132  ,
        0.38706735  ,
        0.45054623  ,
        0.53073716  ,
        0.6254516   ,
        0.721842    ,
        0.8489058   ,
        0.950076    ,
        1.0289694])
    dcl_03y = np.array([
        0.5795244   ,
        0.66359025  ,
        0.7541908   ,
        0.8418327   ,
        0.9053702   ,
        0.92477435  ,
        0.92134106  ,
        0.870641    ,
        0.7795087   ,
        0.65718764  ,
        0.5292241   ,
        0.42002234  ,
        0.31561366  ,
        0.24927819  ,
        0.20081228])
    dcl_04x = np.array([
        0.101170234 ,
        0.13933887  ,
        0.21559484  ,
        0.30041364  ,
        0.3679689   ,
        0.4201591   ,
        0.47970656  ,
        0.5465618   ,
        0.6321443   ,
        0.70837194  ,
        0.7849708   ,
        0.8748135   ,
        0.95331097  ,
        1.0321301])
    dcl_04y = np.array([
        0.4383987    ,
        0.5611802    ,
        0.7302291    ,
        0.8588458    ,
        0.9166408    ,
        0.93445325   ,
        0.918568     ,
        0.86630124   ,
        0.7479059    ,
        0.6270017    ,
        0.52622616   ,
        0.422517     ,
        0.35258052   ,
        0.30008885])
    dcl_05x = np.array([
        0.100611635  ,
        0.16003183   ,
        0.22580166   ,
        0.28651935   ,
        0.3521089    ,
        0.42094398   ,
        0.49332154   ,
        0.55030936   ,
        0.60547286   ,
        0.657656     ,
        0.7811455    ,
        0.83445996   ,
        0.91403925   ,
        0.9848577    ,
        1.0531412])
    dcl_05y = np.array([
        0.26390004  ,
        0.45742816  ,
        0.63472843  ,
        0.7544014   ,
        0.84981996  ,
        0.9049062   ,
        0.93576306  ,
        0.9252954   ,
        0.8880145   ,
        0.8333387   ,
        0.67932916  ,
        0.6138931   ,
        0.53051245  ,
        0.4768288   ,
        0.42990467])
    dcl_06x = np.array([
        0.092324555  ,
        0.14004596   ,
        0.20694715   ,
        0.285936     ,
        0.3687891    ,
        0.41803077   ,
        0.46293795   ,
        0.53696656   ,
        0.6064133    ,
        0.6924483    ,
        0.80663955   ,
        1.0465158])
    dcl_06y = np.array([
        0.10297041   ,
        0.23899613   ,
        0.40553612   ,
        0.57856077   ,
        0.744801     ,
        0.81904876   ,
        0.8745847    ,
        0.9228614    ,
        0.9390072    ,
        0.9172546    ,
        0.8359083    ,
        0.64749444])
    dcl_08x = np.array([
        0.10996995 ,
        0.19120382 ,
        0.28550822 ,
        0.37916917 ,
        0.47046137 ,
        0.527382   ,
        0.60414356 ,
        0.68986386 ,
        0.7777232  ,
        0.8957115  ,
        1.0026197])
    dcl_08y = np.array([
        0.050286047 ,
        0.27293655  ,
        0.48326     ,
        0.65869373  ,
        0.77779204  ,
        0.83578694  ,
        0.88803947  ,
        0.92133033  ,
        0.92639107  ,
        0.9067228   ,
        0.8630999])
    dcl_list = np.array([0,0.1,0.3,0.4,0.5,0.6,0.8])
    if design_cl > np.amax(dcl_list) or design_cl < np.amin(dcl_list): 
        S =0.9
    else:
        dcl_x_list = [dcl_0x,dcl_01x,dcl_03x,dcl_04x,dcl_05x,dcl_06x,dcl_08x]
        dcl_y_list = [dcl_0y,dcl_01y,dcl_03y,dcl_04y,dcl_05y,dcl_06y,dcl_08y]
        dcl_l = max(dcl_list[design_cl >= dcl_list])
        dcl_u = min(dcl_list[design_cl <= dcl_list])
        dcl_li = np.where(dcl_list == dcl_l)[0][0]
        dcl_ui = np.where(dcl_list == dcl_u)[0][0]
        S_l = np.interp(cl,dcl_x_list[dcl_li],dcl_y_list[dcl_li])
        S_u = np.interp(cl,dcl_x_list[dcl_ui],dcl_y_list[dcl_ui])
        S = np.interp(cl,[dcl_l,dcl_u],[S_l,S_u])
    return S
    