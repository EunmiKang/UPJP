rule BMP_GIF_RULE
{
    strings:
        $BMP = {42 4D ?? ?? ?? ?? 00 00 00 00}
        $GIF1 = {47 49 46 38 39 61}
        $GIF2 = {47 49 46 38 37 61}

    condition:
        $BMP or $GIF1 or $GIF2
}