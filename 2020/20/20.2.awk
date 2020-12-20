function reverse(x) { y=""; for(j=length(x);j>0;--j) y=y substr(x,j,1); return y; } 
function ccw(n) { if (n<0) return -cw(-n); return n==1 ? 4 : n-1; }
function cw(n) { if (n<0) return -ccw(-n); return n==4 ? 1 : n+1; }

/^Tile/ { ++ntiles; current_id = $2; r = 0; }
/^[.#]+$/ {
  row[++r,current_id] = $0; LEN = length($0);
  if (r == 1) side[1,current_id] = $0;
}
/^$/ {
  # Keep tile borders clockwise, 1=top, 2=right, 3=bottom(reverse), 4=left(reverse)
  side[3,current_id] = reverse(row[r,current_id]);
  side[2,current_id] = ""; side[4,current_id] = "";
  for (i=1;i<=r;++i) {
    side[2,current_id] = side[2,current_id] substr(row[i,current_id],LEN,1);
    side[4,current_id] = side[4,current_id] substr(row[r-i+1,current_id],1,1);
  }
  # Insert tile borders into map from side to id
  for (i=1; i<=4; ++i) {
    x = side[i,current_id]; mapid[x,++mapn[x]] = current_id;
    print "Tile " current_id " side " i " " x " matching " reverse(x)
  }
}

function print_tile(id) {
print "TILE " id
  for (i=1; i<=LEN; ++i) print row[i,id]
print
}

function rotate_tile_cw(id) {
  print "Rotate cw " id
  for (i=1; i<=LEN; ++i) {
    newrow[i] = "";
    for (j=1; j<=LEN; ++j) {
      newrow[i] = newrow[i] substr(row[LEN-j+1,id],i,1);
    }
  }
  for (i=1; i<=LEN; ++i) {
    row[i,id] = newrow[i];
  }
  delete newrow;
  # Also rotate sides and maps
  temp = side[1,id];
  side[1,id] = side[4,id];
  side[4,id] = side[3,id];
  side[3,id] = side[2,id];
  side[2,id] = temp;
}

function remove_from_mapid(xx,id) {
  for (kk = 1; kk <= mapn[xx]; ++kk) {
    if (mapid[xx,kk] == id) {
      while (++kk <= mapn[xx]) mapid[xx,kk-1] = mapid[xx,kk];
      --mapn[xx];
      return;
    }
  }
  print "WTF NOT FOUND IN MAPID"
}

function flip_tile_horiz(id) {
  print "Flip horiz " id
  for (i=1; i<=LEN; ++i) {
    row[i,id] = reverse(row[i,id]);
  }
  # Also flid sides and maps
  xx = side[1,id]; rxx = reverse(xx); remove_from_mapid(xx,id);
  side[1,id] = rxx; mapid[rxx,++mapn[rxx]] = id;
  xx = side[3,id]; rxx = reverse(xx); remove_from_mapid(xx,id);
  side[3,id] = rxx; mapid[rxx,++mapn[rxx]] = id;
  temp = side[4,id];
  xx = side[2,id]; rxx = reverse(xx); remove_from_mapid(xx,id);
  side[4,id] = rxx; mapid[rxx,++mapn[rxx]] = id; 
  xx = temp; rxx = reverse(xx); remove_from_mapid(xx,id);
  side[2,id] = rxx; mapid[rxx,++mapn[rxx]] = id; 
}

function flip_tile_vert(id) {
  print "Flip vert " id
  for (i=1; i<LEN-i+1; ++i) {
    temp = row[i,id];
    row[i,id] = row[LEN-i+1,id];
    row[LEN-i+1,id] = temp;
  }
  # Also flid sides and maps
  xx = side[2,id]; rxx = reverse(xx); remove_from_mapid(xx,id);
  side[2,id] = rxx; mapid[rxx,++mapn[rxx]] = id;
  xx = side[4,id]; rxx = reverse(xx); remove_from_mapid(xx,id);
  side[4,id] = rxx; mapid[rxx,++mapn[rxx]] = id;
  temp = side[3,id];
  xx = side[1,id]; rxx = reverse(xx); remove_from_mapid(xx,id);
  side[3,id] = rxx; mapid[rxx,++mapn[rxx]] = id; 
  xx = temp; rxx = reverse(xx); remove_from_mapid(xx,id);
  side[1,id] = rxx; mapid[rxx,++mapn[rxx]] = id; 
}

