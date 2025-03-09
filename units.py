"""This module contains all data realted to the physical quantities, units and conversion rate for the columns of a Evdf object."""

import numpy as np


# These are the Phantom units. Here are defined in cgs
ptu = np.float64(1.594e3)
pmu = np.float64(1.989e33)
pdu = np.float64(6.96e10)
pvu = pdu / ptu
pmomu = pmu * pvu
peneru = pmu * pvu**2
pdensu = pmu / pdu**3

# Time units
seconds = ptu
minutes = seconds / 60
hours = seconds / 3600
days = seconds / (3600 * 24)
years = seconds / (3600 * 24 * 365)

# Mass units
grams = pmu
kilograms = grams / 1000
tons = grams / 1e6
moon_mass = grams / 7.348e25
earth_mass = grams / 5.972e27
jupiter_mass = grams / 1.898e30
solar_mass = grams / 1.989e33

# Distance units
centimeters = pdu
meters = centimeters / 100
kilometers = meters / 1e3
solar_radius = centimeters / 6.96e10
au = centimeters / 1.496e13

# Speed units
cm_s = pvu
m_s = meters / seconds
km_s = kilometers / seconds
km_h = kilometers / hours
km_d = kilometers / days

# Density units
g_cm3 = pdensu
kg_m3 = kilograms / meters**3

# Linear momentum units
gcm_s = pmomu
gm_s = grams * m_s
kgm_s = kilograms * m_s

# Energy units
gcms2 = peneru
kgms2 = kilograms * m_s**2

# Angular momentum units
gcm2_s = gcm_s * centimeters
kgm2_s = kgm_s * meters


time_dict = {
    "Null": 1,
    "ph. time units": 1,
    "seconds": seconds,
    "s": seconds,
    "minutes": minutes,
    "min": minutes,
    "hours": hours,
    "hr": hours,
    "days": days,
    "d": days,
    "years": years,
    "yr": years,
}


mass_dict = {
    "Null": 1,
    "ph. mass units": 1,
    "grams": grams,
    "g": grams,
    "kilograms": kilograms,
    "kg": kilograms,
    "tons": tons,
    "moon_mass": moon_mass,
    "m_moon": moon_mass,
    "earth_mass": earth_mass,
    "m_earth": earth_mass,
    "jupiter_mass": jupiter_mass,
    "m_jupiter": jupiter_mass,
    "solar_mass": solar_mass,
    "m_sun": solar_mass,
}


distance_dict = {
    "Null": 1,
    "ph. distance units": 1,
    "centimeters": centimeters,
    "cm": centimeters,
    "meters": meters,
    "m": meters,
    "kilometers": kilometers,
    "km": kilometers,
    "solar_radius": solar_radius,
    "r_sun": solar_radius,
    "au": au,
}


velocity_dict = {
    "Null": 1,
    "ph. velocity units": 1,
    "cm/s": cm_s,
    "cgs": cm_s,
    "m/s": m_s,
    "mks": m_s,
    "km/s": km_s,
    "km/h": km_h,
    "km/d": km_d,
}


density_dict = {
    "Null": 1,
    "ph. density units": 1,
    "g/cm^3": g_cm3,
    "cgs": g_cm3,
    "kg/m^3": kg_m3,
    "mks": kg_m3,
}


momentum_dict = {
    "Null": 1,
    "ph. momentum units": 1,
    "g cm/s": gcm_s,
    "cgs": gcm_s,
    "g m/s": gm_s,
    "kg m/s": kgm_s,
    "mks": kgm_s,
}


energy_dict = {"Null": 1, "ph. energy units": 1, "erg": gcms2, "J": kgms2}


angmom_dict = {
    "Null": 1,
    "ph. angular momentum units": 1,
    "g cm^2/s": gcm2_s,
    "cgs": gcm2_s,
    "kg m^2/s": kgm2_s,
    "mks": kgm2_s,
}


phys_quantities_dict = {
    "time": time_dict.keys(),
    "mass": mass_dict.keys(),
    "distance": distance_dict.keys(),
    "velocity": velocity_dict.keys(),
    "density": density_dict.keys(),
    "momentum": momentum_dict.keys(),
    "energy": energy_dict.keys(),
    "angular momentum": angmom_dict.keys(),
}


merged_units_dict = {
    **time_dict,
    **mass_dict,
    **distance_dict,
    **velocity_dict,
    **density_dict,
    **momentum_dict,
    **energy_dict,
    **angmom_dict,
}


def phys_quants_units_default(column_key):
    '''
    This function reads the column name of Evdf object and writes the default values for
    physical quantity, unit and conversion rate corresponding for a given column name.
    
    Parameters
    ----------
    column_key : string
        Given column name of the Evdf.
    
    Returns
    -------
    quants_units : list
        A list containing three elements: The type of physical quantity ('time', 'mass', 'distance'),
        the unit for the column (ph. time units, ph. mass units, ph. distance units), and the conversion
        rate for that unit (default is 1).

    Notes
    -----
        This function assumes that the original ev file has not being edited since its creation via Phantom.
        This is the reason why all units are label as `ph. X units` and the conversion rate is always 1.
      
    '''
    time_default_quants_units = ["time", "ph. time units", time_dict["ph. time units"]]
    mass_default_quants_units = ["mass", "ph. mass units", mass_dict["ph. mass units"]]
    distance_default_quants_units = [
        "distance",
        "ph. distance units",
        distance_dict["ph. distance units"],
    ]
    velocity_default_quants_units = [
        "velocity",
        "ph. velocity units",
        velocity_dict["ph. velocity units"],
    ]
    density_default_quants_units = [
        "density",
        "ph. density units",
        density_dict["ph. density units"],
    ]
    energy_default_quants_units = [
        "energy",
        "ph. energy units",
        energy_dict["ph. energy units"],
    ]
    momentum_default_quants_units = [
        "momentum",
        "ph. momentum units",
        momentum_dict["ph. momentum units"],
    ]
    angmom_default_quants_units = [
        "angular momentum",
        "ph. angular momentum units",
        angmom_dict["ph. angular momentum units"],
    ]

    quant_dict = {
        "time": time_default_quants_units,
        "dt": time_default_quants_units,
        "mass": mass_default_quants_units,
        "macc": mass_default_quants_units,
        "x": distance_default_quants_units,
        "y": distance_default_quants_units,
        "z": distance_default_quants_units,
        "xcom": distance_default_quants_units,
        "ycom": distance_default_quants_units,
        "zcom": distance_default_quants_units,
        "vx": velocity_default_quants_units,
        "vy": velocity_default_quants_units,
        "vz": velocity_default_quants_units,
        "vrms": velocity_default_quants_units,
        "rho ave": density_default_quants_units,
        "rhomax": density_default_quants_units,
        "emag": energy_default_quants_units,
        "epot": energy_default_quants_units,
        "ekin": energy_default_quants_units,
        "erad": energy_default_quants_units,
        "etherm": energy_default_quants_units,
        "total energy": energy_default_quants_units,
        "totmom": momentum_default_quants_units,
        "totmomall": momentum_default_quants_units,
        "angmom": angmom_default_quants_units,
        "angall": angmom_default_quants_units,
    }

    if column_key in quant_dict.keys():
        return quant_dict[column_key]
    else:
        return ["Unknown quantity", "Unknown units", 1.0]
