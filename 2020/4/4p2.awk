function range(x, min, max) { split(x,c,":"); return (c[2] >= min && c[2] <= max); }
function oneof(x, array) { split(x,c,":"); for (j in array) if (c[2] == array[j]) return 1; return 0; }
BEGIN { nfields = 0; n = 0; split("amb:blu:brn:gry:grn:hzl:oth", ecls, ":"); }
{ for (i = 1; i <= NF; ++i) {
    if ($i ~ /^byr:[0-9]+$/ && range($i, 1920, 2002)) { nfields +=  1; }
    if ($i ~ /^iyr:[0-9]+$/ && range($i, 2010, 2020)) { nfields +=  2; }
    if ($i ~ /^eyr:[0-9]+/ && range($i, 2020, 2030)) { nfields +=  4; }
    if ($i ~ /^hgt:[0-9]+cm$/ && range(substr($i,1,length($i)-2), 150, 193)) { nfields +=  8; }
    if ($i ~ /^hgt:[0-9]+in$/ && range(substr($i,1,length($i)-2), 59, 76)) { nfields +=  8; }
    if ($i ~ /^hcl:#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$/) { nfields +=  16; }
    if ($i ~ /^ecl:/ && oneof($i,ecls)) { nfields +=  32; }
    if ($i ~ /^pid:[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$/) { nfields +=  64; }
  }
}
/^$/ { if (nfields == 127) ++n; nfields = 0; }
END { if (nfields == 127) ++n; print n; }
