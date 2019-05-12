# -*- coding: utf-8 -*-

def fs_volume_coefficient(reference_length,reference_area,reference_mac,fs_mac,fs_area):
    """Estimation of Volume Coefficient of The Flying Surface (Exposed)"""
    arm = abs(fs_mac - reference_mac)
    return (arm*fs_area)/(reference_length*reference_area)