function fill_image(r,c,id) {
  print "Filling image " r " " c " from " id
  for (p = 1; p <= LEN; ++p)
  for (q = 1; q <= LEN; ++q)
    full[r*LEN+p-LEN,c*LEN+q-LEN] = substr(row[p,id],q,1);
  # Assume that tile has already been rotated and flipped
  r = (r-1)*(LEN-2)+1; c = (c-1)*(LEN-2)+1; # forget about boundaries
  for (p = 2; p <= LEN-1; ++p)
  for (q = 2; q <= LEN-1; ++q)
    image[r+p-2,c+q-2] = substr(row[p,id],q,1);
}

function print_image() {
  print
  for (p = 1; p <= LLEN; ++p) {
    line[p] = "";
    for (q = 1; q <= LLEN; ++q)
      line[p] = line[p] image[p,q];
    print line[p] 
  }
  delete line;
}

function rotate_image_cw() {
  print "Rotate image cw "
  for (i=1; i<=LLEN; ++i)
  for (j=1; j<=LLEN; ++j) {
    newimage[i,j] = image[LLEN-j+1,i];
  }
  for (i=1; i<=LLEN; ++i)
  for (j=1; j<=LLEN; ++j) {
    image[i,j] = newimage[i,j];
  }
  delete newimage;
}

function flip_image_horiz() {
  print "Flip image horiz"
  for (i=1; i<=LLEN; ++i)
  for (j=1; j<LLEN-j+1; ++j) {
    temp = image[i,j]; image[i,j] = image[i,LLEN-j+1]; image[i,LLEN-j+1] = temp;
  }
}

function find_sea_monster() {
  res = 0;
  for (p = 1; p+SM_MAXY-1 <= LLEN; ++p)
  for (q = 1; q+SM_MAXX-1 <= LLEN; ++q) {
    found = 1;
    for (i in sm) {
      split(sm[i],sml,"");
      for (j in sml) {
        if (sml[j] == "#" && image[p+i-1,q+j-1] == ".") { found = 0; break; }
      }
    }
    if (found == 1) {
      for (i in sm) {
        split(sm[i],sml,"");
        for (j in sml) {
          if (sml[j] == "#") image[p+i-1,q+j-1] = "O";
        }
      }
      ++res;
    }
  }
  return res;
}

