function array_swap(a,i,j) { _t = a[i]; a[i] = a[j]; a[j] = _t }
function array_sort(a) {
  do {
    _haschanged = 0
    for(_i=1; _i < length(a); _i++)
      if (a[_i] > a[_i+1]) {
        array_swap(a,_i,_i+1); _haschanged = 1
      }
  } while (_haschanged == 1)
}
{ split($0,a,""); n=length(a); for (i=1;i<=n;++i) b[NR,i]=a[i]; m=NR }
END {
  for (i=1;i<=m;++i) { b[i,0]=9; b[i,n+1]=9 }
  for (j=1;j<=n;++j) { b[0,j]=9; b[m+1,j]=9 }
  for (i=1;i<=m;++i)
  for (j=1;j<=n;++j) {
    if (b[i,j]<b[i+1,j] && b[i,j]<b[i-1,j] && b[i,j]<b[i,j+1] && b[i,j]<b[i,j-1]) { basin[i,j]=++k; size[k]=1 }
  }
  do {
    finished=1
    for (i=1;i<=m;++i)
    for (j=1;j<=n;++j) {
      if (b[i,j]==9) { basin[i,j]=" "; continue }
      if (basin[i,j]>0) continue
      if (basin[i+1,j]>0) { basin[i,j]=basin[i+1,j]; ++size[basin[i,j]]; finished=0 }
      else if (basin[i-1,j]>0) { basin[i,j]=basin[i-1,j]; ++size[basin[i,j]]; finished=0 }
      else if (basin[i,j+1]>0) { basin[i,j]=basin[i,j+1]; ++size[basin[i,j]]; finished=0 }
      else if (basin[i,j-1]>0) { basin[i,j]=basin[i,j-1]; ++size[basin[i,j]]; finished=0 }
    }
  } while (!finished)
  array_sort(size); k=length(size)
  print size[k] "*" size[k-1] "*" size[k-2] " = " size[k] * size[k-1] * size[k-2]
}
