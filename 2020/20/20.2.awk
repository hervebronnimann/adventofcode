function reverse(x) { y=""; for(j=length(x);j>0;--j) y=y substr(x,j,1); return y; } 
function ccw(n) { if (n<0) return -cw(-n); return n==1 ? 4 : n-1; }
function cw(n) { if (n<0) return -ccw(-n); return n==4 ? 1 : n+1; }
function abs(x) { return x<0 ? -x : x; }

/^Tile/ { ++ntiles; current = $2; r = 0; }
/^[.#]+$/ {
  row[++r,current] = $0; LEN = length($0);
  if (r == 1) side[1,current] = $0;
}
/^$/ {
  # Keep tile borders clockwise, 1=top, 2=right, 3=bottom(reverse), 4=left(reverse)
  side[3,current] = reverse(row[r,current]);
  side[2,current] = ""; side[4,current] = "";
  for (i=1;i<=r;++i) {
    side[2,current] = side[2,current] substr(row[i,current],LEN,1);
    side[4,current] = side[4,current] substr(row[r-i+1,current],1,1);
  }
  delete row; r = 0;
  # Insert tile borders into map
  for (i=1; i<=4; ++i) {
    x = side[i,current]; mapid[x,++mapn[x]] = current; maps[x,mapn[x]] = i;
    print "Tile " current " side " i " " x " matching " reverse(x)
  }
}

function rotate_tile_ccw(id) {
  # OUCH but who cares about performance at this point
  rotate_tile_cw(id);
  rotate_tile_cw(id);
  rotate_tile_cw(id);
}

function rotate_tile_cw(id) {
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
  side[1,id] = side[4,id]; for (kk=1; kk<=mapn[x]; ++kk) { xx = side[1,id]; if (mapid[xx,kk] == id) maps[xx,kk] = cw(i); }
  side[4,id] = side[3,id]; for (kk=1; kk<=mapn[x]; ++kk) { xx = side[4,id]; if (mapid[xx,kk] == id) maps[xx,kk] = cw(i); }
  side[3,id] = side[2,id]; for (kk=1; kk<=mapn[x]; ++kk) { xx = side[3,id]; if (mapid[xx,kk] == id) maps[xx,kk] = cw(i); }
  side[2,id] = temp;       for (kk=1; kk<=mapn[x]; ++kk) { xx = side[2,id]; if (mapid[xx,kk] == id) maps[xx,kk] = cw(i); }
}

function remove_from_map(xx,id) {
  for (kk = 1; kk <= mapn[xx]; ++k)
    if (mapid[xx,kk] == id) {
      while (++kk <= mapn[xx]) { mapid[xx,kk-1] = mapid[kk,kk]; maps[xx,kk-1] = maps[xx,kk]; }
      --mapn[xx];
    }
}

function flip_tile_horiz(id) {
  for (i=1; i<=LEN; ++i) {
    row[i,id] = reverse(row[i,id]);
  }
  # Also flid sides and maps
  xx = side[1,id]; rxx = reverse(xx); remove_from_map(xx,id);
  side[1,id] = rxx; mapid[rxx,++mapn[rxx]] = id; maps[rxx,mapn[rxx]] = 1;
  xx = side[3,id]; rxx = reverse(xx); remove_from_map(xx,id);
  side[3,id] = rxx; mapid[rxx,++mapn[rxx]] = id; maps[rxx,mapn[rxx]] = 3;
}

function flip_tile_vert(id) {
  for (i=1; i<LEN-i+1; ++i) {
    temp = row[i,id];
    row[i,id] = row[LEN-i+1,id];
    row[LEN-i+1,id] = temp;
  }
  # Also flid sides and maps
  xx = side[2,id]; rxx = reverse(xx); remove_from_map(xx,id);
  side[2,id] = rxx; mapid[rxx,++mapn[rxx]] = id; maps[rxx,mapn[rxx]] = 1;
  xx = side[4,id]; rxx = reverse(xx); remove_from_map(xx,id);
  side[4,id] = rxx; mapid[rxx,++mapn[rxx]] = id; maps[rxx,mapn[rxx]] = 3;
}

