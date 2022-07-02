paper=$1

mkdir garbage

python pdfsplit.py ${paper}.pdf garbage

# gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dPDFSETTINGS=/printer -dCompatibilityLevel=1.4 -sOutputFile=figures-2-comp.pdf figures-2.pdf
# mv figures-2-comp.pdf figures-2.pdf
shift

while (( "$#" >= 2 )); do
  src=garbage/${paper}-$1.pdf
  dst=$2.pdf
  pdfcrop ${src} ${dst} &
  shift 2
done

wait
