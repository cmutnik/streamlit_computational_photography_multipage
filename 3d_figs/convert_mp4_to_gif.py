ffmpeg \
  -i point_anim.mp4 \
  -r 15 \
  -vf "scale=512:-1,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
  -ss 00:00:03 -to 00:00:06 \
  point_anim.gif
