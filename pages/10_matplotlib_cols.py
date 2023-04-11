"""Matplotlib colorbar."""
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')

st.markdown("----", unsafe_allow_html=True)
st.markdown("before cols", unsafe_allow_html=True)

col1, col2 = st.columns(2)
_r2_value_ = 0.5

st.markdown("----", unsafe_allow_html=True)
st.markdown("after cols", unsafe_allow_html=True)

# import pylab as pl
# import numpy as np

# a = np.array([[0,1]])
# pl.figure(figsize=(9, 1.5))
# img = pl.imshow(a, cmap="Blues")
# pl.gca().set_visible(False)
# cax = pl.axes([0.1, 0.2, 0.8, 0.6])
# pl.colorbar(orientation="horizontal", cax=cax)  
# # pl.savefig("colorbar.pdf")

cmap_spectrum = "RdYlGn"

fig = plt.figure()
# ax = fig.add_axes([0.05, 0.80, 0.9, 0.1])
ax = fig.add_axes([0, 0.80, 0.9, 0.1])
cb = mpl.colorbar.ColorbarBase(ax, orientation="horizontal", 
                            cmap=cmap_spectrum)
with col2:
    st.markdown("Legend", unsafe_allow_html=True)

    
    # plt.savefig('just_colorbar.png', bbox_inches='tight')
    st.pyplot(fig)
fig.clf()

def get_hexcode_of_value(_r2_value_, cmap_spectrum="RdYlGn"):
    # Green gets too dark to read for R2~1.0, so use hexcode of 0.95.
    if _r2_value_ >= 0.95:
        _r2_value_ = 0.95
    cmap = mpl.colormaps[cmap_spectrum]
    rgba = cmap(_r2_value_)
    R, G, B, A = round(rgba[0]*100), round(rgba[1]*100), round(rgba[2]*100), rgba[3]
    hex_code_string = "#{:02x}{:02x}{:02x}".format(*(R,G,B,A))
    print(f"\nhex_code_string for R2={_r2_value_}: {hex_code_string}")
    return hex_code_string

_r2_color_ = get_hexcode_of_value(_r2_value_)
r2_superscript = r"$R^{2}$"
_r2_text_ = f"<p style='background-color:{_r2_color_};'>$R^2$ = {_r2_value_}</p>"

with col1:
    st.markdown("Metrics", unsafe_allow_html=True)
    st.markdown(r"$R^{2}$"+str(_r2_value_), unsafe_allow_html=True)

    st.markdown(_r2_text_, unsafe_allow_html=True)

# # cmap = mpl.cm.get_cmap(cmap_spectrum)
# cmap = mpl.colormaps[cmap_spectrum]
# rgba = cmap(0.5)
# print(rgba)



# you can have an expander under a tab but not a tab under an expander,
# unless you define the cols/tabs under the expander

# with st.expander("COLUMNS EXPANDER"):
#    col1, col2, col3 = st.columns(3)
#    col1.markdown("foo c1")
