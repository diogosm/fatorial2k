# Fatorial 2k

Obs.: some fun with factorial 2k design of experiments using Python. That's an on going research/learning, so pay attention for any incomplete behavior or incomplete coding.

Things to pay attention:

- This code works as follows: put `k={number of factors}` in the first line and in the following `2^k` put the results of your experiments. Pay attention that these lines need to have the same amount of experiments. Ex. for two factors A and B and 3 measures:

```
2
28 25 27
36 32 32
18 19 23
31 30 29
```

# Running

```
python fatorial2k.py < input.in
```
# Referências

[[1]](http://leg.ufpr.br/~fernandomayer/aulas/ce074/fatorial_2-3.html)

[[2]](https://edisciplinas.usp.br/pluginfile.php/2100277/mod_resource/content/1/fatoriais%202ak%20fracionados%20II.pdf)

[[3]](https://www.stat.washington.edu/pds/stat502/LectureNotes/2k.factorial.intro.pdf)
