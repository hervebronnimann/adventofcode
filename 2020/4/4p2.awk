BEGIN { nfields = 0; n = 0; }
/byr:[0-9]/ { nfields +=  1; }
/iyr:/ { nfields +=  2; }
/eyr:/ { nfields +=  4; }
/hgt:/ { nfields +=  8; }
/hcl:/ { nfields +=  16; }
/ecl:/ { nfields +=  32; }
/pid:/ { nfields +=  64; }
/^$/ { if (nfields == 127) ++n; nfields = 0; }
END { if (nfields == 127) ++n; print n; }
