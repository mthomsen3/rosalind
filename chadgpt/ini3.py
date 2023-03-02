def slice_string(s, a, b, c, d):
    return s[a:b+1] + " " + s[c:d+1]

s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
a, b, c, d = 22, 27, 97, 102
print(slice_string(s, a, b, c, d))




s = "ksNytiUGf3DPiB51iuIYt1tnW5oJxW7CYiSsuCmduB3AQ8bfRIlDNebkB195DH9qFxrpfJ0YKNiGNZARFJsCDqoThymalluswZqCLuOpfPEbv0Jzsd8nRri9lbdfncjcQqvCQbjORztNNylwLcSW2KKCbb2LRoXDP10SvhD1mONhypoleucosec4L7H3nI."
a, b, c, d = 87, 95, 171, 180
print(slice_string(s, a, b, c, d))