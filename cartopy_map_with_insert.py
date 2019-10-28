#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:57:59 2019

@author: emmaworthington

Demo code for creating a small map using cartopy, using
GSHHS coastlines and a zoomed insert.

You may need to change the projection, depending on the latitude
you are working with.
"""


import cartopy.mpl.geoaxes as geoax
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# Set projection
ccrs.PlateCarree()

# Set extent of map - [x0, x1, y0, y1]
extents = [-77.5, -75, 24.3, 27]

# Get coastlines from GSHHG dataset
gshhs = cfeature.GSHHSFeature()

# Set latitudes and longitudes
wb2 = dict(lon=-76.741, lat=26.5153)

# Plot WB2 and casts nearest
fig, ax = plt.subplots(figsize=(20, 40), 
                       subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent(extents)
ax.add_feature(gshhs, facecolor=cfeature.COLORS['land'])

ax.plot(wb2['lon'], wb2['lat'], marker='o', markersize=10, color='r', 
        label='WB2', alpha=0.5)

# Add island names
ax.text(-77.15, 26.1, 'Great Abaco', fontsize=14)
ax.text(-75.71, 24.4, 'Cat Island', fontsize=14)
ax.text(-77.35, 24.95, 'New Providence', fontsize=14)
ax.text(-76.35, 25, 'Eleuthera', fontsize=14)

# Style gridlines and labels
gl = ax.gridlines(draw_labels=True, alpha=0.5)
gl.xlabel_style = dict(fontsize=14)
gl.ylabel_style = dict(fontsize=14)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
gl.xformatter=LONGITUDE_FORMATTER
gl.yformatter=LATITUDE_FORMATTER

# Add inset plot
axins = zoomed_inset_axes(ax, 2.5, loc=1, axes_class=geoax.GeoAxes,
                          borderpad=5,
                          axes_kwargs=dict(map_projection=ccrs.PlateCarree()))
axins.add_feature(gshhs, facecolor=cfeature.COLORS['land'])
axins.set_xlim(-77.0, -76.6)
axins.set_ylim(26.4, 26.7)

# Draw gridlines and labels for inset
glins = axins.gridlines(draw_labels=True, alpha=0.6)
glins.xlabel_style = dict(fontsize=8)
glins.ylabel_style = dict(fontsize=8)
glins.xformatter=LONGITUDE_FORMATTER
glins.yformatter=LATITUDE_FORMATTER

# Plot inset
axins.plot(wb2['lon'], wb2['lat'], marker='o', markersize=10,
           color='r', label='WB2', alpha=0.5)

# Add labels
axins.text(-76.73, 26.51, 'WB2', color='r', fontsize=12)

# Draw 'zoom' lines
mark_inset(ax, axins, loc1=2, loc2=3, fc="none", ec="0.5")

# Make sure inset rectangle lines are 'over' coastlines
ax.background_patch.set_visible(False)

# Add legend at bottom right
ax.legend(loc=5, fontsize=14)

