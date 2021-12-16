for f in q*_*.py
do
    python3 "$f" >> "$f.res"
done