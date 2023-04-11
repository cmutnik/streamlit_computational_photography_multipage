"""Matplotlib colorbar."""
#%%
# import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')

_r2_value_ = 0.5

cmap_spectrum = "RdYlGn"

fig = plt.figure()
ax = fig.add_axes([0, 0.80, 0.9, 0.1])
cb = mpl.colorbar.ColorbarBase(ax, orientation="horizontal", 
                            cmap=cmap_spectrum)
#%%
# cmap = mpl.cm.get_cmap(cmap_spectrum)
cmap = mpl.colormaps[cmap_spectrum]
rgba = cmap(1)
print(rgba)
#%%
# #colormap possible values = viridis, jet, spectral
# rgba_color = cm.jet(norm(400),bytes=True)
# color_rgba = (0, 0, 0, 1)
# color_rgba = (00,42,22, 1) # #002a16
color_rgba = (655, 7, 149, 1) # #28f0795 # not #28f079
hex_code_string = "#{:02x}{:02x}{:02x}".format(*color_rgba)
print(f"\nhex_code_string: {hex_code_string}")

#%%
# dir(cb)
#%%


import matplotlib.pyplot as plt
import numpy as np

cmap = plt.cm.RdYlGn

cm = plt.pcolormesh(np.random.randn(10, 10), cmap=cmap)


value = 1
print(f"cmap(cm.norm(value)): {cmap(cm.norm(value))}")
print(f"cmap(value): {cmap(value)}")
print(f"cm.to_rgba(1): {cm.to_rgba(1)}")
print(f"dir(cmap): {dir(cmap)}")

import matplotlib as mpl

# cmap = mpl.cm.get_cmap('Spectral')
cmap1 = mpl.colormaps.get_cmap("RdYlGn")
rgba1 = cmap1(value)
print(f"rgba: {rgba1}")

cmap2 = mpl.colormaps["RdYlGn"]
rgba2 = cmap2(value)
print(f"rgba2: {rgba2}")

print(f"dir(cm.norm): {dir(cm.norm)}")
print(f"dir(cmap1): {dir(cmap1)}")

# print(f"cmap(cm.norm(value)): {cmap(cm.norm(value, vmax=1, vmin=0))}")
import matplotlib

norm = matplotlib.colors.Normalize(vmin=0, vmax=1)
print(f"norm(0.5): {norm(0.5)}")
print(f"dir(norm): {dir(norm)}")
# cmap = matplotlib.cm.get_cmap('Spectral')
# print(norm.process_value(0))

_x_ = 0.99
rgb_val_of_x_ = mpl.colormaps["RdYlGn"](_x_)#[np.newaxis, :, :3]
print(f"\nrgb_val_of_x_: {rgb_val_of_x_}")

# color_rgba = (12, 28, 200, 28) # R, G, B, Alpha
color_rgba = (65, 0, 15, 1) # _x_ = 0.0001 # #41000f
# color_rgba = (0, 32, 22, 1) # _x_ = 0.99 # #002016
color_rgba = (00, 41, 22, 1) # _x_ = 0.99999 # #002916
hex_code_string = "#{:02x}{:02x}{:02x}".format(*color_rgba)
print(f"\nhex_code_string: {hex_code_string}")

def on_color_fg_error_chosen(self, user_data):
    print("You chose the color: " + self.button_err_bg.get_rgba().to_string())
    color_rgba = self.button.get_rgba()
    color_hex = '#{:02x}{:02x}{:02x}'.format(*color_rgba)
    print(color_hex)



# %%
# plt.colorbar(ticks=range(6), label='digit value')
# plt.clim(-0.5, 5.5)

# %%
