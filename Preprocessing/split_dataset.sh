input=${1?"Input file must be specified"}
in_file=tmp.txt

cat $input > $in_file

rm -f train.txt
rm -f validate.txt

shuf $in_file >> shuf_corpus.txt

wc -l shuf_corpus.txt > x.txt
read lines fname < x.txt
echo total lines = $lines

train=$(($lines / 4 * 3))
validate=$(($lines / 4 ))
echo $(($train + $validate))

echo

head -n $train shuf_corpus.txt > train.txt
wc -l train.txt

echo
 
tail -n $validate shuf_corpus.txt > validate.txt
wc -l validate.txt

echo
   
rm -f x.txt
rm -f tmp.txt
rm -f shuf_corpus.txt
