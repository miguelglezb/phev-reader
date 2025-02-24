#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import pandas as pd
import units
import warnings



class Evdf(pd.DataFrame):
    """
    A subclass of pandas.DataFrame made for phev-reader, which is designed to store and 
    manage physical quantities, units, and conversion values for columns.

    This class extends the functionality of pandas DataFrame by incorporating metadata attributes that define the physical 
    meaning of each column of ev files.

    Attributes:
    ----------
    phys_quantity : dict
        A dictionary mapping column keys to their corresponding physical quantities.
    units : dict
        A dictionary mapping column keys to their corresponding units.
    conv_value : dict
        A dictionary mapping column keys to their conversion values.

    Methods:
    --------
    assign_default_quants_units():
        Assigns default physical quantities, units, and conversion values 
        to each column in the DataFrame.

    column_units(column_key):
        Returns the unit associated with a given column key.

    column_physical_quantity(column_key):
        Returns the physical quantity associated with a given column key.

    column_conversion_value(column_key):
        Returns the conversion value associated with a given column key.

    edit_physical_quantity(column_key, new_quantity_name):
        Edits the physical quantity tag of a specified column.

    convert_units(column_key, new_units, new_conversion_val=0):
        Changes the unit of a given column and updates the conversion value.
        If the unit is not in the predefined list, a custom conversion 
        factor must be provided.

    Notes:
    ------
    - This class inherits from pandas.DataFrame and retains all its functionalities.
    - The physical quantities, units, and conversion values are stored in the 
      `.attrs` dictionary of the DataFrame.
    - Conversion values are expected to be consistent with the predefined unit dictionary.
    """


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def _constructor(self):
        return Evdf

    def assign_default_quants_units(self):
        """Assigns default physical quantities, units, and conversion values to Evdf attributes."""
        quants_atr, units_atr, conv_value_atr = {}, {}, {}
        for column_key in self.keys():
            default_qu = units.phys_quants_units_default(column_key)
            quants_atr[column_key], units_atr[column_key], conv_value_atr[column_key] = default_qu

        self.attrs.update(
            {
                "phys_quantity": quants_atr,
                "units": units_atr,
                "conv_value": conv_value_atr,
            }
        )

    def column_units(self, column_key):
        """Returns the unit associated with a given column key."""
        return self.attrs["units"].get(column_key, None)

    def column_physical_quantity(self, column_key):
        """Returns the physical quantity associated with a given column key."""
        return self.attrs["phys_quantity"].get(column_key, None)

    def column_conversion_value(self, column_key):
        """Returns the conversion value associated with a given column key."""
        return self.attrs["conv_value"].get(column_key, None)

    def edit_physical_quantity(self, column_key, new_quantity_name):
        """It allow to edit the tag of physical quantity in a given column of the Ev DataFrame."""
        self.attrs["phys_quantity"].update({column_key: new_quantity_name})

    def convert_units(self, column_key, new_units, new_conversion_val=0): 
        """It allow to edit the tag of physical units in a given column of the Ev DataFrame."""
        phys_quants = self.column_physical_quantity(column_key)

        units_dict = units.phys_quantities_dict
        quants_and_unit_stored = (phys_quants in units_dict.keys()) and (new_units in units_dict[phys_quants])                                    


        if quants_and_unit_stored:
            self.attrs["units"].update({column_key: new_units})
            new_conversion_val = units.merged_units_dict[new_units] 
            self[column_key] = self[column_key] / self.column_conversion_value(column_key)
            self.attrs["conv_value"].update({column_key: new_conversion_val})
            self[column_key] = self[column_key] * new_conversion_val 
            print(f"Units changed in column {column_key} to {new_units}")
            return None
        elif phys_quants in units_dict.keys() and new_conversion_val > 0:
            self.attrs["units"].update({column_key: new_units})
            self[column_key] = self[column_key] / self.column_conversion_value(column_key)
            self[column_key] = self[column_key] * new_conversion_val 
            warnings.warn(f"Warning: '{new_units}' not found in unit list. Changes are made to new unit by user.", stacklevel=2)
            print(f"Units changed in column {column_key} to {new_units}")
            return None
        elif new_conversion_val == 0:
            raise ValueError("Invalid conversion value")
            return None


def evreader(filename, pheaders=True):
    """
    Reads an .ev file and converts its columns and rows into an Evdf (extended pandas DataFrame) object.

    Parameters
    ----------
    filename : str
        Path to the .ev file. The file must remain unchanged from the moment it was created by Phantom.

    pheaders : bool, optional, default=True
        If True, prints the column names after removing the brackets characteristic of the .ev file.

    Returns
    -------
    evdf : Evdf
        A DataFrame-like object containing the parsed data, with assigned physical quantities and units.
    """

    f = open(filename, "r")
    raw_data = f.read().split("\n")
    f.close()
    Row1 = raw_data[0]
    ncols = len(Row1.split("]")) - 1
    (
        headers,
        columns,
    ) = (
        [],
        [],
    )
    for i in Row1.split("]")[:-1]:
        columns.append([])
        headers.append(
            i.strip("#").strip().strip("[").strip().lstrip("1234567890").strip()
        )

    if pheaders == True:
        print(headers)

    for i in raw_data[1:]:
        if i.strip() == "":
            continue
        S = i
        for j in range(ncols):
            S = S.lstrip()
            if j < ncols - 1:
                try:
                    columns[j].append(float(S[: S.find(" ")]))
                except:
                    columns[j].append(S[: S.find(" ")])
            else:
                try:
                    columns[j].append(float(S))
                except:
                    columns[j].append(S)
            S = S[S.find(" ") :]

    formatted_columns = []
    for col in enumerate(columns):
        formatted_columns.append(np.array(col[1]))

    Data = {}

    for h, c in zip(headers, formatted_columns):
        Data.update({h: c})
    Data = Evdf(Data)
    Data.assign_default_quants_units()
    return Data


class constants:
    mass = 1.989e33
    time = 1.594e3
    dist = 6.96e10
    vel = dist / time
    dens = mass / dist**3
    spangmom = dist**2 / time
    spener = (dist / time) ** 2
    ener = mass * spener
    angmom = mass * spangmom
    pressure = ener / dist**3
    yr = time / (24 * 3600 * 365)
    day = time / (24 * 3600)

    def __init__(
        self,
        mass=mass,
        time=time,
        dist=dist,
        yr=yr,
        day=day,
        spangmom=spangmom,
        ener=ener,
        spener=spener,
        vel=vel,
        angmom=angmom,
        dens=dens,
        pressure=pressure,
    ):
        """Phantom units in cgs"""
        self.G = G
        self.mass = mass
        self.time = time
        self.dist = dist
        self.vel = vel
        self.dens = dens
        self.spangmom = spangmom
        self.spener = spener
        self.angmom = angmom
        self.ener = ener
        self.pressure = pressure
        self.yr = yr
        self.day = day
