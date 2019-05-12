# -*- coding: utf-8 -*-

def component_build_up(Cf_c,Swet_c,FF_c,Q_c,Sref):
    """Estimate the drag of the component"""
    return (Cf_c*Swet_c*FF_c*Q_c)/Sref