END {
  SIDE=sqrt(ntiles);
  print "Tiles " ntiles " borders " SIDE*4

  # Find border tiles, keep count by id, corners will have count==2, others count==1
  for (x in mapn) {
    rx = reverse(x);
    if (mapn[x] == 1 && !(rx in mapn)) {
      print "Found border " x " id " mapid[x,1];
      borderx[mapid[x,1],++bordern[mapid[x,1]]] = x;
    }
  }

  # Identify one corner, and stitch the image together
  for (id in bordern) {
    if (bordern[id] == 2) {
      x1 = borderx[id,1]; x4 = borderx[id,2];
      print "Found corner " id " both sides " x1 " and " x4
      while (side[4,id] != x1) rotate_tile_cw(id);
      if (side[1,id] == x4) { 
         x1 = borderx[2]; x4 = borderx[1]; # swap them to make x1 the top side
      } else if (side[3,id] == x4) { 
        rotate_tile_cw(id); # rotate one more time to make x1 the top side
      } else {
        print "WTF CORNER ABORT"; exit;
      }
      print "Found corner " id " top side " x1 " left side " x4

      # Fill image row by stitching right side to left side
      for (rr = 1; rr <= SIDE; ++rr) {
        first_id = id;
        # Invariant: current square on the row is id
        fill_image(rr,1,id);

        for (cc = 2; cc <= SIDE; ++cc) {
          # Find right neighbor id (rnid)
          x2 = side[2,id]; rx2 = reverse(x2);
          if (mapn[x2] == 2) { # neighbor tile is flipped and perhaps rotated
            if (mapid[x2,1]==id) id = mapid[x2,2];
            else if (mapid[x2,2]==id) id = mapid[x2,1];
            else { print "WTF RN NOT FOUND ABORT"; exit; } 
            for (i=1; i<=4; ++i) if (side[i,id] == x2) break;
            if (i == 5) { print "WTF RN SIDE NOT FOUND ABORT"; exit; }
            if (i == 1 || i == 3) flip_tile_horiz(id); else flip_tile_vert(id);
          } else if (rx2 in mapn && mapn[rx2] == 1) {
            id = mapid[rx2,1];
          } else {
            print "WTF RN MULTIPLE MATCHES ABORT"; exit;
          }
          # Rotate neighbor to bring left side to match rx2
          for (i=1; i<=4; ++i) if (side[i,id] == rx2) break;
          if (side[i,id] != rx2) { print "WTF RN SIDE NOT FOUND ABORT"; exit; }
          while (side[4,id] != rx2) rotate_tile_cw(id);
          #
          print "Found next tile " id " top side " side[1,id] " left side " side[4,id]
          fill_image(rr,cc,id);
        }
       
        # Set up next loop by starting at bottom neighbor
        if (rr < SIDE) {
          id = first_id;
          x3 = side[3,id]; rx3 = reverse(x3);
          if (mapn[x3] == 2) { # second tile is flipped and perhaps rotated
            if (mapid[x3,1]==id) id = mapid[x3,2];
            else if (mapid[x3,2]==id) id = mapid[x3,1];
            else { print "WTF BN NOT FOUND ABORT"; exit; } 
            for (i=1; i<=4; ++i) if (side[i,id] == x3) break;
            if (i == 5) { print "WTF RN SIDE NOT FOUND ABORT"; exit; }
            if (i == 1 || i == 3) flip_tile_horiz(id); else flip_tile_vert(id);
          } else if (rx3 in mapn) {
            id = mapid[rx3,1];
          } else {
            print "WTF BN MULTIPLE MATCHES ABORT"; exit;
          }
          # Rotate neighbor to bring top side to match rx3
          for (i=1; i<=4; ++i) if (side[i,id] == rx3) break;
          if (side[i,id] != rx3) { print "WTF BN SIDE NOT FOUND ABORT"; exit; }
          while (side[1,id] != rx3) rotate_tile_cw(id);
          print "Found next row tile " id " top side " side[1,id] " left side " side[4,id]
        }
      }
      break; ## DONE filling image
    }
  }

  print "FULL IMAGE " 
  print
  for (p = 1; p <= LEN*SIDE; ++p) {
    line[p] = "";
    for (q = 1; q <= LEN*SIDE; ++q) {
      line[p] = line[p] full[p,q];
      if (q % LEN == 0) line[p] = line[p] " "
    }
    print line[p] 
    if (p % LEN == 0) print
  }
  delete line;

  # Print the reconstructed image
  LLEN = (LEN-2)*SIDE;
  print "IMAGE " LLEN " x " LLEN
  print_image();

  # Find the sea monsters
  sm[1] = "                  # "
  sm[2] = "#    ##    ##    ###"
  sm[3] = " #  #  #  #  #  #   "
  SM_MAXX = length(sm[1]); SM_MAXY = 3;

  if (find_sea_monster() == 0) {
    rotate_image_cw();
    if (find_sea_monster() == 0) {
      rotate_image_cw();
      if (find_sea_monster() == 0) {
        rotate_image_cw();
        if (find_sea_monster() == 0) {
          flip_image_horiz();
          if (find_sea_monster() == 0) {
            rotate_image_cw();
            if (find_sea_monster() == 0) {
              rotate_image_cw();
              if (find_sea_monster() == 0) {
                rotate_image_cw();
                if (find_sea_monster() == 0) {
                  print "WTF? NO SEA MONSTERS?"
                }
              }
            }
          }
        }
      }
    }
  }

  print
  print "SEA MONSTERS " LLEN " x " LLEN
  print_image()
  print find_sea_monster();
  res = 0;
  for (p = 1; p <= LLEN; ++p)
  for (q = 1; q <= LLEN; ++q)
    if (image[p,q] == "#") ++res;
  print res;
}