function fill_image(r,c,id) {
  # Assume that tile has already been rotated and flipped
  r = (r-1)*(LEN-2)+1; c = (c-1)*(LEN-2)+1; # forget about boundaries
  for (p = 0; p < LEN-2; ++p)
  for (q = 0; q < LEN-2; ++q)
    image[r+p,c+q] = substr(row[p+2,id],q+2,1);
}

END {
  SIDE=sqrt(ntiles);
  print "Tiles " ntiles " borders " SIDE*4

  # Find border tiles, keep count by id, corners will have count==2, others count==1
  for (x in mapn) {
    rx = reverse(x);
    if (mapn[x] == 1 && !(rx in mapn)) {
      print "Found border " x " side " maps[x,1] " id " mapid[x,1];
      borderx[++bordern[mapid[x,1]]] = x;
    } else {
      # There are no multiple matches so every border matches exactly another tile
      if (mapn[x] == 2) {
        print "Found match " x " side " maps[x,1] " id " mapid[x,1] " with side " -maps[x,2] " id " mapid[x,2];
      } else { # second tile is at most rotated 
        print "Found match " x " side " maps[x,1] " id " mapid[x,1] " with side +" maps[rx,1] " id " mapid[rx,1];
      }
    }
  }

  # Identify one corner, and stitch the image together
  for (id in bordern) {
    if (bordern[id] == 2) {
      x1 = borderx[1]; s1 = maps[x1,1];
      if (maps[x1,2] == cw(s1)) {
        x1 = borderx[1]; s1 = maps[x,1];
      } else if (maps[x1,2] != ccw(s1) {
        print "WTF ABORT"; exit;
      }
      print "Found corner " id " top side " s1 " with " x1
      while (s1 != 1) { rotate_tile_cw(id); s1 = cw(s1); }

      # Fill image row by row by stitching
      for (rr = 1; rr <= SIDE; ++rr) {
        # Invariant: first square on the row is id, top side 1 x1
        fill_image(rr,1,id);

        for (cc = 2; cc <= SIDE; ++cc) {
          # Find right neighbor id (rnid)
          x2 = signed_side(cw(s1),id); rx2 = reverse(x2);
          if (mapn[x2] == 2) { # second tile is flipped and perhaps rotated
            if (mapid[x2,1]==id) { rnid = mapid[x2,2]; rsid = -ccw(maps[x,2]); }
            else if (mapid[x2,2]==id) { rnid = mapid[x2,1]; rsid = -ccw(maps[x,1]); }
            else { print "WTF RN ABORT"; exit; }
          } else if (rx2 in mapn) {
            rnid = mapid[rx2,1]; rsid = cw(maps[rx2,1]); }
            else { print "WTF RN ABORT"; exit; }

          } else {
            print "WTF RN2 ABORT"; exit;
          }
  
          #
          fill_image(rr,cc,x1,s1);
        }
       
        # Set up next loop by starting at bottom neighbor
        if (rr < SIDE) {
          # Find bottom neighbor for going to next row later
          x3 = side[3,first_id];
          if (mapn[x3] == 2) { # bottom tile is flipped and perhaps rotated
            if (mapid[x3,1]==id) { bbid = mapid[x3,2]; bbs1 = maps[x3,2]; }
            else if (mapid[x3,2]==id) { bbid = mapid[x3,1]; bbs1 = maps[x3,1]; }
            else { print "WTF RN ABORT"; exit; }
            if (bbs1 == 1) { flip_tile_horiz(bbid)
            else if (bbs1 == 2) flip_tile_horiz(bbid)
          } else if (rx2 in mapn) {
            bbid = mapid[rx2,1]; rsid = cw(maps[rx2,1]);
            else { print "WTF RN ABORT"; exit; }

          } else {
            print "WTF RN2 ABORT"; exit;
          }
          id = bbid;
        }

      }
      break; ## DONE filling image
    }
  }

  # Find the sea monsters
}
